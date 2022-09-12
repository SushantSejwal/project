# program to buy Apple computers 

import pickle
import json
import os

# Loading whole data
with open("mac.json", "r") as j_file:
    product_data = json.load(j_file)
    product_name = []
    for i in product_data:
        product_name.append(i["name"].lower())



def __help():
    print()
    print('   show                 : show you all the avialable products')
    print('   info product_name    : show information about the selected product name')
    print('   buy product_name     : buy the product')
    print('   bag                  : review your bag')
    print('   bill                 : see the amount to pay')
    print('   rm                   : remove a product from the bag')
    print('   exit                 : to exit the whole program')
    print()
        
        
def show(product_data):
    """show all the avialable apple products"""
    for name in product_data:
        print(f'  {name["name"]}')
    
    
def pr_info(name):
    '''show information about apple products'''
    name = name.title().replace('Macbook', 'MacBook')
    print()
    print(f"Product : {name}")
    
    for product in product_data:
        if product["name"] == name:
            if len(product["processor"]) > 1:
                print('Processor : ') 
                print(f'           base - {product["processor"][0][0]}')
                print(f'           top - {product["processor"][-1][0]}')
            else:
                print(f'Processor : {product["processor"][0][0]}')
            
            # RAM
            print('RAM: ') 
                # base
            if product["ram"][0][0] > 999: print(f'    base - {product["ram"][0][0] / 1000}TB')
            else: print(f'    base - {product["ram"][0][0]}GB')
                # top
            if product["ram"][-1][0] > 999: print(f'    top - {product["ram"][-1][0] / 1000}TB')
            else: print(f'    top - {product["ram"][-1][0]}GB')
            
            # Storage
            print('Storage: ') 
                # base
            if product["storage"][0][0] > 999: print(f'        base - {product["storage"][0][0] / 1000}TB')
            else: print(f'        base - {product["storage"][0][0]}GB')
                # top
            if product["storage"][-1][0] > 999: print(f'        top - {product["storage"][-1][0] / 1000}TB')
            else: print(f'        top - {product["storage"][-1][0]}GB')
            
            print(f'Base Price : ${product["price"]}')
            break
         
            
