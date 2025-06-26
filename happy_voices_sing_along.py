import time
import random
import sys

# ANSI color codes for fun, colorful output
COLORS = [
    '\033[95m',  # Magenta
    '\033[94m',  # Blue
    '\033[92m',  # Green
    '\033[93m',  # Yellow
    '\033[91m',  # Red
    '\033[96m',  # Cyan
    '\033[1m',   # Bold
]
RESET = '\033[0m'

# Key data: Songs and Cheers
SONGS = {
    "Twinkle, Twinkle, Little Star": [
        "Twinkle, twinkle, little star,",
        "How I wonder what you are!",
        "Up above the world so high,",
        "Like a diamond in the sky.",
        "Twinkle, twinkle, little star,",
        "How I wonder what you are!"
    ],
    "Row, Row, Row Your Boat": [
        "Row, row, row your boat,",
        "Gently down the stream.",
        "Merrily, merrily, merrily, merrily,",
        "Life is but a dream.",
        "",
        "Row, row, row your boat,",
        "Gently down the stream.",
        "If you see a crocodile,",
        "Don't forget to scream!"
    ],
    "Happy (Kid Version)": [
        "It might seem crazy what I'm about to say,",
        "Sunshine she's here, you can take a break.",
        "I'm a hot air balloon that could go to space,",
        "With the air, like I don't care, baby, by the way.",
        "",
        "Because I'm happy!",
        "Clap along if you feel like a room without a roof.",
        "Because I'm happy!",
        "Clap along if you feel like happiness is the truth."
    ],
    "Can't Stop the Feeling (Kid Version)": [
        "I got this feeling inside my bones,",
        "It goes electric, wavey when I turn it on.",
        "All through my city, all through my home,",
        "We're flying up, no ceiling, when we in our zone.",
        "",
        "I got that sunshine in my pocket,",
        "Got that good soul in my feet.",
        "I feel that hot blood in my body when it drops,",
        "I can't take my eyes up off it, moving so phenomenally."
    ]
}

CHEERS = [
    "Awesome singing! 🎉",
    "You rock! 🌟",
    "Superstar performance! ✨",
    "Keep it up! 😃",
    "Bravo! 👏",
    "That was magical! 🪄",
    "Sing it loud, sing it proud! 🎤",
    "You make the song shine! ☀️",
    "Fantastic job! 🥳",
    "Way to go! 🚀"
]

# 1. Get Ready, Get Set, Lyrics!
def load_song_lyrics(song_title=None):
    """
    Loads the lyrics for the sing-along from the SONGS dictionary.
    If song_title is None, uses the first song.
    """
    if song_title is None:
        # Default to the first song in the dictionary
        song_title = list(SONGS.keys())[0]
    return SONGS.get(song_title, SONGS[list(SONGS.keys())[0]])

# 2. Happy Cheer Squad!
def generate_cheer():
    """
    Returns a random, encouraging cheer for the singer from the CHEERS list.
    """
    return random.choice(CHEERS)

# 3. Sing-Along Display & "Just Right" Pacing Pal
def display_lyrics_with_pacing(lyrics_list, pause_seconds=2):
    """
    Displays each lyric line with a child-friendly pause and colorful output.
    """
    for idx, line in enumerate(lyrics_list):
        color = random.choice(COLORS)
        print(f"{color}{line}{RESET}")
        time.sleep(pause_seconds)
        # Sprinkle in a cheer after every line
        cheer = generate_cheer()
        print(f"{color}{cheer}{RESET}")
        time.sleep(1.2)

# 4. Show available songs
def show_song_menu():
    """
    Displays the available songs menu.
    """
    print("\n🎵 Available Songs:")
    print("-" * 30)
    songs_list = list(SONGS.keys())
    for i, song in enumerate(songs_list, 1):
        print(f"{i}. {song}")
    print("0. Exit")
    print("-" * 30)

# 5. Get user choice
def get_user_choice():
    """
    Gets the user's song choice with validation.
    """
    while True:
        try:
            choice = int(input("Choose a song (0-{}): ".format(len(SONGS))))
            if 0 <= choice <= len(SONGS):
                return choice
            else:
                print("Please enter a number between 0 and {}.".format(len(SONGS)))
        except ValueError:
            print("Please enter a valid number.")

# 6. Orchestrator
def main_sing_along_loop():
    """
    Coordinates the sing-along experience with song selection.
    """
    print(f"{COLORS[0]}Welcome to 'Happy Voices Sing-Along!' 🎵🎤{RESET}")
    print(f"{COLORS[1]}Let's sing together and have fun!{RESET}\n")
    
    while True:
        show_song_menu()
        choice = get_user_choice()
        
        if choice == 0:
            print(f"\n{COLORS[2]}Thanks for singing with us! Come back soon! 👋{RESET}")
            break
        
        # Get the selected song
        song_title = list(SONGS.keys())[choice - 1]
        lyrics = load_song_lyrics(song_title)
        
        print(f"\n{COLORS[3]}🎤 Now singing: {song_title} 🎵{RESET}")
        print("=" * 50)
        
        display_lyrics_with_pacing(lyrics)
        
        print(f"\n{COLORS[2]}You finished the song! You're a singing superstar! 🌈🎶{RESET}")
        
        # Ask if user wants to continue
        continue_choice = input("\nWant to sing another song? (y/n): ").lower()
        if continue_choice not in ['y', 'yes']:
            print(f"\n{COLORS[2]}Thanks for singing with us! Come back soon! 👋{RESET}")
            break

if __name__ == "__main__":
    try:
        main_sing_along_loop()
    except KeyboardInterrupt:
        print(f"\n{COLORS[1]}Goodbye! 👋{RESET}")
    except Exception as e:
        print(f"\n{COLORS[4]}An error occurred: {e}{RESET}") 