goodinput = False
while not goodinput:

    try:
        print("Please give me a number.")
        firstnumber = int(input())
        if firstnumber < 0:
            goodinput = False
            print("Make sure it is a positive number!")
            continue

        print("Thanks! Now give me a second number!")
        secnumber = int(input())
        if secnumber < 0:
            goodinput = False
            print("Make sure it is a positive number! START AGAIN")
        elif firstnumber > secnumber:
            goodinput = False
            print("Make sure the second number is higher!")

        elif firstnumber < secnumber:
            goodinput = True
            for i in range(firstnumber, secnumber + 1):
                # all prime numbers are greater than 1 so we make sure its higher than 1
                if i > 1:
                    for num in range(2, i):
                        if (i % num) == 0:
                            break
                        else:
                            if num == i // 2 + 1:
                                print(i)

    except ValueError:
        print("This is not an Integer!")
