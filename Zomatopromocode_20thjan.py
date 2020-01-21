#Zomato promocode
"""
amount>200,promocode-ZOMATO>>>>40% OFF
amount>100,promocode-JUMBO>>>>50% OFF


"""
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




