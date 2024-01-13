# having a loop inside loop
# y loop will continue as long as it reach the range, will go back to outer and will go to y again

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")
