name = input("What is your name?: ")

if len(name) < 3:    
    print("Your name must be at least 3 characters: " + str(len(name)))
elif len(name) > 50: 
    print("Your name reached the maximum characters (50): " + str(len(name)))
else:
    print("Your name looks good! " + str(len(name)))

print("Done")