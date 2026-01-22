from flask import Flask, jsonify, request, render_template
from sources.azoramoon import AzoraMoonSource
import os

app = Flask(__name__, template_folder='web', static_folder='web')

# تهيئة المصادر
sources = {
    'azoramoon': AzoraMoonSource()
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/home')
def api_home():
    source_name = request.args.get('source', 'azoramoon')
    source = sources.get(source_name)
    if not source:
        return jsonify({'error': 'Source not found'}), 404
    
    try:
        mangas = source.get_home()
        return jsonify(mangas)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/chapters')
def api_chapters():
    manga_url = request.args.get('url')
    source_name = request.args.get('source', 'azoramoon')
    if not manga_url:
        return jsonify({'error': 'URL is required'}), 400
        
    source = sources.get(source_name)
    try:
        chapters = source.get_chapters(manga_url)
        return jsonify(chapters)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/images')
def api_images():
    chapter_url = request.args.get('url')
    source_name = request.args.get('source', 'azoramoon')
    if not chapter_url:
        return jsonify({'error': 'URL is required'}), 400
        
    source = sources.get(source_name)
    try:
        images = source.get_images(chapter_url)
        return jsonify(images)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # سيتم تشغيله عبر main.py عادةً
    app.run(host='0.0.0.0', port=5000, debug=True)
