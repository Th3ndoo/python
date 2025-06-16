# recursion using factorial

def fact(n):
    '''The recursive function for find the factorial'''
    if n ==1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact.__doc__)
'''The main function to call the recursive function'''

n = int(input("enter the number"))
print(f"the factorial of the {n} is {fact(n)}")
