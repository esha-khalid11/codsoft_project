import random
print("***ROCK PAPER SCISSOR GAME***")
print("***RULES***")
print('1:Rock beats scissors \n2:Scissors beat paper \n3:Paper beats rock')

def rps():
    user_input = int(input("Enter your choice 0 for rock,1 for paper,2 for scissor:"))
    if user_input>2 or user_input<0:
        print('You entered an invalid number')
    else:    

        computer_selection = random.randint(0,2)

        print('Computer choose:')
        print(computer_selection)

        if (computer_selection==user_input):
            print('Its a tie')

        elif computer_selection == 0 and user_input==2:
            print("You lose")

        elif user_input==0 and computer_selection == 2:
            print("You win")        

        elif (computer_selection>user_input):
            print('You lose')

        elif (user_input>computer_selection):
            print('You win')  
rps()
user_choice = input('Do you want to play another round(yes or no):')
if user_choice == 'yes':
    rps()
else:
    exit()    


