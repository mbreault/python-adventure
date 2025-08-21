"""The Adventure game.

Copyright 2010-2015 Brandon Rhodes.  Licensed as free software under the
Apache License, Version 2.0 as detailed in the accompanying README.txt.

"""
import sys

if sys.version_info <= (3,):
    raise RuntimeError('Alas, Adventure requires Python 3 or later')

def load_advent_dat(data):
    import os
    from .data import parse

    datapath = os.path.join(os.path.dirname(__file__), 'advent.dat')
    with open(datapath, 'r', encoding='ascii') as datafile:
        parse(data, datafile)

def play(seed=None):
    """Turn the Python prompt into an Adventure game.

    With optional the `seed` argument the caller can supply an integer
    to start the Python random number generator at a known state.

    """
    global _game

    from .game import Game
    from .prompt import install_words

    _game = Game(seed)
    load_advent_dat(_game)
    install_words(_game)
    _game.start()
    print(_game.output[:-1])

def resume(savefile, quiet=False):
    global _game

    from .game import Game
    from .prompt import install_words

    _game = Game.resume(savefile)
    install_words(_game)
    if not quiet:
        print('GAME RESTORED\n')

# Simple API for programmatic use
def create_game(seed=None):
    """Create a new Adventure game instance for API use."""
    from .game import Game
    game = Game(seed)
    load_advent_dat(game)
    game.start()
    # Answer the instructions question with "no"
    game.do_command(['no'])
    return game

def send_command(game, command_string):
    """Send a command to the game and return the response."""
    import re
    words = re.findall(r'\w+', command_string.lower())
    if not words:
        return "I don't understand that command."
    return game.do_command(words)
