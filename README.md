# Сайт "Продуктовый помощник Foodgram"
![example workflow](https://github.com/Seryojka-dev/foodgram-project-react/actions/workflows/main.yml/badge.svg)

На этом сайте пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.
## Установка локально
1. Склонируйте репозиторий:
    ```
    git clone git@github.com:Seryojka-dev/foodgram-project-react.git
    ```


2. Создайте виртуальное окружение:
    ```
    cd foodgram-project-react
    ```
    ```
    python -m venv venv
    ```
3. Активируйте виртуальное окружение:  
    * Для Windows:
        ```
        source venv\scripts\activate
        ```
        или

    * Для Linux/Mac:
        ```
        sorce venv/bin/activate
        ```
4. Установите зависимости:
    ```
    cd backend/
    ```
    ```
    python -m pip install -r requirements.txt
    ```
5. Cоздайте файл `.env` в директории `/infra/` с содержанием:

    ```
    SECRET_KEY=секретный ключ django
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    DB_HOST=db
    DB_PORT=5432
    ```

## Запуск проекта в Docker контейнере
* Установите и запустите Docker.
* Запустите файл docker compose (находится в директории `/infra/`):
    ```bash
    docker-compose up -d --build
    ```  
* После сборки появляются 3 контейнера: **db**, **backend**, **nginx**

* Примените миграции:
    ```bash
    docker-compose exec backend python manage.py makemigrations
    ```
    ```bash
    docker-compose exec backend python manage.py migrate
    ```
* Загрузите ингредиенты:
    ```bash
    docker-compose exec backend python manage.py ingredients_db
    ```
* Загрузите теги:
    ```bash
    docker-compose exec backend python manage.py tags_db
    ```
* Создайте суперпользователя:
    ```bash
    docker-compose exec backend python manage.py createsuperuser
    ```
* Соберите статику:
    ```bash
    docker-compose exec backend python manage.py collectstatic --noinput
    ```
## Action workflow:
В проекте Foodgram при пуше в ветку main код автоматически деплоится на сервер http://51.250.9.143/

## Админ-зона
Админ-зона: http:/51.250.9.143/admin/

```
Логин и пароль суперпользователя для проверки админ-зоны:
Email: admin@ya.ru
Password: admin
```

