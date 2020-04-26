import urllib
from urllib import request
from DataBase import take_info
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# данные за конкретный день по указанной стране

@app.route('/<country_name>/<date>')
def country_date(country_name, date):
    information = take_info(country_name, date)
    return information














# данные по всем странам по указанной дате
@app.route('/total/{date}')
def total(date):
    return 'total in date'


# аггрегированные данные по указанной стране, вплодь до указанной даты. если дата не указана - до сегодняшнего дня
@app.route('/{country_name}?date=yyyy-MM-dd')
def name():
    return 'country name in date'


# аггрегированные данные по всем странам, вплодь до указанной даты. если дата не указана - до сегодняшнего дня
@app.route('/total?date=yyyy-MM-dd')
def total_date():
    return 'total in date'

#должен возвращать данные: {'service': <name of service>, 'debug': <current debug flag>, 'host': <name of host machine>}
@app.route('/')
def info():
    return "{'service': <name of service>, 'debug': <current debug flag>, 'host': <name of host machine>}"


if __name__ == "__main__":
    app.run(debug=True)
