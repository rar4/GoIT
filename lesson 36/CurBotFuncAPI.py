import requests
import datetime


def nowerday():
    """
    returns today date
    """
    nowday = ''
    now = str(datetime.date.today())
    now = now.split('-')
    for i in now:
        nowday += i
    return nowday


def terminal_cur(name_of_cur):
    if name_of_cur in ['AUD', 'AZN', 'EUR', 'DZD', 'USD', 'GBP', 'CNY', 'KRW', 'AMD', 'JPY']:
        new_course = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='
                                  f'{name_of_cur}&date={nowerday()}&json').json()
        result = f'1 {name_of_cur} {new_course[0]["rate"]} is UAH'
        return result


print(terminal_cur('AUD'))
