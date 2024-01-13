numbers = [2, 2, 2, 7, 7]

for x_count in numbers:
    # print("x" * x_count)
    output = "" #magiging 0 ulit value once na masatisfy 'yung inner loop
    for count in range(x_count):
        output += "x" #will produce 5 x then will go to the next number on the list
    print(output)