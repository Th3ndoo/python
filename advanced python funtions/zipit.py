# zip function

a = [10,20,30,40]
b = [100,200,300,400]

for x,y in zip(a,b[::-1]):
    print (x,y)

stocks = ['infosys','bekcys','chicken licken']
price = [2145,3000,2410]

dic1 = {stock:price for stock,price in zip(stocks, price)}

print(dic1)