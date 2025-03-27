from flask import Flask, render_template,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

# Подключение к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

# Создание модели
class InputData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_input = db.Column(JSONB)

# Создание таблиц
with app.app_context():
    db.create_all()


# Создание обработчика запросов
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            # Получаем список введенных данных
            fields = request.form.getlist('name[]')
            print(fields)
            # Сохраняем данные
            new_entry = InputData(data_input=fields)
            db.session.add(new_entry)
            db.session.commit()
            return jsonify({"message": "Данные сохранены"})
        except Exception as e:
            print(str(e))
            # Откат если ошибка
            db.session.rollback()
            return jsonify({"error": "Произошла ошибка"})
    else:
        return render_template("index.html")


@app.route('/view', methods=['GET'])
def view_data():
    try:
        # Получаем данные и выводим их
        entries = InputData.query.all()
        return render_template('view_data.html', entries=entries)
    except Exception as e:
        print(str(e))
        return "Произошла ошибка"

if __name__ == '__main__':
    app.run(debug=True) 