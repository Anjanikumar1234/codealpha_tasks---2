# Hangman Game

📌 **Description**  
This is a Python-based Hangman game featuring multiple categories of words including Superheroes, Cricket Players, Telugu Heroes, and Movies. Players guess letters or full words to reveal the hidden word, with hints available to assist. The game tracks player scores (wins, losses, games played) and displays a classic ASCII art hangman based on the number of wrong guesses.

🛠 **Installation**  
To run this project, ensure you have Python installed. You can download it from:  
🔗 [Python Official Website](https://www.python.org/downloads/)

No additional dependencies are required as the game uses only Python's standard library.

🚀 **How to Run**  
Run the game using the command:

```bash
python hangman.py
```

You will be prompted to enter your name and then presented with a menu to:  
1️⃣ Play the game  
2️⃣ View your scores  
3️⃣ Exit the game

During gameplay, you can guess letters, attempt the full word, or type 'hint' to receive a letter hint (limited to 3 per game).

📊 **Example Runs**

Example 1 - Playing a Game  
```
Welcome to the Hangman Game!
Enter your name: Alice

1. Play Game
2. View Scores
3. Exit
Enter choice: 1

Choose category:
1. Superheroes
2. Cricket Players
3. Telugu Heroes
4. Movies
Enter choice: 4

Hint: The story of a warrior who seeks revenge and the mystery of his identity and heritage unfolds in a grand kingdom.

Word: _ _ _ _ _ _ _ _ _
Guessed Letters: 
Attempts Left: 6
Hints Remaining: 2
Guess a letter or full word or type 'hint': a
Good guess!
...
```

Example 2 - Viewing Scores  
```
Enter choice: 2
Alice's Score: Wins: 3, Losses: 1, Games Played: 4
```

⏳ **Key Features**  
✅ Multiple word categories with hints  
✅ Guess letters or full words  
✅ Limited hints per game to assist players  
✅ ASCII art hangman display reflecting wrong guesses  
✅ Persistent player scores saved to file  
✅ Simple text-based interface for easy play

🤝 **Contributing**  
Want to improve this project? Feel free to:  
🔹 Fork the repository  
🔹 Create a new branch  
🔹 Submit a pull request  

Your contributions are always welcome! 😊
