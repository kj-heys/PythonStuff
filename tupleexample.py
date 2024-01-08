<<<<<<< HEAD
myTuple = ("Cat", "Dog", "Penguin", "Zebra")
print(len(myTuple))


myTuple = ("Cat", "Dog", "Penguin", "Zebra")
print(myTuple[1])

myTuple = ("Cat", "Dog", "Penguin", "Zebra")
print(myTuple[-1])

x = ("Cat", "Dog", "Penguin", "Zebra")
y = list(x)
y[1] = "Cow"
x = tuple(y)

print(x)

print("never ever leave your machine open")
<<<<<<< HEAD
=======

# I hate Git
>>>>>>> master
=======
def food():
    global orders 
    orders = ['SFAC', 'LFAC', 'SAKP' , 'SAKPWC' , 'RSAC']
    x = int(input("Please make a selection: "))
    if(x == 1):
        print(orders[0] , "has been chosen.")
    if(x == 2):
        print(orders[1] , "has been chosen. ")
    if(x == 3):
        print(orders[2] , "has been chosen. ")
    if(x == 4):
        print(orders[3] , "has been chosen. ")
    if(x == 5):
        print(orders[4] , "has been chosen. ")
    else:
        print("Invalid option made. Process closed. Good Bye!")

while(True):
    food()
    #hello from me
    print("hello")
>>>>>>> master
