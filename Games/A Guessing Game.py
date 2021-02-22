
secret_word = "Cow"
guess = ""
guesses_taken = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guesses_taken < guess_limit:
        guess = input("Take a guess: (hint- the most common herbivore) ")
        guesses_taken += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you lost! :(")
else:
    print("Bravo! You guessed right.")
