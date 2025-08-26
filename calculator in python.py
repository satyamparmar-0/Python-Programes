def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
while True:
    print("1- for addition\n2- for substraction\n3- for multiply\n4- for divide\n5- for exit")
    op = input("enter any input ")
    if op in ('1','2','3','4'):
        n1=int(input("enter any number "))
        n2=int(input("enter any number "))
        if op =='1':
            print(add(n1,n2))
        elif op =='2':
            print("the substraction is ",sub(n1,n2))
        elif op=='3':
            print("the multiply is ",mul(n1,n2))
        elif op=='4':
            print("the divide is ",div(n1,n2))
    elif op=='5':
        print("GoodBye! exit")
        break
    else:
        print("calculate yourself")
    
