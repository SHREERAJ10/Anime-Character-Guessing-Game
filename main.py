import random
from animeChars import words

print("\nWelcome to guessing anime characters name!")
play = input("Are you ready to play? y/n\n").lower()
if play == "n":
    print("OK!")
    exit()

while play == "y":

    randomWord = random.choice(words)
    wordLength = len(randomWord)
    word = ["_"]*wordLength
    guesses = wordLength + 2
    count=0
    correct_guess = 0

    def listToStr(word):
        string = " "
        return (string.join(word))

    print(listToStr(word))

    while guesses > 0 :
        #case: Victory
        if listToStr(word).replace(" ","") == randomWord:
            print("You are correct. \nYOU WIN!")
            play = input("Do you want to play again? y/n\n")
            if play == "y":
                break
            else:
                print("Thanks for playing!")
                exit()

        char = input("Enter an alphabet: \n")

        if char == "qt":
            break

        for i in range(0,wordLength):
            word = list(word)
            if randomWord[i]==char:
                correct_guess = 1
                word[i]=char

            else:
                count+=1


        #Displaying the progress    
        print("\n"+listToStr(word))

        #epic victory
        if char == randomWord:
            print(f"Congratulations! You guessed it altogether!\nThe character is {randomWord}")
            play = input("Do you want to play again? y/n\n")
            if play == "y":
                break
            else:
                print("Thanks for playing!")
                exit()

        #case: Incorrect guess by the user
        if correct_guess !=1 and count>=1:
            guesses -=1
            print("\nTry Again!\n")

        print(f"\nChances remaining: {guesses}")

        if guesses == 0:
            print("You are out of chances.\nYOU LOSE!\n")
            print(f"The name of the character is {randomWord}")
            play = input("Do you want to play again? y/n\n")
            if play == "y":
                break
            else:
                print("Thanks for playing!")
                exit()
            

        #reseting the value for proper execution of above 'Try Again' condition
        correct_guess = 0
