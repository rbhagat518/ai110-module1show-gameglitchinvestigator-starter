# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose:
This was a simple streamlit geuss the number game. Core logic is to guess the number between (1-100 for normal mode) in the fewest attempts. the final reward is based off one's performance.

- [ ] Detail which bugs you found.
Scoring logic didnt make any sense.
hint was hard coded to go lower.
game state isn't reset upon success.
- [ ] Explain what fixes you applied.
With the help of copilot, I was able to update the core functionality for scoring. game state, and accurate hints. Additonally, I refactored the code to be moved into the game logic file for improved clarity.

## 📸 Demo
![Descriptive alt text](./success.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
