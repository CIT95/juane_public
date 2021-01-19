def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print('FIZZBUZZ')
    elif num % 5 == 0:
        print('BUZZ')
    elif num % 3 == 0:
        print('FIZZ')
    else:
        print('nothing:( just your silly number: ' + str(num))



    


def getInfo():
    num = int(input("Type in a number please: "))
    fizz_buzz(num)

getInfo()