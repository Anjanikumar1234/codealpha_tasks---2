import random
import time
import os

# ------------------ Word Bank ------------------
WORDS = {
    "Superheroes": [
        ("ironman", "Genius, billionaire, playboy, philanthropist"),
        ("spiderman", "Wall-crawling hero with spider sense"),
        ("captainamerica", "Super soldier, fights for justice"),
        ("thor", "God of Thunder, wields Mjolnir"),
        ("hulk", "Jekyll and Hyde with unlimited strength"),
        ("blackwidow", "Assassin with unmatched agility"),
        ("blackpanther", "King of Wakanda, fights with vibranium suit"),
        ("doctorstrange", "Master of the mystic arts"),
        ("deadpool", "Merc with a mouth, known for his healing factor"),
        ("antman", "Can shrink and grow, controls ants")
    ],
    "Cricket Players": [
        ("dhoni", "Known for his calmness under pressure and finishing matches with his helicopter shot"),
        ("kohli", "Known for his aggressive batting and consistency in all formats"),
        ("hardikpandya", "The all-rounder who is known for his explosive batting and quick bowling"),
        ("rohitsharma", "Known for his ability to score big centuries, including multiple double centuries"),
        ("yuzi_chahal", "A leg-spinner who plays a crucial role in limited overs cricket"),
        ("bhuvneshwar", "Known for swinging the ball both ways, particularly deadly with the new ball"),
        ("shami", "Pace bowler with a deadly seam position, particularly effective in Test cricket"),
        ("abdevilliers", "Known for his 360-degree batting and unorthodox shots across the field"),
        ("sky", "Has gained fame for his innovative stroke play and unorthodox shots in T20s"),
        ("davidwarner", "An explosive opener who is known for his aggressive batting in all formats")
    ],
    "Telugu Heroes": [
        ("prabhas", "Famous for his role in 'Baahubali', known for his action-packed performances"),
        ("pawan_kalyan", "Known as 'Power Star', famous for his political involvement and iconic films like 'Gabbar Singh'"),
        ("mahesh_babu", "Known as 'Prince', famous for his roles in 'Srimanthudu' and 'Bharat Ane Nenu'"),
        ("ntr", "Known for his intense performances, especially in 'Temper' and 'RRR'"),
        ("ram_charan", "Famous for his action roles in 'Magadheera' and 'RRR'"),
        ("allu_arjun", "Known as the 'Stylish Star', famous for his dance moves and roles in 'Ala Vaikunthapurramuloo'"),
        ("vijay_devarakonda", "Known for his breakthrough role in 'Arjun Reddy'"),
        ("sai_dhanshika", "Known for her versatile acting, primarily in action and thriller roles"),
        ("nani", "Famous for his natural acting style and hit films like 'Jersey' and 'Eega'"),
        ("siddharth", "Known for his roles in 'Rang De' and 'Aata', with his unique charm and versatile performances")
    ],
    "Movies": [
        ("arjunreddy", "A passionate and short-tempered surgeon spirals out of control after a heartbreak, leading to self-destruction."),
        ("rrr", "Two revolutionaries, one from India and one from the British Raj, unite to fight against the oppressive British rule."),
        ("baahubali", "The story of a warrior who seeks revenge and the mystery of his identity and heritage unfolds in a grand kingdom."),
        ("vikram", "A tough cop and a notorious criminal engage in a deadly cat-and-mouse chase, full of intense action and thrills."),
        ("master", "A college professor with a troubled past takes on a gang of criminals involved in child trafficking."),
        ("salaar", "A ruthless gangster seeks redemption as he fights to break free from his violent past while confronting enemies."),
        ("kgf", "A young man rises from poverty to become a powerful figure in a gold mining empire, taking on the corrupt system."),
        ("pellichoopulu", "Two strangers agree to a marriage proposal but soon realize that their personalities clash, leading to fun and chaos."),
        ("msdhoni", "The biographical story of MS Dhoni, focusing on his rise from a small town to becoming India’s most successful cricket captain."),
        ("chhichhore", "A group of middle-aged friends reunite and relive their college days, learning life lessons along the way."),
        ("eega", "A man is reincarnated as a housefly after being killed, and seeks revenge against the man who murdered him.")
    ]
}

