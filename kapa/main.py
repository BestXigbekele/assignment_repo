cart = {}

def add_to_cart(item_name,price,*args,**kwargs):
    if item_name in cart:
        print('ITEM ALREADY EXIST IN CART')
        item_price = price
        for discount in args:
            item_price -= item_price * (discount/100)
        cart[item_name]["item_price"] += item_price
        return

    item_price = price
    for discount in args:
        item_price -= item_price * (discount/100)

    cart[item_name] = {
'item_price': round(item_price,2),
'details':kwargs
    }





def index():
    print()
    print("____CART SUMMARY____")
    print()
    total_price = 0
    for item,value in cart.items():
        print(f'{item} - price : ${value['item_price']} ,detail : {value['details']}')
        total_price += value['item_price']
       

while True:
    item_name = input('Enter item name (or "done" to finish):')
    if item_name.lower() == 'done':
        break
    price = float(input('Enter item price:'))
    discounts = input("Discounts (comma-separated, e.g., 10,20): ")
    discounts = [float(d) for d in discounts.split(",")] if discounts else []
    
    details={}
    while True:
        print()
        print("____ADD DETAILS____")
        print()
        details_type = input('Enter item details type (or "done" to finish):')
        if details_type.lower() == 'done':
            break
        details_value = input('Enter item details value:')
        details[details_type] = details_value
    add_to_cart(item_name,price,*discounts,**details)


index()

    
