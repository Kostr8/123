# -*- coding: cp1251 -*-

#print("õóé")

import telebot
import time

bot = telebot.TeleBot('')

#Îáðàáîòàêà êîìàíäû /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Ïðèâåò! ß ïðèø¸ë ñïàñòè èêñòåðîâ îò ÏÈÄÎÐÛ. Íàïèøè /help, ÷òîáû óçíàòü, ÷òî ÿ óìåþ. ")

#Îáðàáîòàêà êîìàíäû /help
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "/kick - êèêíóòü ïîëüçîâàòåëÿ")

#Îáðàáîòêà êèêà
@bot.message_handler(commands=['kick'])
def kick_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Íåâîçìîæíî êèêíóòü àäìèíèñòðàòîðà.")
        else:
            bot.kick_chat_member(chat_id, user_id)
            bot.reply_to(message, f"Ïîëüçîâàòåëü {message.reply_to_message.from_user.username} áûë êèêíóò.")
    else:
        bot.reply_to(message, "Ýòà êîìàíäà äîëæíà áûòü èñïîëüçîâàíà â îòâåò íà ñîîáùåíèå ïîëüçîâàòåëÿ, êîòîðîãî âû õîòèòå êèêíóòü.")


#Ïåðåäà÷à ñîîáùåíèé áîòó èç òåëåãðàìà
bot.polling(none_stop=True, interval=0)


