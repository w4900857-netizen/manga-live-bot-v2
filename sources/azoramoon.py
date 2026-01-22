from .base import BaseSource
from bs4 import BeautifulSoup
import re

class AzoraMoonSource(BaseSource):
    def __init__(self):
        super().__init__()
        self.base_url = "https://azoramoon.com"

    def get_home(self):
        url = f"{self.base_url}/series/"
        response = self.scraper.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        mangas = []
        
        # البحث عن روابط السلاسل
        # بناءً على الفحص، السلاسل تكون داخل روابط تحتوي على /series/
        items = soup.find_all('a', href=re.compile(r'/series/[^/]+$'))
        seen_urls = set()
        
        for item in items:
            href = item.get('href')
            if href.startswith('/'):
                href = self.base_url + href
            
            if href in seen_urls or "/series/page/" in href:
                continue
                
            title = item.get_text(strip=True)
            img_tag = item.find('img')
            img_url = img_tag.get('src') if img_tag else None
            
            if title and href:
                mangas.append({
                    'title': title,
                    'url': href,
                    'thumbnail': img_url
                })
                seen_urls.add(href)
        
        return mangas[:20] # إرجاع أول 20 نتيجة

    def get_chapters(self, manga_url):
        response = self.scraper.get(manga_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        chapters = []
        
        # البحث عن روابط الفصول
        links = soup.find_all('a', href=re.compile(r'/series/.+/chapter-.+'))
        for link in links:
            title = link.get_text(strip=True)
            url = link.get('href')
            if url.startswith('/'):
                url = self.base_url + url
            
            if title and url:
                chapters.append({
                    'title': title,
                    'url': url
                })
        
        return chapters

    def get_images(self, chapter_url):
        response = self.scraper.get(chapter_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        images = []
        
        # البحث عن الصور داخل div يحتوي على الصور
        img_tags = soup.find_all('img')
        for img in img_tags:
            src = img.get('src') or img.get('data-src')
            if src and ('storage.azoramoon.com' in src or 'upload' in src):
                if not src.startswith('http'):
                    src = 'https:' + src if src.startswith('//') else self.base_url + src
                images.append(src)
        
        return images

    def search(self, query):
        # البحث في الموقع (غالباً عبر query parameter)
        url = f"{self.base_url}/series/?search={query}"
        response = self.scraper.get(url)
        # نفس منطق get_home تقريباً
        return self.get_home() # للتبسيط حالياً
