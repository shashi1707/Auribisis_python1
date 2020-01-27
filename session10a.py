def add(*args):
    print(args)
    print(type(args))
    sum=0
    for data in args:
        sum=sum+data
    print("sum is :",sum)
add(10,20,40,50)
add(10,20,40)

def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))
fun(name='shashibhushanpatel',data=20,email="sbhushan170697@")
print(fun)




"""def fun(**kwargs,*args):#error
    print(kwargs)
    print(type(kwargs))

fun(name="shashi",data=20,19,29)
"""