def buy(name):
    '''buy apple products'''
    name = name.title().replace('Macbook', 'MacBook')

    brought_product_file = open('bag.sushant', 'ab+')
    file_data = []
    file_data.append(name)
    print()
    print(f"Product : {name}")
    for product in product_data:
        if product["name"] == name:
            print(f'  Processor : {product["processor"][0][0]}')
            
            if product["storage"][0][0] > 999: print(f'  RAM : {product["ram"][0][0] / 1000}TB')
            else: print(f'  RAM : {product["ram"][0][0]}GB')
            
            if product["storage"][0][0] > 999: print(f'  Storage : {product["storage"][0][0] / 1000}TB')
            else: print(f'  Storage : {product["storage"][0][0]}GB')
            
            print(f'  Base Price : ${product["price"]}')
            
            mac_price = product["price"]
            deafult_file_data = [product["processor"][0][0], product["ram"][0][0], product["storage"][0][0], mac_price]
            break
        
    while True:
        customize = input('wanna customize your mac [Yes/no] or enter [exit] to leave\n ->  ').lower().strip()
        if customize =='exit' or customize == 'e' :
            print('order hasn\'t placed')
            brought_product_file.close()
            break
        elif customize == 'yes' or customize == 'y' or customize == '':
            
            # Processor
            print()
            print('which processor is right for you ?')
            for product in product_data:
                if product["name"] == name:
                    processor_dict = {}
                    
                    for count, processor in enumerate(product["processor"]):
                        if processor[-1] == 0:
                            print(f'   {count} for : {processor[0]} + ${processor[-1]} (Deafault)')
                            processor_dict[count] = [processor[0], processor[-1]]
                        else:
                            print(f'   {count} for : {processor[0]} + ${processor[-1]}')
                            processor_dict[count] = [processor[0], processor[-1]]
                        
                    while True:
                        processor_chioce = input('  -->  ').strip()
                        
                        # choosing default processor
                        if processor_chioce == '':
                            for i in processor_dict:
                                if processor_dict[i][-1] == 0:
                                    file_data.append(processor_dict[i][0])
                                    mac_price += processor_dict[i][-1]
                                    print(f'processor choose : {processor_dict[i][0]} ')
                                    print(f'total price : ${mac_price}')
                                    break 
                            break     
                        # choosing processor other then default
                        elif processor_chioce.isdigit():
                            processor_chioce = int(processor_chioce)
                            file_data.append(processor_dict[processor_chioce][0])
                            mac_price += processor_dict[processor_chioce][-1]
                            print(f'processor choose : {processor_dict[processor_chioce][0]}')
                            print(f'total price : ${mac_price}')
                            break
                        
                        else:
                            print('only enter number or press enter to choose deafult')
                            continue
                    
                    break

            # RAM
            print()
            print('which amount of RAM is right for you ?')
            for product in product_data:
                if product["name"] == name:
                    ram_dict = {}
                    
                    for count, ram in enumerate(product["ram"]):
                        if ram[-1] == 0:
                            if ram[0] < 1000:
                                print(f'   {count} for : {ram[0]}GB + ${ram[-1]} (Deafault)')
                                ram_dict[count] = [ram[0], ram[-1]]
                            else:
                                print(f'   {count} for : {ram[0] / 1000}TB + ${ram[-1]} (Deafault)')
                                ram_dict[count] = [ram[0], ram[-1]]
                        else:
                            if ram[0] < 1000:
                                print(f'   {count} for : {ram[0]}GB + ${ram[-1]}')
                                ram_dict[count] = [ram[0], ram[-1]]
                            else:
                                print(f'   {count} for : {ram[0] / 1000}TB + ${ram[-1]}')
                                ram_dict[count] = [ram[0], ram[-1]]
                        
                        
                    while True:
                        ram_chioce = input('  -->  ').strip()
                        
                        # choosing default ram
                        if ram_chioce == '':
                            for i in ram_dict:
                                if ram_dict[i][-1] == 0:
                                    file_data.append(ram_dict[i][0])
                                    mac_price += ram_dict[i][-1]
                                    if ram_dict[i][0] < 1000: print(f'RAM choose : {ram_dict[i][0]}GB ')
                                    else:  print(f'RAM choose : {ram_dict[i][0] / 1000}TB ')
                                    print(f'total price : ${mac_price}')
                                    break
                            break     
                        # choosing ram other then default
                        elif ram_chioce.isdigit():
                            ram_chioce = int(ram_chioce)
                            file_data.append(ram_dict[ram_chioce][0])
                            mac_price += ram_dict[ram_chioce][-1]
                            if ram_dict[ram_chioce][0] < 1000: print(f'RAM choose : {ram_dict[ram_chioce][0]}GB')
                            else:  print(f'RAM choose : {ram_dict[ram_chioce][0] / 1000}TB')
                            print(f'total price : ${mac_price}')
                            break
                        
                        else:
                            print('only enter number or press enter to choose deafult')
                            continue
                    
                    break

            # Storage
            print()
            print('how much storage is right for you ?')
            for product in product_data:
                if product["name"] == name:
                    storage_dict = {}
                    
                    for count, storage in enumerate(product["storage"]):
                        if storage[-1] == 0:
                            if storage[0] < 1000:
                                print(f'   {count} for : {storage[0]}GB + ${storage[-1]} (Deafault)')
                                storage_dict[count] = [storage[0], storage[-1]]
                            else:
                                print(f'   {count} for : {storage[0] / 1000}TB + ${storage[-1]} (Deafault)')
                                storage_dict[count] = [storage[0], storage[-1]]
                        else:
                            if storage[0] < 1000:
                                print(f'   {count} for : {storage[0]}GB + ${storage[-1]}')
                                storage_dict[count] = [storage[0], storage[-1]]
                            else:
                                print(f'   {count} for : {storage[0] / 1000}TB + ${storage[-1]}')
                                storage_dict[count] = [storage[0], storage[-1]]
                        
                    while True:
                        storage_chioce = input('  -->  ').strip()
                        
                        # choosing default storage
                        if storage_chioce == '':
                            for i in storage_dict:
                                if storage_dict[i][-1] == 0:
                                    file_data.append(storage_dict[i][0])
                                    mac_price += storage_dict[i][-1]
                                    if storage_dict[i][0] < 1000:
                                        print(f'storage choose : {storage_dict[i][0]}GB ')
                                    else:
                                        print(f'storage choose : {storage_dict[i][0] / 1000}TB ')
                                    
                                    print(f'total price : ${mac_price}')
                                    break 
                            break     
                        # choosing storage other then default
                        elif storage_chioce.isdigit():
                            storage_chioce = int(storage_chioce)
                            file_data.append(storage_dict[storage_chioce][0])
                            mac_price += storage_dict[storage_chioce][-1]
                            if storage_dict[storage_chioce][0] < 1000:
                                print(f'storage choose : {storage_dict[storage_chioce][0]}GB')
                            else:
                                print(f'storage choose : {storage_dict[storage_chioce][0] / 1000}TB')
                            
                            print(f'total price : ${mac_price}')
                            break
                        
                        else:
                            print('only enter number or press enter to choose deafult')
                            continue
                    
                    break
                
            file_data.append(mac_price)
            pickle.dump(file_data, brought_product_file)
            print('order placed, check you bag to see the product')
            brought_product_file.close()
            break
        
        elif customize == 'no' or customize == 'n':
            pickle.dump(deafult_file_data, brought_product_file)
            print('order placed, check you bag to see the product')
            brought_product_file.close()
            break
        else:
            print()
            print('choose yes or no or exit')
            print()


