import time
from datetime import datetime
import random

# ANSI color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def get_time_based_greeting():
    """Get greeting based on actual time of day"""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

def validate_name(name):
    """Validate the name input"""
    if not name.strip():
        return False
    if len(name) > 50:
        return False
    return True

def get_lunch_response():
    """Get and process lunch information"""
    lunch = input(f"{Colors.BLUE}What did you have for lunch today? {Colors.ENDC}")
    if not lunch.strip():
        return "You haven't had lunch yet? Don't forget to eat!"
    
    # Add some fun responses based on common lunch items
    lunch = lunch.lower()
    if "pizza" in lunch:
        return f"Pizza is always a great choice! 🍕"
    elif "sandwich" in lunch or "burger" in lunch:
        return f"Classic lunch choice! Hope it was delicious! 🍔"
    elif "salad" in lunch:
        return f"Healthy choice! Your body will thank you! 🥗"
    elif "sushi" in lunch:
        return f"Fancy lunch! Love the choice! 🍱"
    else:
        return f"Hope your {lunch} was delicious! 😋"

def get_welcome_message():
    # Get the user's name with validation
    while True:
        name = input(f"{Colors.BLUE}Please enter your name: {Colors.ENDC}")
        if validate_name(name):
            break
        print(f"{Colors.RED}Invalid name. Please try again.{Colors.ENDC}")
    
    # Get the user's mood
    moods = ["happy", "excited", "tired", "energetic", "relaxed"]
    print(f"\n{Colors.YELLOW}How are you feeling today?{Colors.ENDC}")
    print("Options:", ", ".join(moods))
    mood = input(f"{Colors.BLUE}Enter your mood: {Colors.ENDC}").lower()
    
    # Get lunch information
    print(f"\n{Colors.YELLOW}Let's talk about lunch!{Colors.ENDC}")
    lunch_response = get_lunch_response()
    
    # Get time-based greeting
    time_greeting = get_time_based_greeting()
    
    # Create a personalized greeting
    greeting = f"{Colors.GREEN}{time_greeting}, {name}!{Colors.ENDC}\n"
    
    # Add mood-based message
    if mood in moods:
        mood_messages = {
            "happy": "It's wonderful to see you in such good spirits!",
            "excited": "Your excitement is contagious!",
            "tired": "Hope you get some rest soon!",
            "energetic": "Your energy is inspiring!",
            "relaxed": "Enjoy your peaceful state of mind!"
        }
        greeting += f"{Colors.YELLOW}{mood_messages[mood]}{Colors.ENDC}\n"
    else:
        greeting += f"{Colors.YELLOW}Hope you're having a great day!{Colors.ENDC}\n"
    
    # Add lunch response
    greeting += f"{Colors.GREEN}{lunch_response}{Colors.ENDC}\n"
    
    # Add current time
    current_time = datetime.now().strftime("%I:%M %p")
    greeting += f"{Colors.BLUE}Current time: {current_time}{Colors.ENDC}"
    
    return greeting

def display_welcome_banner():
    """Display a fancy welcome banner"""
    banner = f"""
{Colors.HEADER}{Colors.BOLD}
╔══════════════════════════════════════╗
║         Welcome to Greeting          ║
║         Your Personal Greeter        ║
╚══════════════════════════════════════╝{Colors.ENDC}
"""
    print(banner)

def main():
    display_welcome_banner()
    
    # Get and display the welcome message
    welcome_message = get_welcome_message()
    
    # Add a small delay for dramatic effect
    print("\nGenerating your personalized greeting", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")
    
    print("\n" + "=" * 50)
    print(welcome_message)
    print("=" * 50)
    
    # Farewell message
    print(f"\n{Colors.GREEN}Thank you for using the Greeting Program!{Colors.ENDC}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Program terminated by user.{Colors.ENDC}")
    except Exception as e:
        print(f"\n{Colors.RED}An error occurred: {str(e)}{Colors.ENDC}") 