
import random

print ('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n"
      + "Good luck ^_^ \n"
      + "-"*50)

while True:
    print( "Enter your choice \n (1) - Rock \n (2) - paper \n (3) - scissors\n")
    choice = int (input("Enter your choice: "))

    while choice > 3 or choice < 1:
        choice = int (input('Enter a vaild choice please: '))

    if choice == 1:
        name = "Rock"
    elif choice == 2:
        name = "Paper"
    else :
        name = "scissors"
    
    print (f"User choice is : {name}")
    print ("--"*50)
    print ("Now it's computer's turn...")
    print ("--"*50)

    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_name = "Rock"
    elif comp_choice == 2:
        comp_name = "Paper"
    else :
        comp_name = "Scissors"

    print (f"Computer choice is : {comp_name}")
    print ("--"*50)
    print (f"{comp_name} vs {name}")
    print ("--"*50)

    if choice == comp_choice:
        res = "Draw"

    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        res = "Paper"

    elif (choice == 1 and comp_choice == 3 ) or (comp_choice == 1 and choice == 3):
        res = "Rock"

    elif (choice == 2 and comp_choice== 3) or (comp_choice == 2 and choice == 3):
        res = "Scissors"

    if res == "Draw":
        print (" --> It's a tie <--")
        print ("--"*50)

    elif res == name :
        print (" --> User win <-- ")
        print ("--"*50)
        
    else :
        print (" --> Computer wins <--")
        print ("--"*50)

    print ("Do you want to play again ? (Y/N)")
    ans = input ().lower()
    if ans == 'n':
        print("Goodbye....")
        break 
