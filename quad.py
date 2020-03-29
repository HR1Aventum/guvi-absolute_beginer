# creating a function
def Quad(a,b,c):
    x1 = (-b + pow((b ** 2) - (4*a*c), 0.5))/(2*a)
    x2 = (-b - pow((b ** 2) - (4*a*c), 0.5))/(2*a)
    print("%.2f" % x1)
    print("%.2f" % x2)
a,b,c = map(float, input().split())
#calling the function
Quad(a,b,c)
