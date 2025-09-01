import os
import telebot
import openai

# Environment variable থেকে key নাও
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_KEY

@bot.message_handler(func=lambda message: True)
def reply(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        max_tokens=100
    )
    bot.reply_to(message, response.choices[0].text.strip())

bot.polling()
