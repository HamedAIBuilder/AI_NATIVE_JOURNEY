def display_animal_result(found_animal_info, user_guess):
    """Prints the result based on whether the animal was found.

    Args:
        found_animal_info (dict or None): A dictionary with animal data or None.
        user_guess (str): The animal the user guessed.
    """
    if found_animal_info:
        print("Hooray!")
        print(f"You chose a {user_guess}! Here's your animal: {found_animal_info['emoji']}")
        print(f"A {user_guess} says: {found_animal_info['sound']}")
    else:
        print("Hmm, I don't know that animal. Try one from the list!") 