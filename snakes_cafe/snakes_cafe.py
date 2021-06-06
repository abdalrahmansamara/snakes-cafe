print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
menu = {
    'wings':0,
    'cookies':0,
    'spring_rolls':0,
    'salmon':0,
    'steak':0,
    'meat_tornado':0,
    'a_literal_garden':0,
    'ice_cream':0,
    'cake':0,
    'pie':0,
    'coffee':0,
    'tea':0,
    'unicorn_tears':0
}

while 5<6:
    order = input('>')
    if (order == "quit"):
        break
    under_order = order.replace(" ", "_").lower()
    if (under_order not in menu):
        print('this is not on the menu')
    else:
        menu[under_order]+=1
        to_print = f'** {menu[under_order]} order of {order} have been added to your meal **'
        print(to_print)
