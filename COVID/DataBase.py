import json
import urllib.request
from datetime import datetime

from peewee import *

db = SqliteDatabase('covid.db')


class Covid(Model):
    country = CharField()
    date = DateTimeField()
    confirmed = IntegerField()
    death = IntegerField()
    recovered = IntegerField()

    class Meta:
        database = db  # This model uses the "covid.db" database.


def download_file(url, local_file_name):
    # Download the file from `url` and save it locally under `file_name`:
    urllib.request.urlretrieve(url, local_file_name)


download_file(r'https://pomber.github.io/covid19/timeseries.json', 'timeseries.json')

with open('timeseries.json') as f:
    data_base = json.load(f)


def connect_to_db():
    db.connect()


def create_db():
    db.drop_tables([Covid], safe=True)
    db.create_tables([Covid], safe=True)


def writing_id_db():
    for country in data_base:
        for country_info in data_base[country]:

            if country_info['date'][6] == '-':
                new_string = country_info['date'][:5] + '0' + country_info['date'][5:]

                datetime_object = datetime.strptime(new_string, '%Y-%m-%d')

                info = Covid.create(country=country, date=datetime_object, confirmed=country_info['confirmed'],
                                    death=country_info['deaths'], recovered=country_info['recovered'])
                info.save()
                print(country_info)

def take_info(input_country, input_date):
    #
    # for country in data_base:
    #     if country == input_country:
    #         for country_info in data_base[country]:
    #             if input_date == country_info['date']:
    #                 return country_info
    a = Covid.select().where(Covid.country == input_country)



take_info('Angola', '2020-4-16')
