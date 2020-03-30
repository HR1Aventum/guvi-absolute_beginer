#creating fuunction
def Simple_interest(p,t,r):
    S = (p*t*r)/100
    print("%.2f" % S)
x,y,z=map(float, input().split())
#calling function
Simple_interest(x,y,z)
