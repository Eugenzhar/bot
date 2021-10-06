import datetime
import json
import http
from logging import getLogger

import xmltodict
import requests


logger = getLogger(__name__)


def get_rates():
    # url запроса
    get_curl = "https://cbr.ru/scripts/XML_daily.asp?"
    # формат даты : д/м/г
    date_format="%d/%m/%Y"

    # дата запроса
    today = datetime.datetime.today()
    params = {
        "date_req": today.strftime(date_format),
    }
    #r = requests.get(get_curl, params=params)
    r = requests.get(get_curl)
    resp = r.text
    #print(resp)


    data = xmltodict.parse(resp)

    #print(json.dumps(data, indent=2))
    # Ищем по @ID
    section_id = 'R01235'


    for item in data['ValCurs']['Valute']:
        if item['@ID'] == section_id:
            currency_name = item['CharCode']
            currency_rate = item['Value']
            print("1 ", currency_name, " = ", currency_rate, " рубля")
            break

if __name__ == '__main__':
    get_rates()
