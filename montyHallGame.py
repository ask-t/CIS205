import random

# Define the game setup
doors = ['goat', 'goat', 'car']
random.shuffle(doors)
print('Welcome to the Monty Hall problem game!\n')
print('Behind one of these doors is a car, and behind the other two are goats.')
choice = int(input('\nChoose a door (1, 2, or 3): ')) - 1
# Host reveals a door with a goat
for i, door in enumerate(doors):
        if door == 'goat' and i != choice:
            revealed = i
            break
    
print(f"\nThe host reveals what's behind door {revealed + 1}: {doors[revealed]}\n")

switch = input('Do you want to switch your choice? (y/n): ') == 'y'


# Define the game function
def monty_hall_game(choice, switch):
    
    # If the player switches, choose the other unopened door
    if switch:
        for i, door in enumerate(doors):
            if i not in (choice, revealed):
                choice = i
                break
    # Determine if the player won or lost
    result = 'win' if doors[choice] == 'car' else 'lose'
    return result


result = monty_hall_game(choice, switch)

if result == 'win':
    print('Congratulations, you won the car!')
else:
    print('Sorry, you lost. Better luck next time!')
