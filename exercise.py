weight = float(input("Weight: "))
unit = (input("(k)g or (l)bs: "))

if unit.upper() == "K":
    converted = weight * 2.2
    print("Weight in lbs: " + str(converted))

elif unit.upper() == "L":
    converted = weight / 2.2
    print("Your weight in kg: " + str(converted))

else:
    print("Try again.")