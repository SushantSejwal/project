import pickle
def buy(name, product_data):
    '''buy apple products'''

    name = name.title()
    if 'Im' in name: name = name.replace('Im', 'iM') 
    if 'cb' in name: name =  name.replace('cb', 'cB') 
    if 'Mi' in name: name =  name.replace('Mi', 'mi') 
    if 'Xdr' in name: name =  name.replace('Xdr', 'XDR') 
    print(name)

    brought_product_file = open('bag.sushant', 'ab+')

    file_data = []
    file_data.append(name)

    print()

    print(f"Product : {name}")

    for product in product_data:
        if product["name"] == name:

            #<><><><><><><><><><><># buying code for display #<><><><><><><><><><><>#

            if product["type"] == "display":
                total_price = 0

                # choosing display glass
                while True:
                    display_dict = {}
                    print("Which display is right for you ")
                    for no, item in enumerate(product["display"]):
                        print(f"           {no} for : {item[0]} -> ${item[-1]}")
                        display_dict[no] = [item[0], item[-1]]
    
                    display_glass = input('  (default = 0)-->  ')

                    if display_glass == '':
                        print(f'  display glass choosed -> {display_dict[0][0]}')
                        file_data.append(display_dict[0][0])
                        total_price += display_dict[0][-1]
                        print()
                        break 

                    elif display_glass.isdigit():
                        display_glass = int(display_glass)

                        if display_glass in display_dict.keys():
                            print(f'  display glass choosed -> {display_dict[display_glass][0]}')
                            file_data.append(display_dict[display_glass][0])
                            total_price += display_dict[display_glass][-1]
                            print()
                            break
                        else:
                            print('choose only from displayed num')
                            print()
                            continue

                    else:
                        print('choose only int')
                        print()
                        continue

                
                # choosing display stand
                while True:
                    stand_dict = {}
                    print("Which stand is right for you ")
                    for no, item in enumerate(product["stand"]):
                        print(f"           {no} for : {item[0]} + ${item[-1]}")
                        stand_dict[no] = [item[0], item[-1]]
    
                    stand_no = input('  (default = 0)-->  ')

                    if stand_no == '':
                        print(f'  display stand choosed -> {stand_dict[0][0]}')
                        file_data.append(stand_dict[0][0])
                        total_price += stand_dict[0][-1]
                        print()
                        break 

                    elif stand_no.isdigit():
                        stand_no = int(stand_no)

                        if stand_no in stand_dict.keys():
                            print(f'  display stand choosed -> {stand_dict[stand_no][0]}')
                            file_data.append(stand_dict[stand_no][0])
                            total_price += stand_dict[stand_no][-1]
                            print()
                            break
                        else:
                            print('choose only from displayed num')
                            print()
                            continue

                    else:
                        print('choose only int')
                        print()
                        continue
                print(f'  total price = {total_price}')
                file_data.append(total_price)
                # print(product["type"])
                file_data.append(product["type"])
                pickle.dump(file_data, brought_product_file)
                brought_product_file.close()

                print('Order has been placed')
                break

            #<><><><><><><><><><><># buying code for notebooks and desktops #<><><><><><><><><><><>#

            else:
                print(f'  Processor : {product["processor"][0][0]}')
                print(f'  RAM : {product["ram"][0][0]}GB')
                print(f'  Storage : {product["storage"][0][0]}GB')
                print(f'  Base Price : ${product["price"]}')
                
                mac_price = product["price"]
                deafult_file_data = [product["name"],product["processor"][0][0], product["ram"][0][0], product["storage"][0][0], mac_price, product["type"]]
                

                # Customizing mac or not
                while True:
                    customize = input('\nwanna customize your mac [Yes/no] or type [exit/e] to leave\n ->  ').lower().strip()

                    if customize == 'no' or customize == 'n':
                        pickle.dump(deafult_file_data, brought_product_file)
                        print('Order has been placed')
                        brought_product_file.close()
                        break
                    
                    elif customize =='exit' or customize == 'e' :
                        print('order hasn\'t placed')
                        brought_product_file.close()
                        break

                    elif customize == 'yes' or customize == 'y' or customize == '':

                        # Choosing Processor
                        print()

                        if product["name"] == "Mac Studio":
                            print('\n **NOTE** choose M1 ultra to maximize RAM upto 128GB')
                            print(' **NOTE** choosing M1 ultra will make 32GB RAM option unavailable\n')

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
                                    processor_chioce = input('  (default = 0)-->  ').strip()

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
                                        if processor_chioce in processor_dict.keys():
                                            file_data.append(processor_dict[processor_chioce][0])
                                            mac_price += processor_dict[processor_chioce][-1]
                                            print(f'processor choose : {processor_dict[processor_chioce][0]}')
                                            print(f'total price : ${mac_price}')
                                            break
                                        else:
                                            print('choose only from displayed num')
                                            continue
                                    
                                    else:
                                        print('choose only int')
                                        continue
                                    
                                break
                            
                        # RAM
                        print()
                        print('which amount of RAM is right for you ?')
                        for product in product_data:
                            if product["name"] == name:
                                ram_dict = {}

                                for count, ram in enumerate(product["ram"]):

                                    # 32GB of RAM is only available with the M1 Pro and M1 max 
                                    if product["name"] == "Mac Studio" and "ultra" in file_data[1].lower():
                                        if ram[0] != 32:
                                            if ram[-1] == 0:
                                                print(f'   {count-1} for : {ram[0]}GB + ${ram[-1]} (Deafault)')
                                                ram_dict[count-1] = [ram[0], ram[-1]]
                                            else:
                                                print(f'   {count-1} for : {ram[0]}GB + ${ram[-1]}')
                                                ram_dict[count-1] = [ram[0], ram[-1]]

                                    # 128GB of RAM is only available with the M1 Ultra
                                    elif product["name"] == "Mac Studio" and "ultra" not in file_data[1].lower():
                                        if ram[0] != 128:
                                            if ram[-1] == 0:
                                                print(f'   {count} for : {ram[0]}GB + ${ram[-1]} (Deafault)')
                                                ram_dict[count] = [ram[0], ram[-1]]
                                            else:
                                                print(f'   {count} for : {ram[0]}GB + ${ram[-1]}')
                                                ram_dict[count] = [ram[0], ram[-1]]

                                    else: 
                                        if ram[-1] == 0:
                                            print(f'   {count} for : {ram[0]}GB + ${ram[-1]} (Deafault)')
                                            ram_dict[count] = [ram[0], ram[-1]]
                                        else:
                                            print(f'   {count} for : {ram[0]}GB + ${ram[-1]}')
                                            ram_dict[count] = [ram[0], ram[-1]]


                                while True:
                                    ram_chioce = input('  -->  ').strip()

                                    # choosing default ram
                                    if ram_chioce == '':
                                        for i in ram_dict:
                                            if ram_dict[i][-1] == 0:
                                                file_data.append(ram_dict[i][0])
                                                mac_price += ram_dict[i][-1]

                                                print(f'RAM choose : {ram_dict[i][0]} GB')
                                                print(f'total price : ${mac_price}')
                                                break
                                        break     

                                    # choosing ram other then default
                                    elif ram_chioce.isdigit():
                                        ram_chioce = int(ram_chioce)

                                        if ram_chioce in ram_dict.keys():
                                            file_data.append(ram_dict[ram_chioce][0])
                                            mac_price += ram_dict[ram_chioce][-1]
                                            print(f'RAM choose : {ram_dict[ram_chioce][0]}GB')
                                            print(f'total price : ${mac_price}')
                                            break
                                        else:
                                            print('choose only from displayed num')
                                            continue
                                    
                                    else:
                                        print('choose only int')
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
                                        print(f'   {count} for : {storage[0]}GB + ${storage[-1]} (Deafault)')
                                        storage_dict[count] = [storage[0], storage[-1]]
                                       
                                    else:
                                        if storage[0] < 1000:
                                            print(f'   {count} for : {storage[0]}GB + ${storage[-1]}')
                                            storage_dict[count] = [storage[0], storage[-1]]
                                        else:
                                            print(f'   {count} for : {storage[0] // 1000}TB + ${storage[-1]}')
                                            storage_dict[count] = [storage[0], storage[-1]]

                                while True:
                                    storage_chioce = input('  -->  ').strip()

                                    # choosing default storage
                                    if storage_chioce == '':
                                        for i in storage_dict:
                                            if storage_dict[i][-1] == 0:
                                                file_data.append(storage_dict[i][0])
                                                mac_price += storage_dict[i][-1]
                                                if storage_dict[i][0] < 1000: print(f'storage choose : {storage_dict[i][0]}GB ')
                                                else: print(f'storage choose : {storage_dict[i][0] / 1000}TB ')
                                                print(f'total price : ${mac_price}')
                                                break 
                                        break     
                                    # choosing storage other then default
                                    elif storage_chioce.isdigit():
                                        storage_chioce = int(storage_chioce)

                                        if storage_chioce in storage_dict.keys():
                                            file_data.append(storage_dict[storage_chioce][0])
                                            mac_price += storage_dict[storage_chioce][-1]
                                            if storage_dict[storage_chioce][0] < 1000: print(f'storage choose : {storage_dict[storage_chioce][0]}GB')
                                            else: print(f'storage choose : {storage_dict[storage_chioce][0] / 1000}TB')
                                            print(f'total price : ${mac_price}')
                                            break
                                        else:
                                            print('choose only from displayed num')
                                            continue
                                    
                                    else:
                                        print('choose only int')
                                        continue
                                    
                                break
                            
                        file_data.append(mac_price)
                        file_data.append(product["type"])
                        pickle.dump(file_data, brought_product_file)
                        print('order placed, check you bag to see the product')
                        brought_product_file.close()
                        break

                    else:
                        print()
                        print('choose yes or no or exit')
                        print()