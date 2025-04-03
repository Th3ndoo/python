# Taking total amount as input from user
Amount = int(input("Please Enter Amount for Withdraw :"))

# Calculating the number of notes of different denominators
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("notes of 100 dollars", note_1)
print("notes of 50 dollars", note_2)
print("notes of 10 dollars", note_3)