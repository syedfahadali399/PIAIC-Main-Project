from random import choice

repeat_program = int(input("How Many you have to play game: "))

def game(r):

    for r in range(0, r):

        user_input = str(input("What is your choice : r for rock, p for paper , s for scissor: "))
        comp_choice =  choice(["r", "p", "s"])

        if user_input not in ["r", "p", "s"]:
            print("Please Enter (r, p, s) to play game: ")
            break
        else: 
            if(user_input == comp_choice):
                print("Its Draw")
            elif(user_input == "r" and comp_choice == "p"):
                print("You Lose")
            elif(user_input == "r" and comp_choice == "s"):
                print("You Win")
            elif(user_input == "p" and comp_choice == "r"):
                print("You Win")
            elif(user_input == "p" and comp_choice == "s"):
                print("You Lose")
            elif(user_input == "s" and comp_choice == "r"):
                print("You Lose")
            elif(user_input == "s" and comp_choice == "p"):
                print("You Win")
            else:
                print("System Error run again")
    r += 1

game(repeat_program)