# War General for Clash of Clans
# Author: Patrick Mejia

# Created project, so I could check all stats of
# clash of clans army and design strats based off stats

import pandas as pd


def intro(name):
    print(f'Hi, {name}')
    print('This is a troop calculator I created when I was bored.\n'
          'It checks the stats of each troop and creates the strongest'
          'army based off your troop count and strats.\n')


# Adds troop to the army
def add_troop(troop, num_troops, space, army, df, level):
    troop_space = parse_troop_stats(df,level, troop)
    total_space = space + (int(num_troops) * int(troop_space))
    army = {troop:num_troops}
    print(f"Total Troop Space: {total_space} || Troops: {army}")
    print()
    return total_space


# Adds troop to the army
def remove_troop(troop, num_troops, space, army, df, level):
    troop_space = parse_troop_stats(df,level, troop)
    total_space = space - (num_troops * troop_space)
    army.append(troop)
    print(f"Total Troop Space: {total_space} Troops:{army}")
    return total_space


# Parses troop stats and creates a troop dictionary
# Parameters: dataframe, level
# Returns the stats of all the troops by the user level
def parse_troop_stats(df, user_level, troop_name):
    for index, row in df.iterrows():
        name = troop_name
        damage,speed = str(row[6]),str(row[3])
        health, level, housingSpace = str(row[4]), str(row[1]), str(row[2])
        if user_level == level:
            troop = {
                'Troop Name': name,
                'Speed': speed,
                'Damage': damage,
                'Hitpoints': health,
                'HousingSpace': housingSpace,
                'Level': level,
            }
            # print(troop)
            return troop['HousingSpace']


# Dataframe for the troop CSV file
df_troop = pd.read_csv('/Users/pmejia/PycharmProjects/WarGeneral/Troops.csv')
names_troops = df_troop['Name']

# instantiates the total army camp space and camp size
total_space, camp_size = 0, 240
army_troops = []

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
        parse_troop_stats(df_troop, user_level, user_troop)

    if choice == 'army':
        user_level = input("What is your troop level \n")
        print(f"Troop Level: {user_level}")
        print(f"Current Army Camp: ", f"Current Army total: {total_space}/{camp_size}")

        if camp_size > total_space:
            user_troop = input("Which troop would you like to add. \n")
            print(f'You selected {user_troop}')
            num_troops = input("How many troops would you like to add to your camp? \n")
            print(f'You selected to add {num_troops} {user_troop} troops.')

            parse_troop_stats(df_troop, user_level, user_troop)
            add_troop(user_troop,num_troops,total_space,army_troops, df_troop, user_level)
    if choice == 'a':
        if camp_size > total_space:
            user_level, num_troops, user_troop = 5, 5, 'Archer'

    else:
        print("Army camp:")
