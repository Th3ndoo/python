# arrays
import array as arr

a = arr.array("i",[12,45,67,122,11,32,12,75,12])
print("array a")
print(a)

# count the no of the given elements
print(f"the number of 12 is given in array is {a.count(12)}")

a.reverse()

print(a)