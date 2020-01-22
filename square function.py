num=10
print('num is :',num,hex(id(num)))

def square(n):
    global  num
    n=n*n
    num=n
    print('square is',n,hex(id(n)))
    print('num is:',num,hex(id(num)))

square(3)
print('num is:',num,hex(id(num)))

print('>>>>>>>><<<<<<<')

def square(num): # num is a Reference Variable which holds HashCode of 10
    print(">> [SQUARE] num is:", num, hex(id(num)))
    num = num * num
    print(">> [SQUARE] num now is:", num, hex(id(num)))


num = 10  # num is a Reference Variable which holds HashCode of 10
print(">> [MAIN] num is:", num, hex(id(num)))
square(num)
print(">> [MAIN] num now is:", num, hex(id(num)))

