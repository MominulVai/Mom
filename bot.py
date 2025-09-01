import telebot
import os
import openai

# API Keys (Railway এর Environment Variables থেকে নিবে)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_KEY

# Start Command
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "হাই! আমি একটি AI Auto-Reply Bot 🤖\nযা কিছু জিজ্ঞেস করো।")

# Handle Messages
@bot.message_handler(func=lambda m: True)
def chat_with_ai(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "তুমি একজন helpful AI assistant."},
                {"role": "user", "content": message.text}
            ]
        )
        reply = response["choices"][0]["message"]["content"]
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

print("Bot is running...")
bot.infinity_polling()
