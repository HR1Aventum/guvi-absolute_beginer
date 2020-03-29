def No_days(n):
    lst = ["Error",31,28,31,30,31,30,31,31,30,31,30,31]
    if n>len(lst):
        print("Error")
    else :
        print(lst[n])
a = int(input())
No_days(a)
