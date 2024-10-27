import telebot
from transformers import pipeline
bot = telebot.TeleBot("Token")
pipe = pipeline("text-generation", model="distilbert/distilgpt2")

@bot.message_handler(content_types=['text'])
def start(msg):
    if msg.text == '/start':
        bot.send_message(msg.from_user.id, "Этот бот работает на gpt-2 урезвнной версии.")
    else:
        bot.send_message(msg.from_user.id, "Бот начал думать над вашим ответом, ждите и вы дождетесь.")
        ai_msg = pipe(msg.text, max_length=150, do_sample=False, temperature=1.0, top_k=50, top_p=0.85, num_return_sequences=1)[0]['generated_text']
        bot.send_message(msg.from_user.id, ai_msg)

while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        pass
