import random
import time
import pyttsx3
a = pyttsx3.init()

def wmk():

    states = {
        'Andhra Pradesh' : 'Amaravati',
        'Arunachal Pradesh' : 'Itanagar',
        'Assam' : 'Dispur',
        'Bihar' : 'Patna',
        'Chhattisgarh' : 'Raipur',
        'Goa' : 'Panaji',
        'Gujarat' : 'Gandhinagar',
        'Haryana' : 'Chandigarh',
        'Himachal Pradesh' : 'Shimla',
        'Jharkhand' : 'Ranchi',
        'Karnataka' : 'Bangalore',
        'Kerala' : 'Thiruvananthapuram',
        'Madhya Pradesh' : 'Bhopal',
        'Maharashtra' : 'Mumbai',
        'Manipur' : 'Imphal',
        'Meghalaya' : 'Shillong',
        'Mizoram' : 'Aizawl',
        'Nagaland' : 'Kohima',
        'Odisha' : 'Bhubaneshwar',
        'Punjab' : 'Chandigarh',
        'Rajasthan' : 'Jaipur',
        'Sikkim' : 'Gangtok',
        'Tamil Nadu' : 'Chennai',
        'Telangana' : 'Hyderabad',
        'Tripura' : 'Agartala',
        'Uttarakhand' : 'Dehradun',
        'Uttar Pradesh' : 'Lucknow',
        'West Bengal' : 'Kolkata'
    }

    key, value = random.choice(list(states.items()))
    guess_word = ""
    turns = 3
    time.sleep(2)
    print(key)
    a.say(key)
    a.runAndWait()
    a.say("Enter your answer: ")
    a.runAndWait()
    guess_word = input("Enter your answer: ")
    
    while len(value) > 0:
        
        if guess_word == value:
            print("Your answer is right!!")
            print("You won!!")
            print("")
            time.sleep(2)
            loop_play()
        
        if guess_word != value:
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
                print(f"The correct answer is {value}")
                print("")
                time.sleep(1)
                loop_play()

def loop_play():
    a.say("Do you want to play again? \n Type Yes to continue and No to exit: ")
    a.runAndWait()
    answer = input("Do you want to play again? \n Type Yes to continue and No to exit: ")
    if answer == "Yes":
        print("")
        wmk()
    elif answer == "No":
        a.say("We hope to see you again soon!! \n Thanks for playing")
        a.runAndWait()
        print("We hope to see you again soon!! \n Thanks for playing!!")
        time.sleep(2)
        quit()
    else:
        print("")
        a.say("Enter the valid response (Yes or No).")
        a.runAndWait()
        print("Enter the valid response (Yes or No).")
        loop_play()

a.say("Enter your name: ")
a.runAndWait()
name = input("Enter your name: ")
print(f"Welcome to the game {name}!")
a.say(f"Welcome to the game {name}!")
a.runAndWait()
print("You have 3 chances to guess the right capital of Indian state")
a.say("You have 3 chances to guess the right capital of Indian state")
a.runAndWait()
print("")

wmk()