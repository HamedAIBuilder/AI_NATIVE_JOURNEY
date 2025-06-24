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
    # Add more songs here as needed
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
    return SONGS[song_title]

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

# 4. Orchestrator
def main_sing_along_loop():
    """
    Coordinates the sing-along experience.
    """
    print(f"{COLORS[0]}Welcome to 'Happy Voices Sing-Along!' 🎵🎤{RESET}")
    print(f"{COLORS[1]}Let's sing together and have fun!{RESET}\n")
    lyrics = load_song_lyrics()
    display_lyrics_with_pacing(lyrics)
    print(f"\n{COLORS[2]}You finished the song! You're a singing superstar! 🌈🎶{RESET}")

if __name__ == "__main__":
    main_sing_along_loop() 