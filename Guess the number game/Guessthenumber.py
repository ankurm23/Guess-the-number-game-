n=18
print("GUESS THE NO.")
i=1
while(i<=9):
    print("enter a no.")
    x=int(input())
    if x>n:
        print("your no. is greater than expected")
        print("you are left with" ,9-i)
    elif x<n:
        print("your no. is smaller than expected")
        print("you are left with" , 9-i)
        
        
    
    else: 
        print("you guessed the right no.")
        break         
    i=i+1
    if i>9:
        print("Game over")