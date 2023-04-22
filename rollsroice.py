# Import random module
import random

# Initialize error message
error_message = 'Invalid input! See "Help" for information.\n'


# print_heading() function definition
def print_heading(text):
    print('~' * 50)
    print('|', text.center(46), '|')
    print('~' * 50, '\n')


# Print welcome message using function print_heading()
print_heading('Welcome to Rolls Roice!')

# Outermost while loop for main functionality of program
while True:
    # Initialize roll_results list for statistics
    roll_results = []

    # Initialize explode variable
    explode = False

    # Initialize response variable and get user input
    response = input('"h" for help, "x" to exit program \n'
                     'Enter a roll: ').lower()

    # Outermost if-elif-else statement
    if response == "h":
        # Tab escapes for formatting output
        print_heading('Help')
        print('Enter roll in "[quantity]d[sides] format." \n'
              'E.g., enter "4d6" to roll four six-sided dice.\n\n'
              'Add "!" to the end, e.g., "4d6!", for "exploding dice".\n'
              'Dice that roll max number are re-rolled and added.\n')
    # Prints a goodbye message and breaks the while loop, ending the program
    elif response == "x":
        # Tab escapes for formatting output
        print_heading('Goodbye!')
        break
    else:
        # Check if there is a "d" present in the string for splitting
        if response.count('d') != 1:
            print(error_message)
            continue

        # Check if there is a "!" within response string, signalling exploding dice
        if response[-1] == '!':
            explode = True
            response = response.replace('!', '')

        # Split response at "d" - making it a list
        response = response.split('d')

        # Check for valid user input post splitting of response
        if (not response[0].isdigit() or not response[1].isdigit()
                or int(response[0]) < 1 or int(response[1]) < 2):
            print(error_message)
            continue

        # Initialize quantity and sides variables post input validation
        quantity, sides = int(response[0]), int(response[1])

        print('Rolling a ', quantity, 'd', sides, '!', sep='')

        # Die rolling loop
        for i in range(quantity):
            roll = random.randint(1, sides)
            # Omit the following print statement if you find this annoying
            print('\tRolled a ', roll, '!', sep='')
            roll_results.append(roll)
            total = roll_results[-1]

            # Exploding die loop
            reroll = None
            while explode and roll == sides:
                reroll = random.randint(1, sides)
                total += reroll
                print('\t\tBOOM! Dice exploded!\n'
                      '\t\tRolled a ', reroll, '! \n \tCurrent total is: ', total, sep='')
                roll_results[-1] = total
                if reroll < sides:
                    break

        # Print Roll Statistics banner
        print_heading('Roll Statistics')

        # Variables for statistics, better readability in the following print statement
        roll_sum = int(sum(roll_results))
        roll_avg = round(roll_sum / quantity, 2)
        roll_min, total_min_rolls = min(roll_results), roll_results.count(min(roll_results))
        roll_max, total_max_rolls = max(roll_results), roll_results.count(max(roll_results))

        # Multi-line print statement for the roll statistics
        print(f'Rolls: {roll_results}\n'
              f'Total of all dice rolls: {roll_sum}\n'
              f'Average of all dice rolls: {roll_avg}\n'
              f'Minimum dice roll: {roll_min}. This had {total_min_rolls} occurrences.\n'
              f'Maximum dice roll: {roll_max}. This had {total_max_rolls} occurrences.\n'
              )
