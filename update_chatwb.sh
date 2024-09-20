#!/bin/bash

# Проверка параметров
if [ "$#" -ne 1 ]; then
    echo "Использование: $0 <container_name>"
    exit 1
fi

# Настройки
CONTAINER_NAME=$1                        # Имя контейнера передается как параметр
IMAGE_NAME="yetanotheruservasya/main:tagname"   # Имя вашего образа
ENV_FILE=".env"           # Путь к вашему .env файлу
DB_FILE="/your_full_path/embeddings.db"  # Путь к файлу базы данных
PORT="8501"                              # Порт для перенаправления

# Удаляем старый контейнер, если он существует
if [ $(docker ps -a -q -f name=$CONTAINER_NAME) ]; then
    echo "Остановка и удаление старого контейнера..."
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

# Пулл нового образа
echo "Загрузка нового образа с Docker Hub..."
docker pull $IMAGE_NAME

# Запускаем новый контейнер
echo "Запуск нового контейнера..."
docker run --env-file $ENV_FILE -v $DB_FILE:/app/embeddings.db -p $PORT:$PORT -d --name $CONTAINER_NAME $IMAGE_NAME

echo "Контейнер запущен!"
