import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
# Отправка сообщений в TG
# Ваш токен бота и ID канала
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')

def send_message_to_channel(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHANNEL_ID,
        'text': message
    }
    response = requests.post(url, data=payload)
    #print(f"Канал: {TELEGRAM_CHANNEL_ID} \t Бот: {TELEGRAM_CHANNEL_ID}")
    return response.json()

# Использование функции для отправки сообщений
def handle_feedback(feedback_type, chat_history):
    if feedback_type == "positive":
        subject = "Положительный отзыв о чате"
        body = f"Здравствуйте!\n\nЯ хотел(а) сообщить, что мне очень понравился ваш чат. Все вопросы были хорошо освещены, и я получил(а) нужную информацию.\n\nВот история моего чата:\n\n{chat_history}\n\nС наилучшими пожеланиями,\n[Ваше Имя]"
    elif feedback_type == "negative":
        subject = "Отрицательный отзыв о чате"
        body = f"Здравствуйте!\n\nК сожалению, я не получил(а) удовлетворительных ответов в вашем чате. Мне кажется, что некоторые вопросы не были должным образом освещены.\n\nВот история моего чата:\n\n{chat_history}\n\nПожалуйста, обратите внимание на мои комментарии и постарайтесь улучшить качество ответов.\n\nС уважением,\n[Ваше Имя]"

    sending_status = send_message_to_channel(body)
    return sending_status

# Подготовка истории чата
def prepare_chat_history():
    chat_history = ""
    for i in range(len(st.session_state['generated'])):
        chat_history += f"Пользователь:\n{st.session_state['past'][i]}\n"
        chat_history += f"Чат-бот:\n{st.session_state['generated'][i]}\n"
        chat_history += "="*40 + "\n"
    return chat_history