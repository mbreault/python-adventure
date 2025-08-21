Welcome to the git repository for the Python 3 version of Adventure!

## API Enhancements

This fork adds two new API methods to the `adventure` module to make the game more accessible for programmatic use:

### `create_game(seed=None)`
Creates a new Adventure game instance ready for API use. Automatically starts the game and answers "no" to the instructions question.

```python
import adventure
game = adventure.create_game(seed=42)  # Optional seed for reproducible gameplay
```

### `send_command(game, command_string)`
Sends a command to the game and returns the response. Handles command parsing and conversion to the format expected by the game engine.

```python
response = adventure.send_command(game, "get lamp")
print(response)  # "OK"

response = adventure.send_command(game, "east")
print(response)  # Room description
```

### Example Usage

```python
import adventure

# Create a new game
game = adventure.create_game()

# Play programmatically
adventure.send_command(game, "get lamp")
adventure.send_command(game, "east")
adventure.send_command(game, "get keys")
adventure.send_command(game, "west")
```

These API methods enable:
- Automated testing of game scenarios
- AI/bot integration
- Game state analysis
- Integration with larger applications

The project README is one level deeper, inside of the package itself:

[adventure/README.txt](adventure/README.txt)
