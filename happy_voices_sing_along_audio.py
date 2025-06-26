import pygame
import time
import random
import os
import sys
from threading import Thread

# Initialize pygame mixer
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

class HappyVoicesSingAlong:
    def __init__(self):
        self.songs = {
            "Twinkle, Twinkle, Little Star": {
                "lyrics": [
                    "Twinkle, twinkle, little star,",
                    "How I wonder what you are!",
                    "Up above the world so high,",
                    "Like a diamond in the sky.",
                    "Twinkle, twinkle, little star,",
                    "How I wonder what you are!"
                ],
                "audio_file": "twinkle_twinkle.mp3",
                "tempo": 2.0  # seconds per line
            },
            "Row, Row, Row Your Boat": {
                "lyrics": [
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
                "audio_file": "row_row_boat.mp3",
                "tempo": 2.0
            },
            "Happy (Kid Version)": {
                "lyrics": [
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
                "audio_file": "happy.mp3",
                "tempo": 1.8
            },
            "Can't Stop the Feeling (Kid Version)": {
                "lyrics": [
                    "I got this feeling inside my bones,",
                    "It goes electric, wavey when I turn it on.",
                    "All through my city, all through my home,",
                    "We're flying up, no ceiling, when we in our zone.",
                    "",
                    "I got that sunshine in my pocket,",
                    "Got that good soul in my feet.",
                    "I feel that hot blood in my body when it drops,",
                    "I can't take my eyes up off it, moving so phenomenally."
                ],
                "audio_file": "cant_stop_feeling.mp3",
                "tempo": 1.5
            }
        }
        
        self.cheers = [
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
        
        self.colors = [
            '\033[95m',  # Magenta
            '\033[94m',  # Blue
            '\033[92m',  # Green
            '\033[93m',  # Yellow
            '\033[91m',  # Red
            '\033[96m',  # Cyan
            '\033[1m',   # Bold
        ]
        self.reset = '\033[0m'
        
        self.current_song = None
        self.is_playing = False
        self.audio_thread = None

    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_colored(self, text, color=None):
        """Print text with color"""
        if color is None:
            color = random.choice(self.colors)
        print(f"{color}{text}{self.reset}")

    def load_audio_file(self, audio_file):
        """Load and play audio file"""
        try:
            # Check if audio file exists
            if os.path.exists(audio_file):
                pygame.mixer.music.load(audio_file)
                pygame.mixer.music.play()
                return True
            else:
                print(f"Audio file not found: {audio_file}")
                print("Continuing without audio...")
                return False
        except Exception as e:
            print(f"Error loading audio: {e}")
            print("Continuing without audio...")
            return False

    def stop_audio(self):
        """Stop audio playback"""
        try:
            pygame.mixer.music.stop()
        except:
            pass

    def display_lyrics_with_audio(self, song_data):
        """Display lyrics synchronized with audio"""
        lyrics = song_data["lyrics"]
        audio_file = song_data["audio_file"]
        tempo = song_data["tempo"]
        
        # Start audio playback
        audio_playing = self.load_audio_file(audio_file)
        
        print(f"\n🎵 Now playing: {self.current_song} 🎵")
        print("=" * 50)
        
        for i, line in enumerate(lyrics):
            if not self.is_playing:
                break
                
            if line.strip() == "":
                # Empty line - shorter pause
                time.sleep(tempo * 0.5)
                continue
                
            # Display current line
            color = random.choice(self.colors)
            print(f"\n{color}🎤 {line}{self.reset}")
            
            # Show cheer after line
            cheer = random.choice(self.cheers)
            print(f"{color}   {cheer}{self.reset}")
            
            # Wait for next line
            time.sleep(tempo)
        
        # Stop audio when done
        if audio_playing:
            self.stop_audio()
        
        if self.is_playing:
            self.print_colored("\n🎉 Congratulations! You finished the song! You're a singing superstar! 🌈🎶", '\033[92m')
            self.print_colored("🎉 CONGRATULATIONS! 🎉", '\033[91m')

    def show_song_menu(self):
        """Display available songs menu"""
        print("\n🎵 Available Songs:")
        print("-" * 30)
        songs_list = list(self.songs.keys())
        for i, song in enumerate(songs_list, 1):
            print(f"{i}. {song}")
        print("0. Exit")
        print("-" * 30)

    def get_user_info(self):
        """Get user information for personalization"""
        print("🎵 Welcome to Happy Voices Sing-Along! 🎤")
        print("Let's get to know you before we start singing! 🌟")
        print()
        
        name = input("What's your name? 👋 ").strip()
        if not name:
            name = "Friend"
            
        while True:
            try:
                age = int(input("How old are you? 🎂 "))
                if 1 <= age <= 120:
                    break
                else:
                    print("Please enter a valid age between 1 and 120.")
            except ValueError:
                print("Please enter a valid number for age.")
        
        print("\nWhat type of songs do you like? 🎵")
        print("1. Nursery Rhymes 🍼")
        print("2. Pop Songs 🎤")
        print("3. All Songs 🌈")
        
        while True:
            try:
                genre_choice = int(input("Choose your favorite genre (1-3): "))
                if 1 <= genre_choice <= 3:
                    break
                else:
                    print("Please enter a number between 1 and 3.")
            except ValueError:
                print("Please enter a valid number.")
        
        return name, age, genre_choice

    def adjust_tempo_for_age(self, age):
        """Adjust song tempo based on user age"""
        if age < 5:
            return 1.5  # Slower for very young kids
        elif age < 8:
            return 1.2  # Medium pace for young kids
        elif age < 12:
            return 1.0  # Normal pace for older kids
        else:
            return 0.8  # Faster for teens and adults

    def run(self):
        """Main application loop"""
        self.clear_screen()
        
        # Get user information
        name, age, genre_choice = self.get_user_info()
        
        # Adjust tempo based on age
        tempo_multiplier = self.adjust_tempo_for_age(age)
        
        # Filter songs based on genre
        if genre_choice == 1:
            available_songs = ["Twinkle, Twinkle, Little Star", "Row, Row, Row Your Boat"]
        elif genre_choice == 2:
            available_songs = ["Happy (Kid Version)", "Can't Stop the Feeling (Kid Version)"]
        else:
            available_songs = list(self.songs.keys())
        
        # Update song tempos based on age
        for song_name in self.songs:
            self.songs[song_name]["tempo"] *= tempo_multiplier
        
        self.clear_screen()
        self.print_colored(f"Welcome back, {name}! Let's sing together and have fun! 🌟", '\033[94m')
        
        while True:
            self.show_song_menu()
            
            try:
                choice = int(input(f"\n{name}, choose a song to sing (0-{len(self.songs)}): "))
                
                if choice == 0:
                    self.print_colored(f"\nThanks for singing with us, {name}! Come back soon! 👋", '\033[92m')
                    break
                elif 1 <= choice <= len(available_songs):
                    self.current_song = available_songs[choice - 1]
                    song_data = self.songs[self.current_song]
                    
                    self.clear_screen()
                    self.print_colored(f"🎤 {name}, let's sing '{self.current_song}'! 🎵", '\033[95m')
                    
                    # Start singing
                    self.is_playing = True
                    self.display_lyrics_with_audio(song_data)
                    
                    # Ask if user wants to continue
                    continue_choice = input(f"\n{name}, want to sing another song? (y/n): ").lower()
                    if continue_choice not in ['y', 'yes']:
                        self.print_colored(f"\nThanks for singing with us, {name}! Come back soon! 👋", '\033[92m')
                        break
                    
                    self.clear_screen()
                else:
                    print("Invalid choice. Please try again.")
                    
            except ValueError:
                print("Please enter a valid number.")
            except KeyboardInterrupt:
                self.print_colored(f"\n\nThanks for singing with us, {name}! Come back soon! 👋", '\033[92m')
                break

def main():
    """Main function to run the application"""
    try:
        app = HappyVoicesSingAlong()
        app.run()
    except KeyboardInterrupt:
        print("\n\nGoodbye! 👋")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up pygame
        pygame.mixer.quit()
        pygame.quit()

if __name__ == "__main__":
    main() 