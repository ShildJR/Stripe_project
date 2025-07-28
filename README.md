# Тестовое задание Ришат.

### Предварительные требования
- Python 3.8+
- Django 4.0+
- Stripe аккаунт (тестовый режим)


### Установка

```
git clone 
cd Stripe_project
```
# Создайте и активируйте виртуальное окружение
```
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
```
# Установите зависимости 
```
pip install -r requirements.txt
```
# Настройте переменные окружения:
### Создайте файл .env в корне проекта, добавьте:
```
SECRET_KEY=ваш-django-secret-key
STRIPE_PUBLIC_KEY=pk_test_ваш-ключ
STRIPE_SECRET_KEY=sk_test_ваш-ключ
SITE_URL=http://localhost:8000
```
# Примените миграции:
```
python manage.py migrate
```
# Создайте суперпользователя:

```
python manage.py createsuperuser
```
# Запустите сервер:

```
python manage.py runserver
```