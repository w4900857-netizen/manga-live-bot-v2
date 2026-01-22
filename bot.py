import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import os

# --- الإعدادات المباشرة (دمج التوكن والرابط كما طلبت) ---
BOT_TOKEN = "8355857057:AAHzyZ2J0yMpGiN8VEa8cyBnt_LoRN_2hjk" # ضع التوكن الخاص بك هنا
WEB_URL = "https://unrhythmic-kaiden-incomputably.ngrok-free.dev"   # ضع رابط ngrok الخاص بك هنا
# --------------------------------------------------

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    # زر فتح الـ WebApp
    webapp_button = InlineKeyboardButton(
        text="قراءة المانهوا 📖", 
        web_app=WebAppInfo(url=WEB_URL)
    )
    markup.add(webapp_button)
    
    welcome_text = (
        "👋 أهلاً بك في Manga Live!\n\n"
        "أفضل تجربة لقراءة المانهوا والمانجا مباشرة داخل تيليغرام.\n"
        "• مصادر متعددة (Azora, MangaLek)\n"
        "• واجهة سريعة وخفيفة\n"
        "• دعم كامل للهواتف\n\n"
        "اضغط على الزر أدناه للبدء 👇"
    )
    try:
        bot.reply_to(message, welcome_text, reply_markup=markup)
    except Exception as e:
        print(f"Error sending welcome: {e}")

def run_bot():
    print(f"Bot is starting with URL: {WEB_URL}")
    # حذف الويب هوك القديم لتجنب التعارض
    bot.remove_webhook()
    try:
        # استخدام infinity_polling لضمان استمرار العمل وتجنب أخطاء Conflict
        bot.infinity_polling(timeout=20, long_polling_timeout=10)
    except Exception as e:
        print(f"Bot polling error: {e}")

if __name__ == '__main__':
    run_bot()
