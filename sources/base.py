import cloudscraper
from bs4 import BeautifulSoup

class BaseSource:
    def __init__(self):
        self.scraper = cloudscraper.create_scraper()
        self.base_url = ""

    def get_home(self):
        """يجب أن تعيد قائمة بالمانهوات في الصفحة الرئيسية"""
        raise NotImplementedError

    def get_chapters(self, manga_url):
        """يجب أن تعيد قائمة بالفصول لمانهوا معينة"""
        raise NotImplementedError

    def get_images(self, chapter_url):
        """يجب أن تعيد قائمة بروابط الصور لفصل معين"""
        raise NotImplementedError

    def search(self, query):
        """يجب أن تعيد نتائج البحث"""
        raise NotImplementedError
