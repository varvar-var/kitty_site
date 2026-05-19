# kitty_site 🌐

Сайт для приюта котиков.

## ✨ Возможности
- Модель котиков
- Поиск и фильтрация
- Адаптивный дизайн Bootstrap

## 🧰 Стек технологий
- Python 3.9
- Django 2.0
- SQLite3

## 🔧 Установка и запуск

### Требования
- Python 3.9
- pip

### Локальный запуск
1. Клонируйте репозиторий:
   ```bash
   git clone git@github.com:varvar-var/kitty_site.git
   cd kitty_site
   ```

2. Создайте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   . venv/Scripts/activate     # Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Создайте файл `.env`:
   ```
   SECRET_KEY=ваш_секретный_ключ
   DEBUG=True
   DB_NAME=db.sqlite3
   ```

5. Выполните миграции:
   ```bash
   python manage.py migrate
   ```

6. Создайте суперпользователя:
   ```bash
   python manage.py createsuperuser
   ```

7. Запустите сервер:
   ```bash
   python manage.py runserver
   ```
   Откройте http://127.0.0.1:8000
