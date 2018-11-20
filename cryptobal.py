#!/usr/bin/env python

import json
import requests
import sys


if __name__ == '__main__':

    input = (str(sys.argv[1]))

    with open(input) as fic:

        print ("%6s %15s %15s %15s" % ("Name","Price_usd","Quantity","Total"))

        count = 0

        for line in fic:
            api = "https://api.coinmarketcap.com/v1/ticker/"
            url = (api + line.split(':')[0])
            quantity = (line.split(':')[1])
            r = requests.get(url)

            for coin in r.json():
                price_usd = (coin["price_usd"])
                count = (count) + (float(coin["price_usd"])*float(quantity))
                print ("%6s %15f %15f %15f" % (coin["symbol"],float(price_usd),float(coin["price_usd"])*float(quantity),(float(coin["price_usd"])*float(quantity))))
        print ("\n")
        print ("%38s %15f" % ("Total price : $",float(count)))
