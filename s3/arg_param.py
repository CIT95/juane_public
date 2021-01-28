def greet(name, msg="Nice to meet you!"):
    if name == 'Carlos':
       print('hey carlos, glad to see you again!')
    else: 
     print('Oh, I love that name ' + name + ', ' + msg)
     coolname(name)

    
#this will greet while knowing their name from the first function or my name lol
def coolname(name):
    import time
    time.sleep(2)# Just adding time so it doesnt feel like its responding quick
    if len(name) <= 4:
        print(' That is a real unique name, ' + name + '. Names with few letters are always cool!')
    else:
        print(' You know. ive always loved that name, ' + name + '. Every name is unique in its own way!')
   
      
        



def nameinfo():
    name = input('Hi what is your name?')
    greet(name)

nameinfo()



