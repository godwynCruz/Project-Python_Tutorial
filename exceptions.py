# exception is a kind of error that crashes your program
# use try except to handle exceptions that are raised in our programs
# as a good programmer, you should always anticipate these kind of exceptions and handle them properly

try:
    age = int(input("Enter your age:"))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Age cannot be 0")