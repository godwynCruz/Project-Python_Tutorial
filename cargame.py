command = ""
started = False

while True:
    command = (input("> ")).upper()
    if command == "START":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car started... Ready to go!")  
    elif command == "STOP":
        if not started:
            print("Car already stopped!")
        else:
            started = False
            print("Car stopped...")
    elif command == "QUIT":
        break
    elif command == "HELP":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    else:
        print("I do not understand that, type 'help'.")
 