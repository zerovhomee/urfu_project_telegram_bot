import telebot
import openai

OpenaAIkey = "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"
TgKey = "6431964212:AAEFA-isNUFeEf8WajXSg-Ycb5wNGYJP3rY"

openai.api_key = OpenaAIkey
bot = telebot.TeleBot(TgKey)


@bot.message_handler(regexp = '/choose')
def welcome(message):
    bot.send_message(message.chat.id , "Привет")


@bot.message_handler(content_types=["text"])
def talk(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.2,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.5
    )
    gpt_text = response["choices"][0]["text"]
    bot.send_message(message.chat.id, gpt_text)


bot.polling(none_stop=True)