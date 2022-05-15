def welcomeMsg():
    print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
""")


def menuItems():
    print("""
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
""")


def orderMsg():
    print("""
***********************************
** What would you like to order? **
***********************************
    """)


def orderedMenu():
    menulist = {
        "Wings": 0,
        "Cookies": 0,
        "Spring Rolls": 0,
        "Salmon": 0,
        "Steak": 0,
        "Meat Tornado": 0,
        "A Literal Garden": 0,
        "Ice Cream": 0,
        "Cake": 0,
        "Pie": 0,
        "Coffee": 0,
        "Tea": 0,
        "Unicorn Tears": 0
    }
    activeorder = True

    while activeorder:
        user_order = input('> ')

        if user_order in menulist:
            menulist[user_order] += 1

            if menulist[user_order] == 1:
                print('')
                print(f'** {menulist[user_order]} order of {user_order} has been added to your meal **')
                print('')
            elif menulist[user_order] > 1:
                print('')
                print(f'** {menulist[user_order]} orders of {user_order} have been added to your meal **')
                print('')
        elif user_order == 'quit':
            exit()

        else:
            print('That item does not exist')


if __name__ == "__main__":
    welcomeMsg()
    menuItems()
    orderMsg()
    orderedMenu()
