# Checking the frequency

dic1 = {"pen": 2,"mobile":2,"diary":3,"pencil":2}

k =2
count = 0
for value in dic1.values():
    if value ==2:
        count+=1

print(f"the key which has the value {k} is {count}")