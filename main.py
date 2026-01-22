import threading
import time
import os
from app import app
from bot import run_bot
from dotenv import load_dotenv

load_dotenv()

def start_flask():
    print("Starting WebApp on http://0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000, use_reloader=False)

if __name__ == '__main__':
    # التحقق من وجود التوكن
    if not os.getenv('BOT_TOKEN'):
        print("❌ خطأ: BOT_TOKEN غير موجود في ملف .env")
        exit(1)

    # تشغيل Flask في Thread منفصل
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # تشغيل البوت في الـ Thread الرئيسي
    time.sleep(2) # انتظار بسيط لتشغيل Flask
    run_bot()
