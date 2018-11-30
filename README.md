# cryptobal

Display value of crypto-currency holdings.

## How to use the script

1) Fill the list file with name_of_the_cryto:your_amount as :

~~~
verge:1.404
cardano:357.009
ripple:141
aelf:60
iota:45
stratis:14.95025
binance-coin:14.48860028
eos:5.66533
ethereum-classic:5.01872
neo:1.47
ethereum:0.74152521
monero:0.457
dash:0.24
~~~

2) Run :

~~~
python3 cryptobal.py /path/of/your/file
~~~

## Sample

~~~
  Name       Price_usd        Quantity           Total
   XVG           0.007        1.404000            0.01
   ADA           0.039      357.009000           13.91
   XRP           0.360      141.000000           50.75
   ELF           0.128       60.000000            7.68
 MIOTA           0.287       45.000000           12.93
 STRAT           0.746       14.950250           11.16
   BNB           5.026       14.488600           72.82
   EOS           2.877        5.665330           16.30
   ETC           4.737        5.018720           23.78
   NEO           7.821        1.470000           11.50
   ETH         113.864        0.741525           84.43
   XMR          57.832        0.457000           26.43
  DASH          90.390        0.240000           21.69


                       Total price : $          353.40
~~~
