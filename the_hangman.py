import random

word_list = ["aardvark", "baboon", "camel", "kedi"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
correct_letters = []
lives = 6

hangmen = [
    '''
      +--+
      |  |
      O  |
     /|\ |
     / \ |
         |
    =====
    ''',
    '''
      +--+
      |  |
      O  |
     /|\ |
     /   |
         |
    =====
    ''',
    '''
      +--+
      |  |
      O  |
     /|\ |
         |
         |
    =====
    ''',
    '''
      +--+
      |  |
      O  |
     /|  |
         |
         |
    =====
    ''',
    '''
      +--+
      |  |
      O  |
      |  |
         |
         |
    =====
    ''',
    '''
      +--+
      |  |
      O  |
         |
         |
         |
    =====
    ''',
    '''
      +--+
      |  |
         |
         |
         |
         |
    =====
    ''',
    '''
      +--+
         |
         |
         |
         |
         |
    =====
    '''
]

word_length = len(chosen_word)

for position in range(word_length):
    placeholder += " _ "
print(placeholder)

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += " _ "

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! Lives remaining: {lives}")
        

    if lives == 0:
        print("Game Over! You've run out of lives.")
        print(hangmen[0])
        game_over = True

    if "_" not in display:
        print("You Won!")
        game_over = True

    print(hangmen[lives])