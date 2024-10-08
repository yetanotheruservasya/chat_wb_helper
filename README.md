# Консультант для начинающих менеджеров WB

## Основная идея и уникальность

Проект создан как помощник для лектора, ведущего курсы для начинающих менеджеров на платформе Wildberries (WB). Основная цель чата — облегчить учебный процесс и оптимизировать время лектора. Лектор часто сталкивается с большим количеством однотипных вопросов, которые повторяются из группы в группу: что такое WB, какие инструменты работы существуют, как настроить личный кабинет и т.д. Отвечать на такие вопросы вручную для каждого учащегося может занимать значительное время.

Чат-бот решает эту проблему, позволяя делегировать ответы на типовые вопросы, обеспечивая быстрый и точный отклик для студентов. Это помогает лектору сосредоточиться на более сложных и индивидуальных запросах, требующих персонализированного подхода. Важно отметить, что чат-бот предлагает ответы, основываясь на базе знаний, которая была создана за два года работы лектора и заказчика с учениками и клиентами.

### Проблемы, которые решает чат:
1. **Время лектора**. Часто возникают простые вопросы вроде "Как настроить личный кабинет?" или "Какие основные задачи менеджера WB?". Такие вопросы требуют времени, которое можно было бы посвятить более сложным задачам.
2. **Самостоятельность обучающихся**. Студенты могут обучаться в удобном для них темпе, задавая вопросы в любое время, даже вне лекций. Это снижает зависимость от личного присутствия лектора и повышает вовлеченность.
3. **Единое качество ответов**. Автоматизация через чат-бота обеспечивает одинаковое качество ответов на вопросы, что минимизирует возможные ошибки или недопонимания со стороны обучающихся.
4. **Управление потоком вопросов**. Чат позволяет сортировать и фильтровать вопросы, помогая лучше организовать ответы и избежать перегрузки лектора.

### Примеры целей обучающихся:
- **Освоение платформы WB**. Большинство начинающих менеджеров не знакомы с внутренними процессами маркетплейса, и их главной целью является полное понимание работы платформы и инструментов.
- **Практическое применение знаний**. Задачи, как настроить рекламу, управлять заказами и анализировать данные — это ключевые темы для новичков.
- **Минимизация ошибок**. Менеджеры стремятся избежать типичных ошибок, связанных с размещением товаров и взаимодействием с покупателями.

### Цели лектора:
- **Оптимизация времени**. Вынести простые вопросы на автоматизированный чат-бот, чтобы сконцентрироваться на более сложных вопросах, возникающих у студентов.
- **Повышение эффективности курса**. За счет предоставления студентам возможности получать ответы быстро и вне лекций, курс становится более гибким и удобным для участников.
- **Поддержание стандарта качества**. Автоматизация ответа на типовые вопросы с использованием проверенной базы знаний позволяет сохранять единое качество обучения.

## Особенности реализации

1. **Чат с пользователем**:  
   Приложение предоставляет пользователям возможность задавать вопросы через текстовое поле. Вопросы обрабатываются с помощью модели OpenAI, которая анализирует их и генерирует ответы, соответствующие контексту и теме. Ассистент адаптирован для работы с вопросами, связанными с платформой Wildberries и задачами менеджеров.

2. **Контактная информация**:  
   В боковой панели приложения выводится контактная информация, которая включает:
   - Электронную почту и Telegram лектора для обратной связи.
   - Контакты разработчика для заказа персонализированного чата.
   - Ссылки на дополнительные ресурсы, такие как веб-сайт и профиль в LinkedIn.

3. **История чата**:  
   История чата хранится в сессии пользователя и позволяет пользователю видеть, какие вопросы он задавал ранее и какие ответы были предоставлены. Это помогает в отслеживании прогресса и понимании контекста обсуждений.

4. **Сохранение и скачивание истории**:  
   Приложение предоставляет пользователям возможность сохранить историю своих взаимодействий с чат-ассистентом. История может быть скачана в виде текстового файла, что удобно для последующего анализа или отправки.

