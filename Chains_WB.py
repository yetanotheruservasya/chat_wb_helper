import sqlite3
import struct
import numpy as np
import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory

# Загрузка ключа API из файла .env
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
PATH_TO_EMBEDINGS_DB = os.getenv('PATH_TO_EMBEDINGS_DB')
print(PATH_TO_EMBEDINGS_DB)
llm = ChatOpenAI(api_key=openai_api_key, temperature=0.7, model="gpt-4o-mini")

# 1. Функция для извлечения данных из SQLite
def fetch_embeddings_from_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('SELECT sentence, embedding FROM sentence_embeddings')
    rows = cursor.fetchall()
    
    sentences = []
    embeddings = []
    
    for sentence, embedding_blob in rows:
        # Конвертируем бинарные данные обратно в массив float
        embedding_length = len(embedding_blob) // 4  # Каждый float занимает 4 байта
        embedding = struct.unpack(f'{embedding_length}f', embedding_blob)
        
        sentences.append(sentence)
        embeddings.append(np.array(embedding))
    
    conn.close()
    
    return sentences, np.array(embeddings)

# 2. Получаем эмбеддинги и предложения из SQLite
sentences, embeddings = fetch_embeddings_from_db(PATH_TO_EMBEDINGS_DB)

# 3. Создаем объект Embeddings
embedding_function = OpenAIEmbeddings(api_key=openai_api_key, model="text-embedding-ada-002")

# 4. Создаем FAISS VectorStore с помощью FAISS.from_embeddings
text_embedding_pairs = zip(sentences, embeddings)
faiss_store = FAISS.from_embeddings(text_embedding_pairs, embedding_function)

# 5. Создаем Retriever
retriever = faiss_store.as_retriever(search_type="similarity", k=8)

### Contextualize question ###
contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)
contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

### Answer question ###
system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

history_aware_retriver = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)
combine_docs_chain = create_stuff_documents_chain(llm, qa_prompt, output_parser=StrOutputParser())
qa_chain = create_retrieval_chain(history_aware_retriver, combine_docs_chain)

# Получаем историю сессии
def get_session_history(session_id: str) -> ChatMessageHistory:
    if session_id not in st.session_state.chat_history:
        st.session_state.chat_history[session_id] = ChatMessageHistory()
    return st.session_state.chat_history[session_id]

# Формируем цепочку выполнения
conversational_rag_chain = RunnableWithMessageHistory(
    qa_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)

# Функция получения ответа от модели 
def generate_response(input_text, session_id):
    # Получаем текущую историю чатов
    history = get_session_history(session_id)

    # Подготовка данных для выполнения цепочки
    answer = conversational_rag_chain.invoke(
        {
            "input": input_text,
            "chat_history": history.messages  # передача истории сообщений
        },
        config={"configurable": {"session_id": session_id}},
    )
    
    # Извлекаем текст ответа
    answer_text = answer["answer"]

    # Сохраняем запрос и ответ в истории
    st.session_state['past'].append(input_text)  # Добавляем пользовательский запрос
    st.session_state['generated'].append(answer_text)  # Добавляем ответ модели
    
    # Отображаем результат
    st.info(answer_text, icon="🤖")

    # Возвращаем текст ответа
    return answer_text