# numbers in reverse order skipping 5
print("the number is reverse order for 10 to 1 sipping 5")
for i in range(10,0,-1):
    if i == 5:
        continue
    print(i)