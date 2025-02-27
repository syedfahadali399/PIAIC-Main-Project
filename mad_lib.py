from time import sleep

sleep(0.5)
print("Welcome To Mad libs Project")

sleep(1.5)
print("Here is the undefined story where you put the noun, pronoun and adjective word to fill the story")

noun = "Noun"
pronoun = "Pronoun"
adjective = "Adjective"

sleep(3)
print("Loading Story...")

sleep(2)
print(f"""Once upon a time, in a mysterious {noun}, there lived a brave {noun} named {noun}.
{pronoun} embarked on a quest to rescue a {adjective} princess from a {adjective} {noun}.
{pronoun} journeyed through a {adjective} {noun} and discovered a {adjective} treasure.""")

print("")

input_noun_1 = str(input("Enter 1st Noun word: "))
input_noun_2 = str(input("Enter 2nd Noun word: "))
input_noun_3 = str(input("Enter 3rd Noun word: "))
input_pronoun_1 = str(input("Enter 1st Pronoun word: "))
input_adjective_1 = str(input("Enter 1st Adjective word: "))
input_adjective_2 = str(input("Enter 2nd Adjective word: "))
input_noun_4 = str(input("Enter 4th Noun word: "))
input_pronoun_2 = str(input("Enter 2nd Pronoun word: "))
input_adjective_3 = str(input("Enter 3rd Adjective word: "))
input_noun_5 = str(input("Enter 5th Noun word: "))
input_adjective_4 = str(input("Enter 4th Adjective word: "))

sleep(0.5)
print("Arranging Words...")

sleep(3)
print(f"""Once upon a time, in a mysterious {input_noun_1}, there lived a brave {input_noun_2} named {input_noun_3}.
{input_pronoun_1} embarked on a quest to rescue a {input_adjective_1} princess from a {input_adjective_2} {input_noun_4}.
{input_pronoun_2} journeyed through a {input_adjective_3} {input_noun_5} and discovered a {input_adjective_4} treasure.""")

print("")

sleep(0.5)
print("The End !")






