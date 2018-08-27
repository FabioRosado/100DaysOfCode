from string import ascii_lowercase

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class Hangman(object):
    def __init__(self):
        self.guesses = 0
        self.used_letters = []
        self.secret_word = list(get_word().lower())
        self.to_guess_word = [PLACEHOLDER if char in ASCII else char
                              for char in self.secret_word]
        self.start_game()

    def update_guess_word(self, letter):
        for index, char in enumerate(self.secret_word):
            if letter == char:
                self.to_guess_word[index] = letter

    def start_game(self):
        while True:
            print(f"You have {ALLOWED_GUESSES - self.guesses} attempts to guess the name of the movie.")
            print(f"Letters used: {self.used_letters}")
            print(self.to_guess_word, "\n")
            letter = input("Choose a letter to use as a guess.").lower()

            if letter in self.used_letters:
                print("You already tried that letter. Please try a different one.")
            elif letter not in self.secret_word:
                print("Sorry, the movie doesn't have that letter. You used 1 attempt.")
                self.guesses += 1
                print(HANG_GRAPHICS[self.guesses-1])
                self.used_letters.append(letter)
            else:
                print("The movie has that letter.")
                self.update_guess_word(letter)
                self.used_letters.append(letter)

            if self.to_guess_word == self.secret_word:
                print("Congratulations! You've found the name of the movie!")
                break
            elif self.guesses == ALLOWED_GUESSES:
                print("Sorry, you have lost this game. The name of the movie was:")
                print(self.secret_word)
                break


if __name__ == '__main__':
    Hangman()