5. **Обратная связь**:  
   Пользователи могут оценивать ответы чат-ассистента с помощью кнопок для положительного (👍) или отрицательного (👎) отзыва. Эти отзывы передаются разработчику через функцию обратной связи, что позволяет улучшать качество работы ассистента на основе реальных данных.

6. **Рекомендации для вопросов**:  
   В приложении реализован раздел с подсказками, который помогает пользователям ориентироваться в возможных вопросах для обсуждения. Вопросы структурированы по категориям и темам, что упрощает взаимодействие с чат-ассистентом и делает процесс обучения более целенаправленным.

## Необходимые библиотеки
   Основные библиотеки перечислены в файле requirements.txt

1. **streamlit**:  
   Используется для создания веб-интерфейса приложения. Позволяет быстро разрабатывать интерактивные веб-приложения с минимальными усилиями, предоставляя готовые компоненты для визуализации данных, ввода текста и обратной связи.

2. **langchain**:  
   Библиотека для работы с текстовыми цепочками, которая упрощает создание многошаговых запросов к моделям и управление контекстом. В проекте используется для обработки запросов пользователей и взаимодействия с моделью OpenAI, а также для создания цепочек обработки данных.

3. **openai**:  
   Официальная библиотека для работы с OpenAI API. Используется для отправки запросов к модели GPT-4 и получения ответов на вопросы, задаваемые пользователями.

4. **faiss-cpu**:  
   Инструмент для работы с векторными представлениями данных, который используется для поиска ближайших соседей в больших коллекциях векторов. В проекте применен для поиска похожих текстов и семантического сравнения вопросов пользователей с базой данных.

5. **numpy**:  
   Библиотека для работы с массивами и выполнения математических операций. В проекте используется для обработки числовых данных, необходимых для работы с векторными представлениями и другими расчетами.

6. **sqlite3**:  
   Библиотека для взаимодействия с базой данных SQLite, в которой хранятся векторные представления вопросов и истории взаимодействий. Она обеспечивает быстрое и легкое хранение данных без необходимости настройки серверной СУБД.

7. **requests**:  
   Библиотека для отправки HTTP-запросов. В проекте используется для взаимодействия с Telegram API, позволяя отправлять обратную связь от пользователей прямо в канал разработчика.

8. **pandas**:  
   Библиотека для работы с табличными данными. Используется для обработки и анализа данных, связанных с обучающими материалами и запросами пользователей.

9. **tqdm**:  
   Применяется для создания индикаторов прогресса. Используется при обработке данных и для удобного отслеживания этапов выполнения в процессе деплоя и обучения.

10. **python-dotenv**:  
    Библиотека для работы с переменными окружения, загружаемыми из файлов `.env`. Применяется для конфиденциального хранения ключей API, ссылок на базы данных и других чувствительных данных, используемых приложением.

11. **SQLAlchemy**:  
    ORM-библиотека для взаимодействия с базами данных. В проекте используется для более удобного управления записями в базе данных SQLite.

12. **tiktoken**:  
    Библиотека для токенизации текста в соответствии с требованиями моделей OpenAI. Она помогает оценить длину текстов и управлять лимитами токенов, что важно при работе с GPT-моделями.

13. **dotenv**:  
    Используется для управления переменными окружения, загружаемыми из файлов `.env`. Это позволяет хранить конфиденциальные данные, такие как API-ключи и пути к базам данных, вне кода приложения.

14. **pydantic**:  
    Библиотека для валидации данных. Применяется в проекте для проверки корректности вводимых пользователем данных и взаимодействия с API.

## Технические особенности

1. **Сбор и обработка данных**:  
   Приложение собирает вопросы от пользователей в режиме реального времени через веб-интерфейс на основе Streamlit. Пользовательский запрос отправляется на сервер, где он обрабатывается с помощью цепочек Langchain. В процессе обработки запрос анализируется и отправляется в OpenAI API для получения текста ответа.

2. **Техники промптинга**:  
   Для взаимодействия с моделью OpenAI используются специально подготовленные шаблоны промптов, которые помогают уточнить контекст вопроса. Промпты настроены для генерации ответов, которые максимально соответствуют тематике курса для начинающих менеджеров WB, учитывая специфическую терминологию и структуру данных.

