temperature = float(input("What is the temperature today?: "))

if temperature > 30:    
    print("It's a hot day")
    print("Drink plenty of water") 
elif temperature > 20: # (20, 30]
    print("It's a nice day")
elif temperature > 10: # (10, 20]
    print("It's a bit cold")
else:
    print("It's a cold day")
    print("Wear warm clothes") 

print("Done")
