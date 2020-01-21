def squaringList(mylist):
    for i in range(0,len(mylist)):
        mylist[i]=mylist[i]*mylist[i]
    print('Squaring of each element of list:',mylist)

mylist=[1,2,4,5,6]
squaringList(mylist)