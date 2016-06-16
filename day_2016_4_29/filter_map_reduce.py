test_data1=[0,1,2,3,4,5,6,7]
test_data2=['a','b','c','d','e','f','g','h','i']


def fun1():
    a=filter(lambda x:x>1,test_data1)
    for item in a :
        print(item)



def mapfun(data):
    return data.upper()






def fun2():
    b=map(mapfun,test_data2)
    for o in b:
        print(o)




if __name__=='__main__':
    fun2()


