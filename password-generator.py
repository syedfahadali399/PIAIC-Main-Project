from random import choice
from time import sleep

sleep(0.3)
print("Welcome To Password Generator")
sleep(0.4)
input_amount = int(input("Enter the amount of password do you want?: "))
sleep(0.5)
input_lenght = int(input("Enter the lenght of your password: "))

def pass_generator(amount_of_pass, lenght_of_pass):

    all_character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&0123456789"

    print("\nGenerating your Password")
    sleep(2)

    for pwd in range(amount_of_pass):
        password = ''
        for c in range(lenght_of_pass):
            password += choice(all_character)
        print(password)

pass_generator(input_amount, input_lenght )