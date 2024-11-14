# Arcade Slot Machine Game 🎰

This is a simple arcade-style slot machine game built in Python. Players spin the machine and try to match symbols to win tickets!

## How to Play

1. Run the game by executing `main.py`.
2. Press Enter to spin the slot machine.
3. Match symbols to earn tickets:
   - **3 symbols match:** You win **50 tickets** 🎟️
   - **2 symbols match:** You win **10 tickets** 🎟️
4. After each spin, you'll be prompted to play again. Type `Yes` to continue or `No` to exit.

## Project Structure

- **arcade.py**: Contains the game’s core functions, including:
  - `spin_column`: Generates a random symbol.
  - `get_score`: Calculates the score based on symbol matches.
  - `draw_display`: Displays the current spin results.
  - Helper functions for checking symbol matches.
- **main.py**: Main script for running the game.

## Symbols

The slot machine displays these symbols:
- `*` - Star
- `$` - Dollar
- `?` - Question mark
- `@` - At symbol

## Requirements

- Python 3.x

## Running the Game

To play the game, run the following command:

```bash
python main.py
```

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