def bag():
    '''display all the products that are purchased'''
    order_no = 1
    if os.path.exists('bag.sushant'):
        with open('bag.sushant', 'rb') as bag_file:
            try:
                while True:
                    ordered_item = pickle.load(bag_file)
                    print()
                    print(f'product {order_no}')
                    print(f'        name: {ordered_item[0]}')
                    print(f'        processor: {ordered_item[1]}')
                    
                    if ordered_item[2] > 999: print(f'        ram: {ordered_item[2] / 1000}TB')
                    else: print(f'        ram: {ordered_item[2]}GB')
                    
                    if ordered_item[3] > 999: print(f'        storage: {ordered_item[3] / 1000}TB')
                    else: print(f'        storage: {ordered_item[3]}GB')
                    
                    print(f'        price: ${ordered_item[4]}')
                    order_no += 1
            except Exception:
                pass
    else:
        print()
        print('your bag is empty buy, first buy some products and they will show here')           
        print()


def remove():
    '''remove product from bag'''
    order_no = 1
    if os.path.exists('bag.sushant'):
        
        data_exist = False
        with open('bag.sushant', 'rb') as bag_file:
            while True:
                try:
                    rec = pickle.load(bag_file)
                    if rec:
                        data_exist = True
                except Exception:
                    break
        if data_exist:           
            with open('bag.sushant', 'rb') as bag_file:
                while True:
                    try:
                        ordered_item = pickle.load(bag_file)
                        print()
                        print(f'product {order_no}')
                        print(f'        name: {ordered_item[0]}')
                        print(f'        processor: {ordered_item[1]}')

                        if ordered_item[2] > 999: print(f'        ram: {ordered_item[2] / 1000}TB')
                        else: print(f'        ram: {ordered_item[2]}GB')

                        if ordered_item[3] > 999: print(f'        storage: {ordered_item[3] / 1000}TB')
                        else: print(f'        storage: {ordered_item[3]}GB')

                        print(f'        price: ${ordered_item[4]}')
                        order_no += 1
                    except Exception:
                        break
                    
            product_nums = list(range(1, order_no))
            product_nums_str = '['

            for i in product_nums:
                if i == product_nums[-1]: product_nums_str += f'{str(i)}'
                else: product_nums_str += f'{str(i)}/'

            product_nums_str += ']'

            while True :
                which_to_del = input(f'enter the prodcut number to del {product_nums_str}\n   -->  ').strip()
                if which_to_del.isdigit():
                    which_to_del = int(which_to_del)
                    break
                else:
                    print('enter number only\n')
                    continue
                
                
            with open('bag.sushant', 'rb') as bag_file:
                temp_num = 1
                not_to_delete = []
                while True:
                    try:
                        ordered_item = pickle.load(bag_file)
                        if temp_num != which_to_del: not_to_delete.append(ordered_item)
                        temp_num += 1

                    except Exception:
                            break    
            # to delete all data from file  
            with open('bag.sushant', 'wb') as bag_file:
                pass

            # to enter new data to file after deleting the selecting item
            with open('bag.sushant', 'ab') as bag_file:
                for i in not_to_delete:
                    pickle.dump(i, bag_file)
        
        # this will run when file will be empty
        else:
            print()
            print('your bag is empty buy, buy some products and they will show here')           
            print()
    
    # this will run when file doesn't exit
    else:
        print()
        print('your bag is empty buy, buy some products and they will show here')           
        print()


def bill():
    data_exist = False
    bill = 0
    
    with open('bag.sushant', 'rb') as bill_file:
        while True:
            try:
                rec = pickle.load(bill_file)
                if rec:
                    data_exist = True
            except Exception:
                break
            
    if data_exist: 
        with open('bag.sushant', 'rb') as bill_file:
            while True:
                try:
                    rec = pickle.load(bill_file)
                    bill += rec[-1]
                except Exception:
                    break
        print(f'the total amount you have to pay is ${bill}')
    else:
        print()
        print('your bag is empty buy, buy some products and they will show here')           
        print()        

print('===***===***===  Welcome to Macbook Store  ===***===***===\n')

while True:
    main_cmd = input('\nenter a command or type --help for help or exit to exit \n -->  ').lower().strip()
    if main_cmd == 'exit' or main_cmd == 'e':
        break
    
    elif main_cmd == '--help':
        __help()
        continue
    
    elif main_cmd == 'show':
        show(product_data)
        
    elif main_cmd.startswith('info'):
        if main_cmd.lstrip('info ') in product_name:
            info_product_name = main_cmd.lstrip('info ')
            pr_info(info_product_name)
        else:
            print('type correct name, use show command to see the products name')
            
    elif main_cmd.startswith('buy'):
        if main_cmd.lstrip('buy ') in product_name:
            buy_product_name = main_cmd.lstrip('buy ')
            buy(buy_product_name)
        else:
            print('type correct name, use show command to see the products name')
            
    elif main_cmd == 'bag':
        bag()
        
    elif main_cmd == 'rm':
        remove()
        
    elif main_cmd == 'bill':
        bill()
