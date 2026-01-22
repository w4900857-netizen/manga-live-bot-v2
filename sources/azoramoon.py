from .base import BaseSource
from bs4 import BeautifulSoup
import re

class AzoraMoonSource(BaseSource):
    def __init__(self):
        super().__init__()
        self.base_url = "https://azoramoon.com"

    def get_home(self):
        url = f"{self.base_url}/series/"
        try:
            response = self.scraper.get(url, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            mangas = []
            
            # البحث عن الكروت بناءً على الهيكلية التي وجدناها في الفحص
            # الكروت تحتوي على روابط تبدأ بـ /series/
            items = soup.find_all('a', href=re.compile(r'^/series/[^/]+$'))
            seen_urls = set()
            
            for item in items:
                href = item.get('href')
                if not href: continue
                full_url = self.base_url + href if href.startswith('/') else href
                
                if full_url in seen_urls or "/series/page/" in full_url:
                    continue
                
                # استخراج العنوان من الـ alt الخاص بالصورة أو النص
                img_tag = item.find('img')
                title = img_tag.get('alt', '').replace('Cover of ', '') if img_tag else item.get_text(strip=True)
                img_url = img_tag.get('src') if img_tag else None
                
                if not title:
                    # محاولة البحث عن العنوان في العناصر المجاورة
                    parent = item.parent
                    title_elem = parent.find('a', class_=re.compile(r'text|font'))
                    if title_elem:
                        title = title_elem.get_text(strip=True)

                if title and full_url:
                    mangas.append({
                        'title': title,
                        'url': full_url,
                        'thumbnail': img_url,
                        'source': 'azoramoon'
                    })
                    seen_urls.add(full_url)
            
            return mangas[:30]
        except Exception as e:
            print(f"Error in AzoraMoon get_home: {e}")
            return []

    def get_chapters(self, manga_url):
        try:
            response = self.scraper.get(manga_url, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            chapters = []
            
            # روابط الفصول تحتوي على /chapter-
            links = soup.find_all('a', href=re.compile(r'/chapter-'))
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
        except Exception as e:
            print(f"Error in AzoraMoon get_chapters: {e}")
            return []

    def get_images(self, chapter_url):
        try:
            response = self.scraper.get(chapter_url, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            images = []
            
            # البحث عن الصور في الصفحة
            img_tags = soup.find_all('img')
            for img in img_tags:
                src = img.get('src') or img.get('data-src')
                if src and ('storage.azoramoon.com' in src or 'upload' in src):
                    if not src.startswith('http'):
                        src = 'https:' + src if src.startswith('//') else self.base_url + src
                    images.append(src)
            return images
        except Exception as e:
            print(f"Error in AzoraMoon get_images: {e}")
            return []
