
#    N.B.  -  I really wanted to create a real-world 'stock worth' calculator for a cafe.
#    So I have submitted two options for this task.  This one, called 'extended', is a robust,
#    'bug-proof' inventory/stock/price calculator for a cafe in the real world...!  I am hoping
#    I can add it to my portfolio later on during the course.  The other one, called 'simple', is
#    the one that hopefully fulfils everything that the task asked us to do.  I have uploaded both
#    of these to the dropbox folder.

#           Thank you for taking the time to have a look at both!





# I created some introductory print statements to introduce the program, including a for loop that
# would display the list of menu items to the user.
# I then created an empty 'menu' list, an empty 'stock' dictionary and an empty 'price' dictionary,
# ready for user input.


print()
print("Welcome to the Blagden Cafe!")
print()

menu = []
stock = {}
price = {}


# I then asked the user to input items for the menu, and used a while loop with an if statement
# to make sure the entries were formatted correctly:


print("Please enter items to be added to the cafe menu.  To stop entering items, please type 'stop'.\n")
      
while True:

    menu_item = input("Please enter an item to be added to the menu: ")
    menu_item_lower = menu_item.lower()
    if menu_item_lower != "stop":
        menu.append(menu_item.title())
    else:
        break


# I then displayed these back to the user:    

print()
print("Here is a list of the items on the menu:")
print()

for item in menu:
    print(item)
print()


# I repeated the same process for the stock entry, formatting the user's entry correctly, and using
# for loops and what I've learned about 2D lists to make sure they were displayed to the user correctly:


print("Now, please enter how much stock you have for each menu item (how many of these menu items you can serve before you run out of ingredients!)")
print()


for item in range(len(menu)):
    while True:
        try:
            stock_count = int(input(f"Please enter the number of available portions of {menu[item]}: "))
            print()
            break

        except Exception:
            print()
            print("Please only enter a number!")
            print()

    stock[menu[item]] = stock_count    
        

print()
print("Here is the amount of menu items you have to sell: ")
print()

stock_display = []

for item in menu:
    item_stock = [item, stock[item]]
    stock_display.append(item_stock)

for row in stock_display:
    for item in row:
        print(item, end="   ")
    print()


# I repeated the above process for the 'price' entry.

    
print()
print("Now, please enter the retail price for each menu item.")
print()


for item in range(len(menu)):
    while True:
        try:
            item_price = float(input(f"Please enter the retail price for {menu[item]}: "))
            print()
            break

        except Exception:
            print()
            print("Please only enter a number and/or a decimal place!")
            print()

    price[menu[item]] = item_price

print()
print("Here are the retail prices for your menu items: ")
print()

price_display = []

for item in menu:
    price_format = f"£{price[item]}"
    item_price = [item, price_format]
    price_display.append(item_price)

for row in price_display:
    for item in row:
        print(item, end="   ")
    print()


# I wanted to display the individual stock worth values first, so I used for loops to
# display this to the user:

print()
print("The individual stock worth of your items are as follows: ")
print()

total_item_worth = []

for item in menu:
    num_worth = f"£{(stock[item] * price[item])}"
    item_worth = [item, num_worth]
    total_item_worth.append(item_worth)

for row in total_item_worth:
    for item in row: 
        print(item, end="   ")
    print()


# I then used the sum method to work out the 'total stock worth' in the cafe, and displayed
# it to the user:

total_stock_worth = []

for item in menu:
    total_stock_worth.append((stock[item] * price[item]))

total_stock_worth = sum(total_stock_worth)

print()
print(f"Therefore, the 'total stock worth' in the cafe currently is £{total_stock_worth}")
print()
