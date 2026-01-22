# 📖 Manga Live Bot (V2 - المصلحة)

نظام احترافي لقراءة المانهوا عبر Telegram WebApp، مصمم ليعمل بكفاءة على **Termux** مع دعم لمصادر متعددة وتجاوز مشاكل الحماية.

## 🚀 التحديثات الجديدة
- **إصلاح ظهور المانهوا**: تم تحديث كود الاستخراج ليتوافق مع الهيكلية الجديدة لموقع AzoraMoon.
- **مصادر متعددة**: إضافة مصدر **LekManga (مانجا ليك)** كبديل قوي.
- **دمج التوكنات**: تم تسهيل الإعداد بدمج التوكن والرابط مباشرة في `bot.py` (أو عبر `.env`).
- **واجهة محسنة**: WebApp أسرع مع إمكانية التنقل بين المصادر.

## 🛠️ التثبيت على Termux

1. قم بتحديث الحزم وتثبيت Python:
   ```bash
   pkg update && pkg upgrade
   pkg install python git
   ```

2. قم بتحميل المشروع:
   ```bash
   git clone https://github.com/w4900857-netizen/manga-live-bot-v2.git
   cd manga-live-bot-v2
   ```

3. تثبيت المكتبات المطلوبة:
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ الإعداد السريع

افتح ملف `bot.py` وقم بتعديل القيم التالية:
```python
BOT_TOKEN = "توكن_البوت_الخاص_بك"
WEB_URL = "رابط_ngrok_الخاص_بك"
```

## 🏃‍♂️ التشغيل
```bash
python main.py
```

## 📂 هيكلية المشروع
- `main.py`: تشغيل البوت والويب معاً.
- `sources/`: كلاسات الاستخراج (AzoraMoon, LekManga).
- `web/index.html`: واجهة المستخدم (WebApp).

---
صنع لدعم مجتمع المانهوا العربي. ❤️
