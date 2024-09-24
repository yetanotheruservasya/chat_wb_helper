import streamlit as st
import uuid
import Lib_WB
import Chains_WB
from dotenv import load_dotenv
import os

load_dotenv()
# Контакты и ссылки
trainer_email = os.getenv('TRAINER_EMAIL')
trainer_telegram = os.getenv('TRAINER_TELEGRAM')
course_channel = os.getenv('COURSE_CHANNEL')
chat_order_email = os.getenv('CHAT_ORDER_EMAIL')
developer_whatsapp = os.getenv('DEVELOPER_WHATSAPP')
website_link = os.getenv('WEBSITE_LINK')
linkedin_profile = os.getenv('LINKEDIN_PROFILE')
donation_link = os.getenv('DONATION_LINK')
calendly_link = os.getenv("CALENDLY_LINK")

# Задаем параметы страницы
st.set_page_config(page_title=' 🤖Чат о WB🧠', layout='centered')
st.title('🍇 Помощник менеджерам WB')
# Боковая панель с описанием и контактной информацией
with st.sidebar:
    st.header("О чате")
    st.write("""
    Этот чат создан для помощи начинающим пользователям WB (Wildberries).
    Вы можете задать любые вопросы, связанные с платформой, и получить быстрые ответы.
    """)

    # Использование переменных
    st.header("Станьте крутым продавцом!")
    st.write(f"""
    - 📧 Email: [Обратная связь]({trainer_email})
    - 📞 Telegram [Написать тренеру]({trainer_telegram})
    - 📢 Однокурсники [Канал курса]({course_channel})
    """)

    st.header("Хотите свой чат?")
    st.write(f"""
    - 📧 Email: [Заказать чат]({chat_order_email})
    - 📞 WhatsApp: [Написать разработчику]({developer_whatsapp})
    - 🌐 Веб-сайт: [boostyourproduct.tech]({website_link})
    - 🔗 LinkedIn: [Vasiliy Fadeev]({linkedin_profile})
    """)

    # Кнопка для оплаты
    st.header("Поддержите проект")
    st.write("""
    Если вам понравился чат и вы хотите поддержать проект, вы можете сделать пожертвование.
    """)
    st.markdown(
        f"""
        <a href={donation_link} target="_blank" style="text-decoration: none;">
            <div style="background-color: #4CAF50; color: white; padding: 10px 20px; text-align: center; border-radius: 5px; display: inline-block;">
                Поддержать проект
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

    # Ссылка на встречу через Calendly
    st.header("Обсудить проект?")
    st.write("""
    Если у вас есть вопросы по проекту или вы хотите обсудить сотрудничество, вы можете записаться на встречу.
    """)
    st.markdown(
        f"""
        <a href={calendly_link} target="_blank" style="text-decoration: none;">
            <div style="background-color: #1E90FF; color: white; padding: 10px 20px; text-align: center; border-radius: 5px; display: inline-block;">
                Записаться на встречу
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

# Проверяем наличие session_id в сессии
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
session_id = st.session_state.session_id

# Инициализация памяти чатов в сессии пользователя
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = {}

# Инициализация истории в сессии
if 'past' not in st.session_state:
    st.session_state['past'] = []  # Сообщения пользователя
if 'generated' not in st.session_state:
    st.session_state['generated'] = []  # Ответы ассистента

# Создаем контейнеры для истории чата и формы ввода
form_container = st.container()
form_help = st.container()
download_container = st.container()

# Форма для ввода нового сообщения
with form_container:
    with st.form('my_form'):
        text = st.text_area('Введите текст:', 'Что делает WB?')
        submitted = st.form_submit_button('Отправить')
        if submitted:
            Chains_WB.generate_response(text, session_id)

# Кнопка для скачивания истории чата
with download_container:
    # Подготовка данных для скачивания с использованием функции
    download_str = Lib_WB.prepare_chat_history()

    if download_str:
        # Создаем три колонки для кнопок
        col0, col1, col2, col3 = st.columns([4, 1, 1, 1])  # Первую колонку сделаем больше для текста
        with col0:
            st.markdown("**Сохраните историю или отправьте ее разработчику**")

        # Используем `st.empty()` для статуса отправки
        status_placeholder = st.empty()

        with col1:
            # Кнопка для скачивания истории
            st.download_button(
                label="💾", 
                data=download_str, 
                file_name='chat_history.txt', 
                mime='text/plain'
            )
        
        with col2:
            # Кнопка для положительного отзыва
            if st.button("👍", key="positive_feedback"):
                feedback = Lib_WB.handle_feedback("positive", download_str)
                # print(feedback)
                # Отображение статуса отправки в placeholder
                status_placeholder.success("Спасибо за ваш положительный отзыв!")

        with col3:
            # Кнопка для отрицательного отзыва
            if st.button("👎", key="negative_feedback"):
                feedback = Lib_WB.handle_feedback("negative", download_str)
                # print(feedback)
                # Отображение статуса отправки в placeholder
                status_placeholder.error("Спасибо за ваш отзыв. Мы постараемся улучшить качество чата.")


if st.session_state["generated"]:
    # Отображение истории чатов
    with st.expander("История чата", expanded=True):
        history_container = st.container(height=400)
        with history_container:
            for i in range(len(st.session_state['generated'])):
                st.info(st.session_state["past"][i], icon="🧐")
                st.success(st.session_state["generated"][i], icon="🤖")

with form_help:
    # Добавление свернутого блока с красиво отформатированными подсказками
    with st.expander("Что спросить?", expanded=False):
        st.markdown(
            """
            ## Возможные вопросы для обсуждения:

            ### 1. Описание площадки WB
            - **Что делает WB?**
            - **Какие инструменты работы с WB бывают?**

            ### 2. Роль менеджера
            - **Чем менеджер личного кабинета маркетплейса отличается от продавца (seller)?**
            - **Зачем нанимают менеджера для личного кабинета маркетплейса?**
            - **Какие основные услуги предоставляет менеджер?**
            - **Какие дополнительные услуги предоставляет менеджер?**
            - **Что должен уметь менеджер?**
            - **Какие доступы у менеджера должны быть для работы?**

            ### 3. Трудоустройство и документы
            - **Менеджер и работодатель**
            - **Менеджер и площадка**
            - **Менеджер и налоговая**
            - **Менеджер и WB**

            ### 4. Начало работы
            - **Что делать в первый день?**
            - **Что можно продать и на каких условиях?**

            **Если у вас есть другой вопрос, не стесняйтесь задавать его!**
            """,
            unsafe_allow_html=False
        )