import csv
import numpy as np
import pandas as pd


def intro(name):
    print(f'Hi, {name}')
    print('This is a program to help you design your army camp for Clash of Clans. ' +
        'It is made to help you keep track of your army camp space and army damage. ' +
        'and a visyal representation of your army camp. ')
    

# TODO: Work on adding counter to the number of troops in the army
# and list the troops in the army in a dictionary
def add_troop(troop, num_troops, total_space, army):
    '''
    Adds a troop to the army
    :param troop: The troop to add
    :param num_troops: The number of troops to add
    :param total_space: The total space of the army
    :param army: The current army
    :return: The total space and the army
    '''
    troop_space = int(num_troops) * int(troop['space'])
    total_space += troop_space
    army[troop['name']] = num_troops
    print(f"Total Troop Space: {total_space} || Troops: {army}")
    return total_space, army

# TODO: Work on removing a troop from the army
# and list the troops in the army in a dictionary
def remove_troop(troop, num_troops, total_space, army):
    '''
    Removes a troop from the army
    :param troop: The troop to remove
    :param num_troops: The number of troops to remove
    :param total_space: The total space of the army
    :param army: The current army
    :return: The total space and the army
    '''
    troop_space = num_troops * troop['space']
    total_space -= troop_space
    del army[troop['name']]
    print(f"Total Troop Space: {total_space} Troops:{army}")
    return total_space, army

def parse_troop_stats(file):
    '''
    Parses the troop stats from a CSV file
    :param file: The file to parse
    :return: A list of troop stats
    '''
    try:
        df = pd.read_csv(file)
        return df.to_dict('records')
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def get_troop_by_name(troops, name):
    '''
    Gets a troop by name
    :param troops: The list of troops
    :param name: The name of the troop
    :return: The troop with the given name
    '''
    # Convert list of troops to DataFrame
    df = pd.DataFrame(troops)

    # Remove 'trooplevel' and 'isflying' columns
    df = df.drop(columns=['TroopLevel', 'IsFlying'])

    # Remove duplicates
    df = df.drop_duplicates(subset=['Name'])

    # If name is 'all', return all troops
    if name.lower() == 'all':
        return df.to_dict('records')

    # Otherwise, return the troop with the given name
    troop = df[df['Name'].str.lower() == name.lower()]
    return troop.to_dict('records') if not troop.empty else None

def main():
    '''
    Main function to run the program
    '''
    df_troop = 'Troops.csv'
    camp_size = 240
    total_space = 0
    army_troops = {}

    intro('Patrick')
    troops = parse_troop_stats(df_troop)
    sorted_troops = pd.DataFrame(troops)
    sorted_troops = sorted_troops.drop(columns=['TroopLevel', 'IsFlying'])
    sorted_troops = sorted_troops.drop_duplicates(subset=['Name'])
    sorted_troops = sorted_troops.sort_values(by=['Name'],ignore_index=True)
    print(f"Troops: {sorted_troops.to_string(index=False)}\n")
    print('****************************************************************************************************')
    
    actions = {
        'stats': show_stats,
        'army': design_army,
    }

    while True:
        choice = input("Would you like to see the stat troops, design an army or quit? Enter 'stats', 'army' or 'quit'. \n")
        if choice in actions:
            action = actions[choice]
            if choice == 'stats':
                user_troop_name = input("Which troop's stats would you like to see. \n")
                user_troop = get_troop_by_name(troops, user_troop_name)
                action(user_troop)
            elif choice == 'army':
                print(f"Current Army Camp: ", f"Current Army total: 0/{camp_size}")
                while camp_size > total_space:
                    user_troop_name = input("Which troop would you like to add. \n")
                    num_troops = input("How many troops would you like to add to your camp? \n")
                    user_troop = get_troop_by_name(troops, user_troop_name)
                    total_space, army_troops = action(user_troop, num_troops, total_space, army_troops)
        elif choice == 'quit' or choice == 'q':
            break
        else:
            print('Invalid choice')

def show_stats(troop):
    '''
    Shows the stats of a troop
    :param troop: The troop to show stats for
    '''
    print(troop)

def design_army(troop, num_troops, total_space, army):
    '''
    Designs an army
    :param troop: The troop to add
    :param num_troops: The number of troops to add
    :param total_space: The total space of the army
    :param army: The current army
    :return: The total space and the army
    '''
    return add_troop(troop, num_troops, total_space, army)

if __name__ == '__main__':
    main()