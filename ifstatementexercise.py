buyer = False
price = 1000000

if buyer :
    payment = price * 0.10 
    print("The downpayment will be: $" + str(payment))

else : 
    payment = price * 0.20
    print("The downpayment will be: $" + str(payment))

#or

print(f"The downpayment will be: ${payment}")