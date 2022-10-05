# program to buy Apple computers 

import pickle
import json
import os

# project operations 
from help import *
from show import *
from info import *
from buy import *
from bag import *
from remove import *
from bill import *

# Loading whole data
with open("mac.json", "r") as j_file:
    product_data = json.load(j_file)
    product_name = []
    for i in product_data:
        product_name.append(i["name"].lower())

   

print('\n\n===***===***===  Welcome to Macbook Store  ===***===***===\n')

while True:
    print()
    main_cmd = input('\nenter a command or type --help for help or exit to exit \n -->  ').lower().strip()
    print()
    if main_cmd == 'exit' or main_cmd == 'e':
        break
    
    elif main_cmd == 'help':
        show_help()
        continue
    
    elif main_cmd == 'show':
        show(product_data)
        
    elif main_cmd.startswith('info'):
        if main_cmd.lstrip('info').strip() in product_name:
            info_product_name = main_cmd.lstrip('info').strip()
            info(info_product_name, product_data)
        else:
            print('type correct name, use show command to see the products name')
            
    elif main_cmd.startswith('buy'):
        if main_cmd.lstrip('buy').strip() in product_name:
            buy_product_name = main_cmd.lstrip('buy').strip()
            buy(buy_product_name, product_data)
        else:
            print('type correct name, use show command to see the products name')
            
    elif main_cmd == 'bag':
        bag()
        
    elif main_cmd == 'rm':
        remove()
        
    elif main_cmd == 'bill':
        bill()
