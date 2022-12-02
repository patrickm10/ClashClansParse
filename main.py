# War General for Clash of Clans
# Author: Patrick Mejia

# Created project, so I could check all stats of
# clash of clans army and design strats based off stats
import csv

import pandas as pd


def intro(name):
    print(f'Hi, {name}')
    print('This is a troop calculator I created when I was bored.\n'
          'It checks the stats of each troop and creates the strongest'
          'army based off your troop count and strats.\n')


# Adds troop to the army
def add_troop(troop, num_troops,space, army, df, level):
    global total_space
    total_space = space + (int(num_troops) * int(troop_space))
    print(num_troops, troop_space)
    added_troops = {troop:num_troops}
    army.update(added_troops)
    print(f"Total Troop Space: {total_space} || Troops: {army}")
    print()
    return total_space


# Adds troop to the army
def remove_troop(troop, num_troops, space, army, df, level):
    global total_space
    total_space = space - (num_troops * troop_space)
    army.append(troop)
    print(f"Total Troop Space: {total_space} Troops:{army}")
    return total_space


# Parses troop stats and creates a troop dictionary
# Parameters: dataframe, level
# Returns the stats of all the troops by the user level
def parse_troop_stats(file):
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)


# Dataframe for the troop CSV file
df_troop = '/Users/pmejia/PycharmProjects/WarGeneral/Troops.csv'

# instantiates the total army camp space and camp size
camp_size = 240
total_space = 0
army_troops = {}

# Main loop
if __name__ == '__main__':
    intro('Patrick')
    # Gives user option to design army or see stats
    choice = input("Would you like to see the stat troops or design an army? Enter 'army' or 'stats'. \n")
    if choice == 'stats':
        user_level = input("What is your troop level \n")
        print('Your level is: ',user_level)
        user_troop = input("Which troop's stats would you like to see. \n")
        print(f'You selected {user_troop}')
        troop = parse_troop_stats(df_troop)
        print(troop)
    if choice == 'army':
        # Gets users troop level
        user_level = input("What is your troop level \n")
        print(f"Troop Level: {user_level}")
        print(f"Current Army Camp: ", f"Current Army total: 0/{camp_size}")

        # Loop for picking troops
        while camp_size > total_space:
            user_troop = input("Which troop would you like to add. \n")
            print(f'You selected {user_troop}')
            num_troops = input("How many troops would you like to add to your camp? \n")
            print(f'You selected to add {num_troops} {user_troop} troops.')

            troop_space = parse_troop_stats(df_troop, user_level, user_troop)
            troop = add_troop(user_troop,num_troops,total_space,army_troops, df_troop, user_level)

    # Shortcut
    # if choice == 'a':
    #     user_level, num_troops, user_troop = 5, 5, 'Archer'
    #     if camp_size > total_space:
    #         parse_troop_stats(df_troop, user_level, user_troop)
    #         add_troop(user_troop, num_troops, total_space, army_troops, df_troop, user_level)
