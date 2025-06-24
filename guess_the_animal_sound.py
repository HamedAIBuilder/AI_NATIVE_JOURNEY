def get_user_animal_choice(animal_list):
    """
    Asks the user for an animal and returns the cleaned input.
    The prompt includes the list of available animals and instructions on how to exit.
    """
    prompt = f"\nWhich animal sound do you want to hear? ({animal_list}, or type 'quit' to exit): "
    animal_choice = input(prompt)
    return animal_choice.lower().strip()

def get_animal_data():
    """Returns a dictionary containing information for the following animals: 
    dog, cat, cow, duck, lion, elephant, sheep, and pig.

    For each animal, the dictionary should store its sound and a relevant emoji.
    
    Returns:
        A dictionary containing animal data.
    """
    animal_data = {
        'dog': {'sound': 'Woof woof!', 'emoji': '🐶'},
        'cat': {'sound': 'Meow!', 'emoji': '🐱'},
        'cow': {'sound': 'Moo!', 'emoji': '🐮'},
        'duck': {'sound': 'Quack!', 'emoji': '🦆'},
        'lion': {'sound': 'Roar!', 'emoji': '🦁'},
        'elephant': {'sound': 'Toot!', 'emoji': '🐘'},
        'sheep': {'sound': 'Baa!', 'emoji': '🐑'},
        'pig': {'sound': 'Oink!', 'emoji': '🐷'}
    }
    return animal_data

def find_animal_info(user_guess, animal_data_dictionary):
    """Checks if the user_guess exists as a key in the animal_data_dictionary.

    Args:
        user_guess (str): The animal typed by the user.
        animal_data_dictionary (dict): A dictionary containing all animal information.

    Returns:
        dict or None: The nested dictionary for the animal if found, otherwise None.
    """
    return animal_data_dictionary.get(user_guess)

def display_animal_result(found_animal_info, user_guess):
    """Prints the result based on whether the animal was found.

    Args:
        found_animal_info (dict or None): A dictionary with animal data or None.
        user_guess (str): The animal the user guessed.
    """
    if found_animal_info:
        print("\nHooray!")
        # The user_guess is capitalized to make the output more readable
        print(f"You chose a {user_guess.capitalize()}! Here's your animal: {found_animal_info['emoji']}")
        print(f"A {user_guess.capitalize()} says: {found_animal_info['sound']}")
    else:
        print(f"\nHmm, I don't know '{user_guess}'. Why not try another animal?")

def main():
    """Main function to run the Guess the Animal Sound app."""
    print("Welcome to Guess the Animal Sound!")
    
    animal_data = get_animal_data()
    animal_list = ", ".join(animal_data.keys())

    while True:
        user_choice = get_user_animal_choice(animal_list)
        
        if user_choice == 'quit':
            print("\nThanks for playing! Goodbye!")
            break
        
        if not user_choice:
            continue

        found_animal = find_animal_info(user_choice, animal_data)
        
        display_animal_result(found_animal, user_choice)

if __name__ == "__main__":
    main() 