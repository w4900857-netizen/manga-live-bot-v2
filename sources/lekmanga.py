from .base import BaseSource
from bs4 import BeautifulSoup
import re

class LekMangaSource(BaseSource):
    def __init__(self):
        super().__init__()
        self.base_url = "https://lekmanga.net"

    def get_home(self):
        url = f"{self.base_url}/manga-list/"
        try:
            response = self.scraper.get(url, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            mangas = []
            
            # هيكلية مانجا ليك تعتمد على كلاسات معينة للصور والعناوين
            items = soup.find_all('div', class_='manga-item') or soup.find_all('div', class_='bs')
            
            for item in items:
                link_elem = item.find('a')
                if not link_elem: continue
                
                href = link_elem.get('href')
                title = link_elem.get('title') or item.find('h3').get_text(strip=True) if item.find('h3') else ""
                img_tag = item.find('img')
                img_url = img_tag.get('src') if img_tag else None
                
                if title and href:
                    mangas.append({
                        'title': title,
                        'url': href,
                        'thumbnail': img_url,
                        'source': 'lekmanga'
                    })
            
            if not mangas:
                # محاولة استخراج عامة إذا فشلت الكلاسات المحددة
                links = soup.find_all('a', href=re.compile(r'/manga/[^/]+/$'))
                for link in links:
                    title = link.get_text(strip=True)
                    if title and len(title) > 2:
                        mangas.append({
                            'title': title,
                            'url': link.get('href'),
                            'thumbnail': None,
                            'source': 'lekmanga'
                        })
            
            return mangas[:30]
        except Exception as e:
            print(f"Error in LekManga get_home: {e}")
            return []

    def get_chapters(self, manga_url):
        try:
            response = self.scraper.get(manga_url, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            chapters = []
            
            # البحث عن قائمة الفصول
            links = soup.find_all('a', href=re.compile(r'/manga/.+/.+/'))
            for link in links:
                title = link.find('span', class_='chapternum')
                title = title.get_text(strip=True) if title else link.get_text(strip=True)
                url = link.get('href')
                if title and url and '/manga/' in url:
                    chapters.append({'title': title, 'url': url})
            return chapters
        except Exception as e:
            print(f"Error in LekManga get_chapters: {e}")
            return []

    def get_images(self, chapter_url):
        try:
            response = self.scraper.get(chapter_url, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            images = []
            
            # البحث عن الصور في منطقة القراءة
            reader_area = soup.find('div', id='readerarea')
            if reader_area:
                img_tags = reader_area.find_all('img')
            else:
                img_tags = soup.find_all('img')
                
            for img in img_tags:
                src = img.get('src') or img.get('data-src')
                if src and not 'data:image' in src:
                    images.append(src)
            return images
        except Exception as e:
            print(f"Error in LekManga get_images: {e}")
            return []
