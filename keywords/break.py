# check alphabet "a" is present or not

str1 = input("enter a phrase")

for i in str1:
    if i.lower() == "a":
        print(f"a is present in {str1}")
        break
    
else:
    print(f"a is not present in {str1}")