import telebot
from telebot import formatting

from src.bot_config import bot
from src.functions import *


# Maneja el primer mensaje '/start' o próximos /start.
@bot.message_handler(commands=['start'])
def handle_start(message: telebot.types.Message):

    # VERIFICA EL USUARIO
    if validarUsuario():
        pass  # Lo inicia directamente en el sistema
    else:
        mandar_bienvenida(message, bot)
    # Si no encontramos identificado este usuario le pedimos que se registre o se identifique


@bot.callback_query_handler(func=lambda call: call.data[:2] == "cb")
def callback_bienvenida(call: telebot.types.CallbackQuery):

    if call.data == "cb_logup":
        registrar_jugador_1(
            call.id, call.message.json["chat"]["id"], call.message.id, bot)
    elif call.data == "cb_login":
        bot.answer_callback_query(call.id, "Answer is No")


@bot.callback_query_handler(func=lambda call: call.data[:2] == "vl")
def callback_volver(call: telebot.types.CallbackQuery):
    if call.data == "vl_volver1":
        volver_bienvenida(
            call.id, call.message.json["chat"]["id"], call.message.id, call.from_user.first_name, bot)
    elif call.data == "vl_login":
        bot.answer_callback_query(call.id, "Answer is No")


@bot.callback_query_handler(func=lambda call: call.data[:2] == "lu")
def callback_logup(call: telebot.types.CallbackQuery):
    if call.data == "lu1_ok":
        volver_bienvenida(
            call.id, call.message.json["chat"]["id"], call.message.id, call.from_user.first_name, bot)
    elif call.data == "lu_login":
        bot.answer_callback_query(call.id, "Answer is No")

# Handles all sent documents and audio files


@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message: telebot.types.Message):
    print("B")

# Handles all text messages that match the regular expression


@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message: telebot.types.Message):
    print("C")


# Handles all messages for which the lambda returns True


@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_text_doc2(message: telebot.types.Message):
    print("D")


# Which could also be defined as:


def test_message(message: telebot.types.Message):
    print("E")
    if message.document is not None:
        return message.document.mime_type == 'text/plain'


@bot.message_handler(func=test_message, content_types=['document'])
def handle_text_doc(message: telebot.types.Message):
    print("F")


# Handlers can be stacked to create a function which will be called if either message_handler is eligible
# This handler will be called if the message starts with '/hello' OR is some emoji


@bot.message_handler(commands=['hello'])
@bot.message_handler(func=lambda msg: msg.text == ". 🙂")
def send_something(message: telebot.types.Message):
    print("G")
    # print(message)


# Handles all sent documents and audio files
@bot.message_handler(content_types=['text'])
def handle_docs_audio2(message: telebot.types.Message):
    print("H")
    # print(message.reply_markup.add("Hola"))
    # bot.edit_message_reply_markup(message.json["chat"]["id"],
    # reply_markup=markup
    # )

    bot.send_message(message.json["chat"]["id"],
                     'Text', reply_markup=MARKUP_BIENVENIDA)

    # bot.reply_to(message, "This is a message handler")
    # bot.edit_message_reply_markup(message,reply_markup=markup)
    print(message.json["text"])
    # print(message.json)


@bot.message_handler(func=lambda message: True, content_types=['audio', 'photo', 'voice', 'video', 'document', 'location', 'contact', 'sticker'])
def handle_docs_audio3(message: telebot.types.Message):
    print("I")
    print(message.json[message.content_type])
    # print(message.json)


@bot.edited_message_handler()
def handle_docs_audio4(message):
    print("I")
    print(message.json[message.content_type])
    # print(message.json)


# for i in bot.get_updates():
# 	print(i)
bot.infinity_polling()
