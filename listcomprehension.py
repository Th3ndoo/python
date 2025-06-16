# list comprehension for odd numbers

list1 = [2,3,13,12,14,5,17,19]
listc = [i for i in list1 if i%2==1]
print(listc)

fruits = ['apple','orange','banana']
list_s = [i.capitalize() for i in fruits ]

print(list_s)