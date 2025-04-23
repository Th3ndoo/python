# character accrance in a phrase

word = input("Enter a phrase ")
ch = input("Enter a character")
count = 0
for i in word:
    if i.lower() == ch.lower():
        count += 1
        
print(f"The no of accurance of {ch}  ind {word} is {count}")