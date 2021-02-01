def fizz_buzz(num):  # new function

    try:
        if num < 0:

            print("Please type a positive number, try again.")
            return ()

        if num % 3 == 0 and num % 5 == 0:  # if divisible by both 3 and 5 it will print
            print("FIZZBUZZ")
        elif num % 5 == 0:
            print("BUZZ")  # ELIF just in case the first case doesnt work
        elif num % 3 == 0:
            print("FIZZ")
        else:
            print(
                "nothing:( just your silly number: " + str(num)
            )  # if all fails then it will give me my number back

    except:
        pass


def getInfo():  # this was called
    try:

        num = int(
            input("Type in a number please: ")
        )  # basically asking for number and assigning it as num

        fizz_buzz(num)  # calling another function while adding num
    except ValueError:
        print("Nope type a real number!")


getInfo()  # this is the only thing the code sees and is calling a function called getInfo
