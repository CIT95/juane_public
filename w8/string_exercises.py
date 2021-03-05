# w3resource.com
# 20, 33, 41, 42, 60

# 20 i did look at the sample solution. I got stuck on the .join part
 def reverse(string):
     if len(string) % 4 == 0:
         return "".join(reversed(string))
     return string


 print(reverse("four"))

# 33 I searched on google for the formula to get floating number by two decibles

x = 5.32424211314234242

print("{:.2f}".format(x))

#41 I did this by myself, learned from the udemy course 
message = "Woah this is weird, isnt it"

print(message.strip("Woah"))

#42 I also learned this from udemy

message = "This will now be a list!"

print(message.split(' = '))

#60 I needed a bit of help with this one
message = "Pretty cool how i could do this"

print(message.title())

#Pynative 16, 10, 8, 13, 12
#16 I was really confused on this so i looked at google
message = "Carl0s 1s R3ally C0Ol"

newmessage = "".join([item for item in message if item.isdigit()])

print(newmessage)

#10 I got the jist of it, just checked sample for a bit of help
message = "Carlos"
newmessage = dict()
for char in message:
    count = message.count(char)
    newmessage[char] = count

print(newmessage)

#8 Learned from UDEMY
message = "I am in the USA, usa in the UsA"
want = "USA"
howMuch = message.lower()
count = howMuch.count(want.lower())
print("How much times is USA display:", count)
#13 I went back on my notes to check up on how to do this
message = "This-has-to-be-a-joke"
splitMessage = message.split("-")

for sub in splitMessage:
    print(sub)

#12 I havent used the find one before so i looked up on google
message = "Emma is really Emma and Emma and of course Emma"
newmessage = message.find("Emma")

print("last position:", newmessage)
