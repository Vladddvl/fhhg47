Требоется:
-Python 3
-PostgreSQL
-Git


1 Клонирование репозитория
В терминале прописываем команду git clone https://github.com/...

2 Нужно создать виртуальное окружение
python3 -m venv venv
source venv/bin/activate

3 Заупустить PostgreSQL
sudo -u postgres psql

4 Создать БД
CREATE DATABASE app_db;

5 Создать пользователя и выдать ему соответствующее разрешение 
CREATE USER user_name WITH PASSWORD password;
GRANT ALL PRIVILEGES ON DATABASE app_db TO user_name;

6 Создать фаил .env
DATABASE_URL=postgresql://user_name:password@localhost/app_db

7 Запуск сервера и проверка работы
python app.py



