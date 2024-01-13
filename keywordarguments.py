first_name = input("What is your first name: ")
last_name = input("What is your last name: ")
name = ""

def greet_user(name): 
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user(name)
print("Finish")

def greet_user(first_name, last_name): 
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user(first_name="yuichi", last_name="marie") # <- positional arguments
print("Finish")

# Yuichi = first parameter, Marie = second parameter based on the position of parameters
# "first_name & last_name" keyword argument
# positional arguments = their position / argument matters
# keyword arguments = their position doesn't matter
# keyword must come after positional arguments
# most of the time, use positional arguments, if there is numerical values then use keyword