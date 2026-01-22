# 📖 Manga Live Bot (Telegram WebApp)

نظام احترافي لقراءة المانهوا عبر Telegram WebApp، مصمم ليعمل بكفاءة على **Termux** (Android) وأي بيئة تدعم Python.

## 🚀 المميزات
- **Telegram WebApp**: واجهة مستخدم سلسة وسريعة داخل تطبيق التيليغرام.
- **نظام المصادر (Sources)**: هيكلية مرنة تسمح بإضافة مواقع مانهوا جديدة بسهولة.
- **متوافق مع Termux**: لا يحتاج إلى Playwright أو متصفحات ثقيلة.
- **Dark Mode**: واجهة مريحة للعين مصممة للهواتف.
- **خفيف وسريع**: يعتمد على Flask و BeautifulSoup.

## 🛠️ المتطلبات
- Python 3.11+
- حساب Telegram (للحصول على BOT_TOKEN)
- ngrok (لجعل الـ WebApp متاحاً عبر الإنترنت)

## 📦 التثبيت على Termux

1. قم بتحديث الحزم وتثبيت Python:
   ```bash
   pkg update && pkg upgrade
   pkg install python git
   ```

2. قم بتحميل المشروع:
   ```bash
   git clone https://github.com/YOUR_USERNAME/manga-live-bot.git
   cd manga-live-bot
   ```

3. تثبيت المكتبات المطلوبة:
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ الإعداد (Environment Variables)

قم بإنشاء ملف `.env` في المجلد الرئيسي للمشروع:
```bash
BOT_TOKEN=your_telegram_bot_token
WEB_URL=your_ngrok_https_url
```

### كيفية الحصول على الروابط:
1. **BOT_TOKEN**: من خلال [@BotFather](https://t.me/BotFather).
2. **WEB_URL**: استخدم ngrok لفتح منفذ 5000:
   ```bash
   ngrok http 5000
   ```
   انسخ رابط الـ **HTTPS** وضعه في `WEB_URL`.

## 🏃‍♂️ التشغيل
```bash
python main.py
```

## 📂 هيكلية المشروع
- `main.py`: ملف التشغيل الرئيسي (يشغل البوت والويب معاً).
- `app.py`: تطبيق Flask والـ API.
- `bot.py`: كود بوت التيليغرام.
- `sources/`: يحتوي على كلاسات استخراج البيانات من المواقع.
- `web/`: يحتوي على واجهة الـ WebApp (HTML/JS).

## 🛡️ ملاحظات تقنية
- المشروع يستخدم `cloudscraper` لتجاوز حماية Cloudflare البسيطة.
- تم تصميم نظام المصادر ليكون قابلاً للتوسعة؛ يمكنك إضافة أي موقع جديد عبر إنشاء ملف جديد في مجلد `sources` يرث من `BaseSource`.

---
صنع بكل حب لدعم مجتمع المانهوا العربي. ❤️
