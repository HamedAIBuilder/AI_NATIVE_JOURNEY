class User:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.coins = 0

    def add_score(self, points):
        self.score += points
        self.coins += points // 10  # 1 coin per 10 points

    def reset(self):
        self.score = 0
        self.coins = 0

    def __str__(self):
        return f"{self.name} | Score: {self.score} | Coins: {self.coins}"

# --- User Profile Management ---
user_profile = {
    "coins": 0,
    "total_score": 0
}

def update_user_profile(coins, score):
    user_profile["coins"] += coins
    user_profile["total_score"] += score
    save_to_database(user_profile)

def save_to_database(data):
    # Placeholder: Replace with actual DB or file save
    print("Saving user data:", data)

def load_game(game_type, user=None):
    # game_type: 'tetris', 'snake', 'runner'
    print(f"Loading game: {game_type}")
    fetch_game_assets(game_type)
    setup_game_environment(game_type)
    start_game_loop(user)

def fetch_game_assets(game_type):
    print(f"Fetching assets for {game_type}...")

def setup_game_environment(game_type):
    print(f"Setting up environment for {game_type}...")

def start_game_loop(user=None):
    print("Starting game loop...")
    if user:
        import random
        # Simulate a game session
        points_earned = random.randint(50, 200)
        print(f"You earned {points_earned} points!")
        user.add_score(points_earned)
        print(f"Current stats: {user}")
        # Daily challenge evaluation
        check_challenge_progress(
            challenge_id="daily_score",
            game_type="arcade",
            event_data={"value": points_earned},
            user=user
        )
        # Update and save user profile
        update_user_profile(user.coins, user.score)
    else:
        print("No user tracking for this session.")

# --- Daily Challenge Functions ---
def check_challenge_progress(challenge_id, game_type, event_data, user=None):
    progress = get_current_progress(challenge_id)
    updated_progress = update_challenge_status(progress, event_data)

    if updated_progress.get("completed"):
        award_challenge_reward(updated_progress["reward"], user)

def get_current_progress(challenge_id):
    # Placeholder: In reality, this would come from a DB
    return {"progress": 40, "target": 50, "completed": False}

def update_challenge_status(progress, event_data):
    progress["progress"] += event_data.get("value", 0)
    if progress["progress"] >= progress["target"]:
        progress["completed"] = True
        progress["reward"] = 50  # Example: 50 coins
    return progress

def award_challenge_reward(reward, user=None):
    print(f"Awarded {reward} coins!")
    if user:
        user.coins += reward

if __name__ == "__main__":
    print("Welcome to PixelQuest Arcade!")
    user_name = input("Enter your player name: ")
    user = User(user_name)
    while True:
        print("\nChoose a game to play:")
        print("1. Tetris")
        print("2. Snake")
        print("3. Runner")
        print("4. View Stats")
        print("5. Exit")
        choice = input("Enter the number of your choice: ")
        game_types = {'1': 'tetris', '2': 'snake', '3': 'runner'}
        if choice in game_types:
            load_game(game_types[choice], user)
        elif choice == '4':
            print(f"\nPlayer Stats: {user}")
        elif choice == '5':
            print("Thanks for playing PixelQuest Arcade!")
            break
        else:
            print("Invalid choice. Try again.") 