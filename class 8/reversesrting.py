# reverse a string

str = input("enter a string")
rev = ""
for i in str:
    rev = i + rev

print(f"The reverse of the given {str} is {rev}")