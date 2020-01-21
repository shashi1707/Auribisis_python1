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