3. **Используемые модели**:  
   В основе приложения лежит языковая модель OpenAI `gpt-4o-mini`, которая адаптирована для работы с вопросами пользователей. Модель обучена на большом корпусе данных и способна предоставлять развернутые и точные ответы на запросы, связанные с менеджментом и обучающими курсами.

4. **Хранение данных**:  
   Векторы эмбеддингов и текстовые данные (вопросы и ответы) сохраняются в базе данных SQLite. Это позволяет эффективно управлять информацией, хранить историю взаимодействий и ускорять процесс поиска схожих запросов.

5. **Использование FAISS**:  
   Для поиска похожих вопросов и запросов используется FAISS (Facebook AI Similarity Search), библиотека для поиска ближайших соседей среди векторов. Этот механизм позволяет быстрее находить ответы на часто задаваемые вопросы и обрабатывать их на основе векторных представлений.

6. **Векторные представления**:  
   Запросы пользователей преобразуются в векторные представления с помощью эмбеддингов, что позволяет системе искать схожие вопросы и улучшать качество ответов. Векторизация текста выполняется с использованием модели OpenAI, а затем результат сохраняется в базе данных и используется для последующих запросов.

7. **История чата**:  
   Все взаимодействия пользователей с чатом сохраняются в сессии, что дает возможность пользователям видеть предыдущие вопросы и ответы. Это помогает отслеживать прогресс и возвращаться к уже обсужденным темам.

8. **Отправка уведомлений**:  
   В приложении настроена интеграция с Telegram API. Пользователи могут отправлять отзывы и получать уведомления о новых материалах или изменениях в курсе прямо через Telegram. Уведомления также используются для передачи обратной связи о работе чат-ассистента разработчику.

9. **Обратная связь и улучшение**:  
   В приложении реализована система обратной связи, где пользователи могут оценивать качество полученных ответов. Эти данные собираются и используются для дальнейшего улучшения работы приложения, подстраивая ответы под конкретные запросы и сценарии пользователей.

10. **Масштабируемость и деплой**:  
    Приложение развернуто в Docker-контейнере на удаленном сервере AWS EC2. Это обеспечивает легкость развертывания и обновления приложения, а также гибкость масштабирования под нагрузку, если количество пользователей увеличится. Все зависимости и переменные окружения управляются через `.env` файл.

## Деплой

Приложение развернуто на удаленном сервере AWS EC2, что было выбрано из-за высокой доступности, надежности и масштабируемости платформы. AWS EC2 предоставляет гибкость в выборе ресурсов, что позволяет адаптировать конфигурацию сервера под текущие требования приложения.

### Причины выбора AWS EC2:

1. **Масштабируемость**: AWS EC2 позволяет легко увеличивать или уменьшать ресурсы в зависимости от нагрузки, что важно для приложений с переменным трафиком.

2. **Надежность**: AWS предлагает высокий уровень надежности и доступности благодаря распределенной инфраструктуре.

3. **Интеграция с другими сервисами**: AWS EC2 легко интегрируется с другими сервисами AWS, такими как RDS для управления базами данных и S3 для хранения файлов.

4. **Безопасность**: AWS предоставляет широкий спектр инструментов для обеспечения безопасности данных и доступа.

### Процесс развертывания:

1. **Проверка наличия предыдущего контейнера**: Перед запуском нового контейнера скрипт проверяет, существует ли уже контейнер с указанным именем. Если он существует, контейнер останавливается и удаляется.

2. **Загрузка нового образа**: Новый образ приложения загружается из Docker Hub, что позволяет автоматически обновлять приложение до последней версии.

3. **Запуск нового контейнера**: Новый контейнер запускается с указанием необходимых переменных окружения и монтированием файла базы данных, что обеспечивает его доступность для приложения.

### Особенности взаимодействия с пользователями:

Пользователи взаимодействуют с приложением через веб-интерфейс, разработанный на Streamlit. Это позволяет легко задавать вопросы и получать ответы в режиме реального времени. Обратная связь от пользователей также интегрирована в приложение, что позволяет собирать данные о качестве ответов и улучшать функциональность чат-ассистента.
