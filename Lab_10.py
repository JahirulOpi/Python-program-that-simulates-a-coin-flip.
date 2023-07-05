import random 
num = 0
win = 0

while (True):
    print("Enter 1 for Head")
    print("Enter 2 for Tail")
    print("Enter 9 to exit")
    answer = int(input())
    flip = random.randint(1,2)
    if (answer == flip):
        num += 1
        win += 1
        print("You Won")
    elif (answer == 9):
        print ("number of flip "+ str(num))
        print ("You won "+str(win)+" times")
        break
    else:
        num += 1
        print("You Lost")
        
   
