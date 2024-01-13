secret_number = 9
chances_count = 0
chances_limit = 3

while chances_count < chances_limit:
    chances = int(input("Guess: "))
    chances_count += 1
    if chances == secret_number:
        print("You won!")
        break
else:
    print("You lose!")
    print("Try again.")