MAX_ATTEMPTS = {
    'Easy': 8,
    'Medium': 6,
    'Hard': 4
}

# ------------------ Helper Functions ------------------
def load_scores():
    scores = {}
    if os.path.exists('scores.txt'):
        with open('scores.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                name = parts[0]
                wins = int(parts[1])
                losses = int(parts[2])
                games = int(parts[3])
                scores[name] = [wins, losses, games]
    return scores

def save_scores(scores):
    with open('scores.txt', 'w') as f:
        for player, (wins, losses, games) in scores.items():
            f.write(f"{player},{wins},{losses},{games}\n")

def display_hangman(tries_left):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
        ---------
        """
    ]
    index = min(len(stages) - 1, len(stages) - tries_left - 1)
    print(stages[index])

def get_random_word(category):
    word, hint = random.choice(WORDS[category])
    return word.lower(), hint

def provide_hint(word, guessed_letters):
    available = [c for c in word if c not in guessed_letters]
    if available:
        return random.choice(available)
    return None

# ------------------ Main Game ------------------
def play_game(player_name, scores):
    print("\nChoose category:")
    categories = list(WORDS.keys())
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    choice = input("Enter choice: ")
    
    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        category = categories[int(choice) - 1]
    else:
        print("Invalid choice. Defaulting to 'Movies'.")
        category = 'Movies'

    word, hint = get_random_word(category)
    word_display = ['_' for _ in word]
    guessed_letters = []
    attempts_left = MAX_ATTEMPTS['Medium']  # Defaulting to Medium difficulty
    wrong_guesses = 0
    hints_used = 0
    hint_limit = 3

    print(f"\nHint: {hint}\n")

    while attempts_left > 0 and '_' in word_display:
        print(f"\nWord: {' '.join(word_display)}")
        print(f"Guessed Letters: {', '.join(guessed_letters)}")
        print(f"Attempts Left: {attempts_left}")
        print(f"Hints Remaining: {hint_limit - hints_used}")

        guess = input("Guess a letter or full word or type 'hint': ").lower()

        if guess == 'hint':
            if hints_used < hint_limit:
                hint = provide_hint(word, guessed_letters)
                if hint:
                    print(f"🔔 HINT: Try the letter '{hint}'!")
                    hints_used += 1
                else:
                    print("No more hints available.")
            else:
                print("You've used all your hints!")
            continue

        if len(guess) == 1:
            if guess in guessed_letters:
                print("Already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess in word:
                for idx, char in enumerate(word):
                    if char == guess:
                        word_display[idx] = guess
                print("Good guess!")
            else:
                print("Wrong guess.")
                attempts_left -= 1
                wrong_guesses += 1
                display_hangman(attempts_left)

        elif len(guess) == len(word):
            if guess == word:
                word_display = list(word)
                print("Correct! You guessed the word!")
                break
            else:
                print("Wrong full word guess.")
                attempts_left -= 2
                wrong_guesses += 2
                display_hangman(attempts_left)
        else:
            print("Invalid input. Guess one letter or the full word.")

    if '_' not in word_display:
        print(f"🎉 Congratulations {player_name}! You guessed '{word}'!")
        scores[player_name][0] += 1
    else:
        print(f"Game Over! The word was '{word}'.")
        scores[player_name][1] += 1

    scores[player_name][2] += 1
    save_scores(scores)

def main():
    print("Welcome to the Hangman Game!")

    scores = load_scores()
    player_name = input("Enter your name: ").capitalize()

    if player_name not in scores:
        scores[player_name] = [0, 0, 0]  # [wins, losses, games]

    while True:
        print("\n1. Play Game\n2. View Scores\n3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            play_game(player_name, scores)
        elif choice == '2':
            print(f"\n{player_name}'s Score: Wins: {scores[player_name][0]}, Losses: {scores[player_name][1]}, Games Played: {scores[player_name][2]}")
        elif choice == '3':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
