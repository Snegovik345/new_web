from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1><a href="/info">Информация о сайте</a><a href="/rm">Рандомные факты</a><a href="/monetka">Бросок монетки</a> '

@app.route("/info")
def info():
    return '<h1>Сайт создан с целью рассказать людям о технологических зависимостях</h1><a href="/">На главную</a>'

@app.route("/rm")
def random_fact():
    listlist = ["Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.",
                "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.",
                "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов."]
    return f'<h1>Рандомный факт</h1><a href="/">На главную</a><p>{random.choice(listlist)}</p>'

@app.route("/monetka")
def monetka():
    moneylist = ["Орел", "Решка"]
    return f'<h1>Бросок Монетки</h1><a href="/">На главную</a><v>{random.choice(moneylist)}</v>'
app.run(debug=True)
