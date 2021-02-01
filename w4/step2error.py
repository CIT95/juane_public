goodinput = False
while not goodinput:
    try:
        int(input("Type a number:"))
        goodinput = True
        print("Nice number")

        print("Now type F to exit:")
        exitApp = input("")
        if exitApp == "F":
            raise SystemExit
        else:
            print("you are stuck here.")
            goodinput = False
            continue
    except ValueError:
        print("No, type a number")
