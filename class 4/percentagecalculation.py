# take marks as input from user
print("Enter Marks Obtained in 4 subjects")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
technology = int(input("technology :"))

# Let's calculate the percentage of marks
sum = math+english+science+technology
print("sum of math, english, science, technology" ,sum)

perc = (sum/400)*100

print(end = "Percentage Mark = ")
print(perc)
