import pickle

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
                    bill += rec[-2]
                except Exception:
                    break
        print(f'the total amount you have to pay is ${bill}')
    else:
        print()
        print('your bag is empty')           
        print()     