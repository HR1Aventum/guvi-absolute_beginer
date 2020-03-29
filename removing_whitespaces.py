#func to remove whitespace
def re_Spaces(string):
    string = string.replace(' ','')
    print(len(string))



N_str = str(input())
#calling the function
re_Spaces(N_str)
