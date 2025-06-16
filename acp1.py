list = [ 12,45.78,98]

start = 0 
end = 4
a = []
even = []
odd = []
for i in list:
    sq = i * i 
    a.append(sq)
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)