# WORDLE
    #### Video Demo: https://youtu.be/faKuEkxzGOY

    #### Description:
    
    Wordle was originally developed by Josh Wardle in 2014, revised and published in 2021,
    and finally purchased by the New York Times in 2022. The game swept the nation by a storm,
    rising from 90 to over 2 million players within the span of under 2 months.

    The program I developed for my final project is a simplified recreation of the game. The program
    operates on 4 very simple functions. The first function is a URL reader which utilizes
    the urllib2 library to read a webpage containing all possible 5-letter words and create a
    list.

    The second function selects a random word from the aforementioned list using the
    random library's choice function. This selection is used as the Wordle session's answer.

    The user is allowed 6 (valid) guesses, which the program checks against the answer,
    and returns a response identifying which letters within the guess are:
    1) < > = in the word and with correct placement
    2) ? ? = in the word but with incorrect placement
    3) ~ ~ = are not in the word at all

    In order to achieve this, a guess validation function was implemented which makes sure the guess
    is an existing word. The method used to accomplish this was by utilizing regular expressions.
    The re library makes it very simple to validate that all characters in the guess are within
    the acceptable set and that the guess is the acceptable length. The function then checks the
    guess against the list of all possible 5-letter words and returns either the users cleaned guess,
    in the case that both tests pass, or False, in the case that it doesn't pass either or both cases.

    Lastly, to analyze the user's guess, a function is used to iterate through the guess and check it
    against the answer. The check appends the state of the character from the 3 states mentioned above.

