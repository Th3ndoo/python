# sum and average of a list


list1 = [ 89,67,45,78,45,98,981]

sum = 0

for i in list1:
    sum+=i

avg = sum/len(list1)
print(f"the list is {list1}")
print(f"the sum of the list is {sum}")
print(f"the average of the list is {avg}")
print(f"the maximum element in the list is {max(list1)}")
print(f"the minimum element in the list is {min(list1)}")