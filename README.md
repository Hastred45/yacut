# Укоротитель ссылок YaCut
Учебный проект в рамках курса Яндекс.Практикум

## Описание
Проект YaCut — это сервис укорачивания ссылок. Его ключевые возможности:
- генерация коротких ссылок (пользовательская или предлагаемая сервисом) 
и связь их с исходными длинными ссылками,
- переадресация на исходный адрес при обращении к коротким ссылкам.

Также всем желающим доступен API проекта.
<details><summary><h4> Примеры запросов к API </h4></summary>

- Генерация короткой ссылки: 
    ```SQL
    POST /api/id/
    {
      "url": "string",
      "custom_id": "string"
    }
    ```

- Получение оригинальной ссылки по указанному короткому идентификатору:
    ```SQL
    GET /api/id/{short_id}/
    ```

</details>

## Технологии
- Python 3.9
- Flask 2.0.2
- REST API
- SQLAlchemy
- HTML

## Установка и запуск проекта локально
<details><summary> Инструкции </summary>

- Клонировать репозиторий и перейти в него в командной строке:

    ```bash
    git clone https://github.com/Hastred45/yacut
    cd yacut
    ```

- Cоздать и активировать виртуальное окружение:

    * Если у вас Linux/MacOS
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

    * Если у вас windows
        ```bash
        python -m venv venv
        source venv/scripts/activate
        ```

- Установить необходимые зависимости:

    ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

- Не забудьте создать файл `.env` и наполнить его:

    ```
    DATABASE_URI=<dialect+driver://username:password@host:port/database>
    FLASK_APP=yacut
    FLASK_ENV=development
    SECRET_KEY=<Ваш_секретный_ключ>
    ```

- Создать файл базы данных и таблицы в нем:

    ```bash
    flask shell
    >>> from yacut import db
    >>> db.create_all()
    ```

- Запустить локально:

    ```bash
    flask run
    ```

</details>

## Автор
Сергей Осетров