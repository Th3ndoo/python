# weather predition

w = (1,0,0,1,0,1,1,0,0,1)

sun = 0
rain = 0

for weather in w:
    if weather == 0:
        sun+=1
    else:
        rain+=1

if sun > rain:
    print("Awsome sunny day")
else:
    print("Raining dogs and cats")