from telebot import TeleBot, formatting, types

from src.markup import MARKUP_BIENVENIDA, MARKUP_LOGUP
from src.msg import MSG_BIENVENIDA, MSG_LOGUP

from .db_config import *


def mandar_bienvenida(message: types.Message, bot: TeleBot):
    bot.send_message(message.json["chat"]["id"],
                     formatting.format_text(
        f"¡Hola, {message.from_user.first_name}\\!\n\n",
        "Te doy la bienvenida👋🏾\\.\n\n",
        *MSG_BIENVENIDA,
        separator=" "  # separator separates all strings
    ),
        reply_markup=MARKUP_BIENVENIDA,
        parse_mode='MarkdownV2')
    print(message.from_user.username)


def validarUsuario() -> bool:
    encontrado = False

    return encontrado


def registrar_jugador_1(call_id: int, chat_id: int, message_id: int, bot: TeleBot):
    bot.answer_callback_query(call_id, "¡Empezamos!")
    bot.edit_message_text(
        formatting.format_text(
            *MSG_LOGUP[0],
            separator=" "  # separator separates all strings
        ),
        chat_id,
        message_id,
        reply_markup=MARKUP_LOGUP[0],
        parse_mode='MarkdownV2')


def volver_bienvenida(call_id: int, chat_id: int, message_id: int, first_name: str, bot: TeleBot):
    bot.edit_message_text(
        formatting.format_text(
            f"¡Hola de nuevo, {first_name}\!\n\n",
            *MSG_BIENVENIDA,
            separator=" "  # separator separates all strings
        ),
        message_id,
        call_id,
        reply_markup=MARKUP_BIENVENIDA,
        parse_mode='MarkdownV2')
