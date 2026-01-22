import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEB_URL = os.getenv('WEB_URL')

if not BOT_TOKEN:
    print("Error: BOT_TOKEN not found in environment variables.")
if not WEB_URL:
    print("Error: WEB_URL not found in environment variables.")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    # إضافة زر WebApp
    webapp_button = InlineKeyboardButton(
        text="فتح قارئ المانهوا 📖", 
        web_app=WebAppInfo(url=WEB_URL)
    )
    markup.add(webapp_button)
    
    welcome_text = (
        "👋 أهلاً بك في بوت قارئ المانهوا!\n\n"
        "يمكنك الآن قراءة المانهوا المفضلة لديك مباشرة داخل تيليغرام.\n"
        "اضغط على الزر أدناه للبدء."
    )
    bot.reply_to(message, welcome_text, reply_markup=markup)

def run_bot():
    print("Bot is starting...")
    try:
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    except Exception as e:
        print(f"Bot error: {e}")

if __name__ == '__main__':
    run_bot()
