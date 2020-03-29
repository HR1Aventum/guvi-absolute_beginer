def Check(n):
    print("Even") if (n%2==0 and n>0) else print("Zero") if n==0 else print("Odd")
n = int(input())
#calling function
Check(n)
