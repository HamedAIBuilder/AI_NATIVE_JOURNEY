import time

def welcome_and_quiz(name):
    """
    Greets the user and asks some humorous questions.

    Args:
        name (str): The name of the person.
    """
    print(f"Hello, {name}! Welcome to this very serious and important program.")
    time.sleep(1)
    print("To proceed, we must ask a few security questions.")
    time.sleep(1)

    answer1 = input("What is the air-speed velocity of an unladen swallow? ")
    if "african or european" in answer1.lower():
        print("I... I don't know that! *flings you into the gorge of eternal peril*")
    else:
        print("Hmm, an interesting, but ultimately incorrect answer.")
    
    time.sleep(1)

    answer2 = input(f"Next question, {name}. What is your favorite AI Copilot Programme ? ")
    print(f"'{answer2.capitalize()}'? Right then. Off you go.")
    
    time.sleep(1)
    
    # New interactive questions
    answer3 = input(f"Alright {name}, serious question: Coffee or Tea? ")
    if "coffee" in answer3.lower():
        print("Ah, a fellow caffeine addict! Your code will be fueled by pure determination.")
    elif "tea" in answer3.lower():
        print("A sophisticated choice! Your code will be as refined as your taste.")
    else:
        print("Water? Really? How do you stay awake during debugging sessions?")
    
    time.sleep(1)
    
    answer4 = input("What's your favorite programming language? ")
    if "python" in answer4.lower():
        print("Python! The language of choice for AI enthusiasts. Excellent taste!")
    elif "javascript" in answer4.lower():
        print("JavaScript! The language that runs everywhere, including your nightmares.")
    elif "java" in answer4.lower():
        print("Java! Write once, debug everywhere. Classic choice!")
    else:
        print(f"{answer4.capitalize()}? Interesting choice! At least it's not COBOL...")
    
    time.sleep(1)
    
    answer5 = input("Quick personality test: Are you a morning person or night owl? ")
    if "night" in answer5.lower() or "owl" in answer5.lower():
        print("Night owl! Perfect for those 3 AM debugging sessions when the code just won't work.")
    elif "morning" in answer5.lower():
        print("Morning person! You probably write your best code before the rest of us are even awake.")
    else:
        print("Somewhere in between? The mysterious middle-ground coder!")
    
    time.sleep(1)
    
    answer6 = input("Final question: What's your biggest coding pet peeve? ")
    print(f"'{answer6}'? Oh, that's definitely annoying! We feel your pain.")
    
    time.sleep(1)
    
    print(f"\n🎉 Congratulations {name}! You've successfully completed the most important interview of your life!")
    print("You are now officially certified as a 'Real Programmer' (whatever that means).")
    print("Welcome to the club, Sir Hamed Builder!")

# The personalized name is set
user_name = "Hamed Builder"

# Run the welcome and quiz
welcome_and_quiz(user_name) 