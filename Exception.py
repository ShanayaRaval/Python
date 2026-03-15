try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    res = num1 / num2
    print("Result is: ", res)

except ZeroDivisionError:
    print("Division by Zero is Error !!")

except SyntaxError:
    print("Comma is missing. Numbers should be separated by comma like this - 1,2")

except:
    print("Invalid Input!")

else:
    print("No exceptions.")

finally:
    print("This will execute no matter what.")