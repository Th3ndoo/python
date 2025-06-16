# multiple exception
try:
    val1,val2 = eval(input("enter 2 numbers seperated by commas"))
    result = val1/val2
    print(result)
except ZeroDivisionError:
    print("zero Division Error occurs")
except SyntaxError:
    print("enter the number seperated by commas")
except:
    print("the error occured")
else:
    print("program succesfully runs")
finally:
    print("if error or no error this block gets executed")