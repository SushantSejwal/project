def show(product_data):
    """show all the avialable apple products"""

    print()

    alltype = set()
    for product in product_data:
        alltype.add(product["type"])

    for type in alltype:
        print(f'   in {type} ')
        no = 1
        for product in product_data:
            if product["type"] == type:
                print(f'      {no}. {product["name"]}')
                no += 1
        print()