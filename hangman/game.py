#!/usr/bin/env python
from enum import Enum

GameState = Enum('GameState', [('WON', 1), ('LOST', 2), ('CONTINUE', 3)])

def get_random_word():
    return list('keyboard')

def get_game_state(word, guesses, max_guesses):
    valid_letters = []
    invalid_letters = []
    for guess in guesses:
        if guess in word:
            valid_letters.append(guess)
        else:
            invalid_letters.append(guess)

    if len(valid_letters) == len(set(word)):
        return GameState.WON

    if len(invalid_letters) == max_guesses:
        return GameState.LOST

    return GameState.CONTINUE

def get_bad_choices(word, guesses):
    invalid_letters = []
    for guess in guesses:
        if guess not in word:
            invalid_letters.append(guess)
    return invalid_letters

def get_display_word(word, guesses):
    letters = []
    for letter in word:
        if letter in guesses:
            letters.append(letter)
        else:
            letters.append(' ')
    return ''.join(letters)

def get_display_dashes(word, guesses):
    letters = []
    for letter in word:
        if letter in guesses:
            letters.append('*')
        else:
            letters.append('-')
    return ''.join(letters)

def prompt_for_guess(prompt, guesses):
    while True:
        guess = input(prompt).lower()
        if len(guess) != 1:
            print('pick a single character')
            continue

        if not ('a' <= guess <= 'z'):
            print('guess must be a character')
            continue

        if guess in guesses:
            print('you already guessed that, try again')
            continue

        return guess

def render_turn(word, guesses, max_guesses):
    display_word = get_display_word(word, guesses)
    display_dashes = get_display_dashes(word, guesses)
    bad_choices = get_bad_choices(word, guesses)
    print(f"What is the word {display_word}?")
    print(f"                 {display_dashes}")
    if len(bad_choices) > 0:
        print(f"Incorrect choices \"{''.join(bad_choices)}\". You have {max_guesses - len(bad_choices)} remaining.")

MAX_GUESSES = 6
guesses = []
word = get_random_word()

print('Welcome to the game of Hang Man')
print('')

while get_game_state(word, guesses, MAX_GUESSES) == GameState.CONTINUE:
    render_turn(word, guesses, MAX_GUESSES)
    guess = prompt_for_guess('choose a letter a-z: ', guesses)
    guesses.append(guess)

if get_game_state(word, guesses, MAX_GUESSES) == GameState.WON:
    print(f"Congratulations, you guessed the word {''.join(word)}")
else:
    print(f"Sorry, try again, the word was {''.join(word)}")
