def Fact(n):
    if (a==0 or a==1):
        print("1")
    elif (a<0):
        print("error")
    else:
        for i in range (1,n):
            n = n * i
        print(n)
a = int(input())
Fact(a)
