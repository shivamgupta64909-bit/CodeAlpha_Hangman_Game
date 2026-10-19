
import random
print("----------------------------------")
print("Welcome to Hangman!")
print("----------------------------------")
words = ["phone", "laptop", "college", "informtation", "computer"]

word = random.choice(words)

hidden_word = ["_"] * len(word)

wrong_guesses = 0
max_wrong_guesses = 6

guessed_letters = []

while "_" in hidden_word and wrong_guesses < max_wrong_guesses:

    print("\nWord:", " ".join(hidden_word))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")

        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        print("Wrong guess!")
        wrong_guesses += 1

if "_" not in hidden_word:
    print("\nCongratulations! You winner !")
else:
    print("\nGame Over!")

print("The word was:", word)