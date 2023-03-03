import random

# Initialize variables
score = 0
num_flips = 0

# Print welcome message
print("Welcome to the Coin Flipping Game!")

# Loop until user decides to quit
while True:

    # Generate random coin flip
    coin = random.choice(['heads', 'tails'])

    # Print demarcation for the round
    print("="*20)
    print(f"FLIP {num_flips + 1}")

    # Display the probability of getting heads or tails
    print("The probability of getting heads is 0.5 and the probability of getting tails is 0.5")

    # Prompt user for guess
    guess = input('Guess heads or tails (type "heads" or "tails"): ')

    # Validate input
    while guess not in ['heads', 'tails']:
        guess = input('Invalid input. Guess heads or tails (type "heads" or "tails"): ')

    # Check if guess is correct
    if guess == coin:
        print('You guessed correctly!')
        score += 1
    else:
        print('Sorry, the coin landed on', coin)

    # Increment number of flips
    num_flips += 1

    # Display running score
    percentage_correct = (score / num_flips) * 100
    print(f'You correctly guessed {score} out of {num_flips} flips ({percentage_correct:.2f}%).')

    # Ask user if they want to continue playing
    play_again = input('Do you want to play again? ([y] or n): ')

    # Check if user wants to quit
    while play_again not in ['y', 'n', '']:
        play_again = input('Invalid input. Do you want to play again? ([y] or n): ')

    # Exit the loop if user doesn't want to play again
    if play_again.lower() == 'n':
        break

# Print final results
percentage_correct = (score / num_flips) * 100
print("="*20)
print(f'You correctly guessed {score} out of {num_flips} flips ({percentage_correct:.2f}%).')
