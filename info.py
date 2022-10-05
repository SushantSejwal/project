    
def info(name, product_data):
    '''show information about apple products'''

    name = name.title()
    if 'Im' in name: name = name.replace('Im', 'iM') 
    if 'cb' in name: name =  name.replace('cb', 'cB') 
    if 'Mi' in name: name =  name.replace('Mi', 'mi') 
    if 'Xdr' in name: name =  name.replace('Xdr', 'XDR') 

    print()
    print(f"Product : {name}")
    
    for product in product_data:
        if product["name"] == name:

            if product["type"] == "display":
                print()
                print(f'  {product["about"]}')

                print(f'     Display : ')
                for no, glass in enumerate(product["display"]):
                    print(f'              {no+1}. {glass[0]}')

                print(f'     Stand : ')
                for no, stand in enumerate(product["stand"]):
                    print(f'            {no+1}. {stand[0]}')
                break

            else:
                print()
                if len(product["processor"]) > 1:
                    print('Processor : ') 
                    print(f'           base - {product["processor"][0][0]}')
                    print(f'           top - {product["processor"][-1][0]}')
                else:
                    print(f'Processor : {product["processor"][0][0]}')
                # RAM
                print('RAM: ') 
                print(f'    base - {product["ram"][0][0]}GB')
                print(f'    top - {product["ram"][-1][0]}GB')
                
                # Storage
                print('Storage: ')
                if product["storage"][0][0] > 999:   print(f'        base - {product["storage"][0][0] // 1000}TB')
                else:   print(f'        base - {product["storage"][0][0]}GB')

                if product["storage"][-1][0] > 999:  print(f'        top - {product["storage"][-1][0] // 1000}TB')
                else:   print(f'        top - {product["storage"][-1][0]}GB')

                # Display 
                if product["display-inbuild"]:
                    print(f'Display size : {product["display-size"]} inches')
                                
                # Price
                print(f'Base Price : ${product["price"]}')
                    
                print('In the box:')
                for box_item in product["in-box"]:
                    print(f'           {box_item}')

                break