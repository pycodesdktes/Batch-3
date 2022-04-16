import random
from word import *

print("Let's play a Word Game!")
print("Let me introduce this game to you- ")
print("observe the blank spaces,it will give u the idea of number of letters in the given word.")
print("You may, at any time, attempt to guess the whole word.")
print("On the other hand, if you run out of tries, you will lose.")
print("Now, Enter any alphabet and I will show you where it places.\n")
print("HINT:")

def get_word():
    type_ind = random.randint(0, len(type_lis) - 1)
    type_w = type_lis[type_ind]
    type_lis_2 = item_dict[type_w]
    list_ind = random.randint(0, len(type_lis_2) - 1)

    word = type_lis_2[list_ind]
    print("This is a", type_w)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)                           # to show unguessed letters as _
    guessed = False
    guessed_letters = []                                        # holds the letter that user guessed
    guessed_words = []                                          #holds the word user that guessed
    tries = 6 # no. of tries



    print(display_word(tries))                                  # initial state of the word
    print(word_completion)                                      # initial state of the word eith _aa
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word:").upper() # getting letter input from the user & store it in variable
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:                                               # user made a correct guess
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)                   # append guess to guessed_letters
                # to revel to the user all occurrences of guess
                word_as_list = list(word_completion)            # converting word completion into a list, so we're able to index it
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess                 # replace each _ by guess
                word_completion = "".join(word_as_list)         # updating word_completion with new changes & converting it into a string
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():       # if guess is a word
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)                     #append guess to guessed_words
            else:                                               # user correctly guessed the word
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_word(tries))
        print(word_completion)

    if guessed:                                                 # check if user guessed word correctly or ranout of tries
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def display_word(tries):                                        # to display no. of tries left
    stages = [
        """NO TRIES LEFT!""",
        """ONE TRY LEFT!!""",
        """TWO TRIES LEFT!!""",
        """THREE TRIES LEFT!""",
        """FOUR TRIES LEFT""",
        """FIVE TRIES LEFT""",
        """\nLET'S GET STARTED!"""
    ]
    return stages[tries]
def main():
    word = get_word()                                               # getting word from get_word
    play(word)                                                      # pass this word to play
    while input("Play Again?if yes press Y otherwise press anykey").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()


