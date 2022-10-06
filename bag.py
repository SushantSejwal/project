import os
import pickle 

def bag():
    '''display all the products that are add for purchase'''
    order_no = 1
    if os.path.exists('bag.sushant'):
        with open('bag.sushant', 'rb') as bag_file:
            try:
                while True:
                    
                    ordered_item = pickle.load(bag_file)
                    if ordered_item[-1] == "display":
                        print()
                        print(f'product {order_no}')
                        print(f'        name: {ordered_item[0]}')
                        print(f'        glass: {ordered_item[1]}')
                        print(f'        stand: {ordered_item[2]}')
                        print(f'        price: {ordered_item[3]}')
                        order_no += 1

                    else:
                        print()
                        print(f'product {order_no}')
                        print(f'        name: {ordered_item[0]}')
                        print(f'        processor: {ordered_item[1]}')
                        print(f'        ram: {ordered_item[2]}GB')

                        if ordered_item[3] > 999: print(f'        storage: {ordered_item[3] / 1000}TB')
                        else: print(f'        storage: {ordered_item[3]}GB')

                        print(f'        price: ${ordered_item[4]}')
                        order_no += 1

            except Exception:
                pass
    else:
        print()
        print('your bag is empty buy')           
        print()
