import random
def wmk():
    vocab = {
              "The lack or unavailability of something or someone" :  "absence",
              "Having a positive opinion of something or someone" : "approval",
              "The response or receipt to a phone call, question, or letter" : "answer",
              "Noticing or recognizing something of interest" : "attention",
              "A mass or a collection of something" : "amount"
            }
    key, value = random.choice(list(vocab.items()))
    turns = 3
    guessmade = ''
    valid_entry = set('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z')
    print(key)

    while len(value) > 0:
        main_word = ""
        missed = 0

        for letter in value:
            if letter in guessmade:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "

        if main_word == value:
            print(main_word)
            print("You guessed correctly!!")
            break

        print("Guess the word", main_word)
        guess = input()

        if guess in valid_entry:
            guessmade = guessmade + guess
        else:
            print("Enter valid character")
            guess = input()

        if guess not in value:
            turns = turns - 1

            if turns == 2:
                print("2 turns left!!")

            if turns == 1:
                print("You only have one chance left")

            if turns == 0:
                print("You loose!!")
                print("No more chances left!!")

name = input("Enter your name: ")
print("Welcome", name, "!")
print("Guess the words which has definition as given below")
print("You have less than 3 attempts to guess the right word")
wmk()