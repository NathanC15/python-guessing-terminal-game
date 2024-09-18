import random

player_name = str(input("Enter your name: "))
number = random.randint(1, 100)
attempts = 0
leaderboard = {'Tom': 2, 'John': 4}

while attempts != 5:
    guess = int(input("Guess a number between 1-100: "))

    if guess > number:
        print('Your guess is too high!')
        attempts = attempts + 1
    elif guess < number:
        print('Your guess is too low!')
        attempts = attempts + 1
    elif guess == number:
        print(f'You guessed the number: {number} in {attempts} attempts! Great job {player_name}!')
        leaderboard.update({player_name: attempts})
        print(leaderboard)
        exit()

if attempts == 5:
    print('You ran out of attempts! Try again!')
    exit()