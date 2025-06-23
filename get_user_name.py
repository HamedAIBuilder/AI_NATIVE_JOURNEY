def get_user_words():
    """
    Asks the user for a noun, a verb, and an adjective, and returns these words.

    Inputs:
        None

    Returns:
        tuple: A tuple containing three strings: (noun, verb, adjective).
               Each word will be stripped of leading/trailing whitespace.
    """
    print("\n--- Let's get some words for our silly story! ---")

    # Prompt for the noun and capture input
    noun = input("Please give me a noun (a person, place, or thing, like 'dog' or 'house'): ").strip()

    # Prompt for the verb and capture input
    verb = input("Please give me a verb (an action word, like 'run' or 'sing'): ").strip()

    # Prompt for the adjective and capture input
    adjective = input("Please give me an adjective (a describing word, like 'fluffy' or 'happy'): ").strip()

    print("Thanks for the words!")
    return noun, verb, adjective

def create_silly_story(noun, verb, adjective):
    """
    Creates and prints a silly story using the provided words.

    Inputs:
        noun (str): The noun to use in the story.
        verb (str): The verb to use in the story.
        adjective (str): The adjective to use in the story.

    Returns:
        None
    """
    print("\n--- Here is your silly story! ---")
    story = f"The {adjective} {noun} loves to {verb} all over the world."
    print(story)
    print(f"What a crazy {noun}!")


if __name__ == "__main__":
    my_noun, my_verb, my_adjective = get_user_words()
    create_silly_story(my_noun, my_verb, my_adjective) 