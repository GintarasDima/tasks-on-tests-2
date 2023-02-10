#Напишите код программы на Python, которая будет в реальном времени
# (с максимально возможной скоростью)
# считывать текущую цену фьючерса XRP/USDT на бирже Binance.
# В случае, если цена упала на 1% от максимальной цены за последний час,
# программа должна вывести сообщение в консоль.
# При этом программа должна продолжать работать дальше, постоянно считывая актуальную цену.


import ccxt
import time
import sys

pair = 'XRP/USDT'

while True:
    try:
        binance = ccxt.binance()
        price = float(binance.fetch_ticker(pair)['bid'])
        print(price)
        time.sleep(10)
        sys.stdout.flush()
        if price < 0.3:
            print('Внимание! Цена фьючерса XRP/USDT упала на 1% от максимальной цены за последний час. Сейчас стоит: ' + str(price))
            break
    except:
        print('Ошибка получения цены')
        time.sleep
