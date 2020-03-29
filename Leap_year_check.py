#creating a func:
def Year(n):
    print("Y") if (n%4==0 or n%100 != 0 and n%400==0) else print("N")
n = int(input())
#calling the function
Year(n)
