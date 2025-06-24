def find_animal_info(user_guess, animal_data_dictionary):
    """Checks if the user_guess exists as a key in the animal_data_dictionary.

    Args:
        user_guess (str): The animal typed by the user.
        animal_data_dictionary (dict): A dictionary containing all animal information.

    Returns:
        dict or None: The nested dictionary for the animal if found, otherwise None.
    """
    return animal_data_dictionary.get(user_guess) 