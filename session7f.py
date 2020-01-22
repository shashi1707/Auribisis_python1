menu={
    "dal":150,
    "roti":10,
    "paneer":180,
    "salad":10,
    "noodles":50
}
print("Your menu is here:")
print(menu.keys())

cart=[]

choice="yes"
while choice=='yes':

    fooditem=input("Enter a food item")
    if fooditem in menu:
        cart.append(fooditem)
        choice=input("would you like to add another fooditem(yes/no:")
    else:
        print("please choose another food item")

print("Your cart:",cart)
totalprice=0
for item in cart:
    totalprice=totalprice+menu[item]

print("total price",totalprice)
amount = int(input('Enter the amount:'))
promocode = input('Enter the promocode :')

if amount > 100:
    if amount > 200 and promocode == 'JUMBO':
        print('Your entered amount is:', amount)
        print('Your entered promocode is:', promocode)
        print("Promocode is successfully applied")
        amount = amount - (.5 * amount)
        print('Amount to be paid after applying the promocode is:', amount)

    elif amount > 200 and promocode == 'ZOMATO':
        print('Your entered amount is:', amount)
        print('Your entered promocode is:', promocode)
        print("Promocode is successfully applied!!")
        amount = amount - (.4 * amount)
        print('Amount to be paid after applying the promocode is:', amount)
    elif amount < 200 and promocode == 'ZOMATO':
        print('Please try the JUMBO as promocode to get 50% OFF')
    elif amount < 200 and promocode=='JUMBO':
        print('Your entered amount is:', amount)
        print('Your entered promocode is:', promocode)
        print("Promocode is successfully applied")
        amount = amount - (.5 * amount)
        print('Amount to be paid after applying the promocode is:', amount)

    else:
        print('Please try the ZOMATO or JUMBO as promocode to get 40% or 50% OFF respectively')


