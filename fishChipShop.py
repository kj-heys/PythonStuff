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
    
