import random
words=["programming","coding","library","computer"]
word_random=random.choice(words)
word_list=list(word_random)
random.shuffle(word_list)
shuffled_word="".join(word_list)
print("Welcome to the Word Scramble Game!")
print(shuffled_word)
attemps=5
while attemps>0:
    word_input=input("Try to guess the original word from the scrambled word:")
    if(word_input==word_random):
        print("Congratulations! You guessed the correct word")
        break
    else:
        attemps-=1
        if attemps>0:
            print(f"Incorrect! Try again. You have {attemps} attempts left.")
        else:
            print(f"You’re out of attempts! The correct word was: {word_random}")

