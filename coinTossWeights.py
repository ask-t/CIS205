import random

# Generate random probability for heads between 0.2 and 0.8
prob_heads = random.uniform(0.2, 0.8)
prob_tails = 1 - prob_heads

# Initialize variables
score = 0
num_flips = 0

# Loop until user decides to quit
while True:
    # Generate random coin flip
    coin = random.choices(['heads', 'tails'], weights=[prob_heads, prob_tails], k=1)[0]
    
    # Display the probability of getting heads or tails
    print(f"The probability of getting heads is {prob_heads:.2f} and the probability of getting tails is {prob_tails:.2f}")

    # Prompt user for guess
    print("\n" + "=" * 30)
    print(f"FLIP {num_flips + 1}")
    print("=" * 30)
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
print(f'You correctly guessed {score} out of {num_flips} flips ({percentage_correct:.2f}%).')
