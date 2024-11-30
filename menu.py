#Whole unaltered menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}
'''
'dict'=dictionary elements
'choice'=user input
no suffix = expanded dictionary from that point
'ex' variables are used only when an item has more than 1 option, example 'Cheesecake': {'New York', 'Strawberry'}
'''
#external variables
total_price=0.0
recipt=(f'Item name       | Price  | Quantity\n----------------|--------|----------\n')
destiny=True
#Beginning of loop
while destiny==True:
#Menu list Variable
    menu_dict={}
    i=1
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_dict[i] = key
        i += 1
#User Menu Choice
    while True:
        cat_choice=(input("Choose Menu :"))
        if cat_choice.isdigit():
            cat_choice=int(cat_choice)
            break
        else:
            print(f'You did not answer correctly, please try again.')
    cat=menu_dict[cat_choice]
    print(f'You chose: {cat}')
#User Menu Category Choice
    cat_items=menu[cat]
    print(cat_items)
#Order list Variable
    order_dict={}
    i=1
    for key in cat_items.keys():
        print(f"{i}: {key}")
        order_dict[i] = key
        i += 1
#User Order
    while True:
        order_choice=input('Which item would you like to order?: ')
        if order_choice.isdigit():
            order_choice=int(order_choice)
            break
        else:
            print(f'You did not answer correctly, please try again.')
    order=order_dict[order_choice]
    order_items=menu[cat][order]
    print(f'You chose: {order}')
#User Order 'ex' variables
    ex_placeholder=order
    if type(order_items)!=float:
        ex_order_dict={}
        i=1
        for key in order_items.keys():
            print(f'{i}: {key}')
            ex_order_dict[i] = key
            i +=1
        while True:
            ex_order_choice=input('What type would you like to order?: ')
            if ex_order_choice.isdigit():
                ex_order_choice=int(ex_order_choice)
                break
            else:
                print(f'You did not answer correctly, please try again.')
        ex_order=ex_order_dict[ex_order_choice]
        order_items=menu[cat][order][ex_order]
        print(f'You chose: {ex_order}')
        ex_placeholder=order
        order=ex_order
#Quantity of item ordered
    if ex_placeholder == order:
        while True:
            quantity=input(f'How many \'{order}\'s would you like to order?: ')
            if quantity.isdigit():
                quantity=int(quantity)
                break
            else:
                print(f'You did not answer correctly, please try again.')
        print(f'You ordered {quantity} \'{order}\'s!')
#Quantity of item order if 'ex' variable
    else:
        while True:
            quantity=input(f'How many \'{order} {ex_placeholder}\'s would you like?: ')
            if quantity.isdigit():
                quantity=int(quantity)
                break
            else:
                print(f'You did not answer correctly, please try again.')
        print(f'You ordered {quantity} \'{order} {ex_placeholder}\'s!')
#Recipt Dictionary
    if ex_placeholder == order:
        recipt=(recipt+f'{order} - ${order_items} - {quantity}\n')
    else:
        recipt=(recipt+f'{order} {ex_placeholder} - ${order_items} - {quantity}\n')
    order_items=quantity*order_items
#Order Price
    price=(order_items)
    total_price=total_price+price
    print(f'Total cost: ${round(total_price, 2)}')
#Loop Breaker
    while True:
        breaker=input('Would you like to continue ordering? YES(y) NO(n): ')
        if breaker == 'n':
            destiny=False
            print('Thank you for your order!')
            print("This is what we are preparing for you.\n")
            break
        elif breaker =='y':
            break
        else:
            print('Try again: ')
#End of loop
print (f'{recipt}Total: ${round(total_price, 2)}')