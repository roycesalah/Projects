# WORDLE
import urllib.request
import random
import re
import sys

# 6 tries total
# correct letter correct placement <letter>
# correct letter incorrect placement ?letter?
# incorrect letter ~letter~

def main():
    print('''
            ---===Wordle===---
    Guess the correct 5 letter word within 6 tries
    < > = Correct letter and placement
    ? ? = Letter in word but incorrect placement
    ~ ~ = Letter not in word
        ''')
    # WORDLE RANDOMIZED SELECTION
    #word = get_random_wordle()
    word = "SHORE"

    # 6 ATTEMPTS
    for i in range(6):

        while True:
            guess = guesstester(input("Guess: "))
            if guess == False:
                print("Invalid guess\n")
            else:
                break

        print(respond(guess,word)+"\n")
        if guess == word:
            sys.exit(f"Great job! {word.title()} was the word!")

    # GAME OVER
    print(f"Better luck next time! {word.title()} was the word.")

def get_wordlist():
    read = urllib.request.urlopen("https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt").read()
    words = list(read.splitlines())
    return words

def get_random_wordle():
    return str(random.choice(get_wordlist()),encoding="ascii").upper()

def respond(guess,answer):
    response = ""
    for letter in range(len(guess)):
        if guess[letter] == answer[letter]:
            response += ("<"+guess[letter]+"> ")
        elif guess[letter] in answer:
            response += ("?"+guess[letter]+"? ")
        else:
            response += ("~"+guess[letter]+"~ ")
    return response

def guesstester(guess):
    guess = guess.strip().upper()
    matches = re.search(r"^[A-Z]{5}$",guess)
    if matches and bytes(guess.lower(),"utf-8") in get_wordlist():
        return guess
    else:
        return False


if __name__ == "__main__":
    main()
