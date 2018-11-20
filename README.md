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
   XVG        0.006724        0.009441        0.009441
   ADA        0.046222       16.501735       16.501735
   XRP        0.447684       63.123484       63.123484
   ELF        0.135943        8.156592        8.156592
 MIOTA        0.307919       13.856370       13.856370
 STRAT        0.752835       11.255078       11.255078
   BNB        5.684394       82.358915       82.358915
   EOS        3.711299       21.025736       21.025736
   ETC        5.534133       27.774264       27.774264
   NEO        9.010394       13.245279       13.245279
   ETH      133.448756       98.955617       98.955617
   XMR       67.878208       31.020341       31.020341
  DASH      102.240280       24.537667       24.537667


                       Total price : $      411.820520
~~~
