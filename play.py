#!/usr/bin/env python3
"""Play Adventure on the command line"""

import adventure

# Create and start the game
game = adventure.create_game()

print("Welcome to Adventure! Type commands or 'quit' to exit.")
print("=" * 50)

# Main game loop
while True:
    try:
        # Get user input
        command = input("> ").strip()

        if command.lower() in ['quit', 'q', 'exit']:
            print("Thanks for playing!")
            break

        if command:
            # Send command to game and print response
            response = adventure.send_command(game, command)
            print(response)

    except KeyboardInterrupt:
        print("\nThanks for playing!")
        break
    except EOFError:
        print("\nThanks for playing!")
        break