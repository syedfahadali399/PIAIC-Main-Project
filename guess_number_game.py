from random import randint

def guess():
    random_number = randint(0, 10)
    input_user = 0
    while input_user != random_number:
        input_user = int(input("Enter a number between 1 to 10: "))
        random_number = randint(0, 10)
        if(input_user < random_number):
            print(f"Your guess number {input_user} is too low!")
            print("")
        elif(input_user > random_number):
            if input_user > 10:
                print(f"Your entered number {input_user} is greater than the 10")
                print("")
            else:
                print(f"Your guess number {input_user} is too high!")
                print("")
    else:
        print(f"Yah Congrats your number {input_user} and random number {random_number} is correct")

guess()