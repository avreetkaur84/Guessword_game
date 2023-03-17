import random
import time

def wmk():

    vocab = {
        'Adept' : 'A person who is skilled or expert at something',
        'Articulate' : 'The art of expressing an idea or feeling with clarity.',
        'Candor' : 'Noun that refers to honesty, being truthful and sincere',
        'Conductive' : 'Adjective that means to help make an outcome possible.',
        'Deference' : 'A noun that means respectful submission to or courteous',
        'Egregious' : 'Adjective that means extremely bad, horrifying or appalling.',
        'Entail' : 'A verb which means to involve something necessary or require.',
        'Facilitate' : 'A verb which means to make something easier.',
        'Gist' : 'A noun that refers to essential meaning of speech or text.',
        'Knack' : 'A noun that refers to a special skill an individual possesses that is difficult to reach.',
        'Novel' : 'Adjective which means new and innovative.',
        'Obsolete' : 'Adjective to describe something that is no longer used or produced.',
        'Paramount' : 'Ajective means more important than anything else or chief in importance.',
        'Reinforce' : 'Verb means to strengthen and add support.',
        'Tremendous' : 'Adjective that means extraordinary in size, amount, intensity or excellence.'
        }

    key, value = random.choice(list(vocab.items()))
    guess_word = ""
    turns = 3
    time.sleep(2)
    print(value)
    guess_word = input("Enter your answer: ")

    while len(key) > 0:
        
        if guess_word == key:
            print("Your answer is right!!")
            print("You won!!")
            print("")
            time.sleep(2)
            loop_play()
        
        if guess_word != key:
            turns = turns - 1
            
            if turns == 2:
                print("Your answer is wrong")
                print("2 more guesses to enter right answer!!")
                print("")
                guess_word = input("Enter your answer: ")

            if turns == 1:
                print("Your answer is wrong")
                print("1 more guess to enter right answer!!")
                print("")
                guess_word = input("Enter your answer: ")

            if turns == 0:
                print("No more turns!! \n You lost the game!!") 
                print(f"The correct answer is {key}")
                print("")
                time.sleep(1)
                loop_play()

def loop_play():
    answer = input("Do you want to play again? \n Type Yes to continue and No to exit: ")
    if answer == "Yes":
        print("")
        wmk()
    elif answer == "No":
        print("We hope to see you again soon!! \n Thanks for playing!!")
        time.sleep(2)
        quit()
    else:
        print("")
        print("Enter the valid response (Yes or No).")
        loop_play()

name = input("Enter your name: ")
print("Welcome to the game!!!")
print("You have 3 chances to guess the right word according to the definition")
print("")
wmk()