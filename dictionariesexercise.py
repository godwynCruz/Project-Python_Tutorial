print("Numbers to words translator!")
phone = input("Phone number: ")
digits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

output = ""
for every_number in phone:
    output += digits.get(every_number, "?") + " "

print(output)
