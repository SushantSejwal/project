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
