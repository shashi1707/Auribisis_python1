def show(num):
    if num==0:
        return 
    print('num is:',num)
    num-=1
    show(num)

show(10)
