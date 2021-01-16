print('Please give me a number.')
firstnumber = int(input())
print ('Thanks! Now give me a second number!')
secnumber = int(input())

if(firstnumber < secnumber):
    for i in range(firstnumber, secnumber + 1):
        #all prime numbers are greater than 1 so we make sure its higher than 1
        if i > 1:
            for num in range(2, i):
                if (i % num) == 0:
                    break      
                else:
                    if num == i//2 + 1:
                        print(i)

else:
    print('Make sure the second number is higher!')
