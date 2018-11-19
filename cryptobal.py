#!/usr/bin/env python

import json
import requests
import sys


if __name__ == '__main__':

    input = (str(sys.argv[1]))
    
    with open(input) as fic:
        
        print ("Name","\t","Price_usd","\t","Quantity","\t\t","Total")
        
        count = 0   
        
        for line in fic:
            api = "https://api.coinmarketcap.com/v1/ticker/"
            url = (api + line.split(':')[0])
            quantity = (line.split(':')[1])
            r = requests.get(url)
            
            for coin in r.json():
                price_usd = (coin["price_usd"])
                count = (count) + (float(coin["price_usd"])*float(quantity))

                print(coin["symbol"],"\t",price_usd,"\t",float(coin["price_usd"])*float(quantity),"\t",(float(coin["price_usd"])*float(quantity)))
                
        print ("\nTotal : ",(count),"$")
