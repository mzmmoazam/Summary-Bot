import telebot
import re
import Algorithmia

bot = telebot.TeleBot(" Telegram API ")


@bot.message_handler(commands=['START'])
def yoyo(message):
    tee = "Hi,this bot is made mzm .Jmzm -- This  bot will summarise a website for u .Just enter  the link of the website "
    bot.reply_to(message, tee)


@bot.message_handler(func=lambda message: True)
def blab(message):
    try:
        input = message.text
        client = Algorithmia.client('Algorithmia API')
        if "://" in input and "https" in input:
            input = input.rsplit('://', 1)[1]
            assert not input == input.rsplit('/', 1)[1]
            input = "https://" + input
        elif "://" in input and "http" in input:
            input = input.rsplit('://', 1)[1]
            assert not input == input.rsplit('/', 1)[1]
            input = "http://" + input
        else:
            assert not input == input.rsplit('/', 1)[0]
        algo = client.algo('nlp/SummarizeURL/0.1.1')
        bot.reply_to(message, (algo.pipe(input)).result)
    except:
        bot.reply_to(message, "your link is not correct  or you have entered a base url...")


bot.polling()
