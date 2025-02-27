from random import randint

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
           guess = randint(low, high)
        else:
            guess = low    
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C): ")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yah! The Computer guess your number {guess}, Correctly")        

computer_guess(10)