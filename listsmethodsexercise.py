numbers = [2, 2, 3, 3, 5, 6, 6]
uniques = []

for num in numbers:
    if num not in uniques:
        uniques.append(num)
        print(num)
