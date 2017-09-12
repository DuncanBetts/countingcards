import os

import countingcards as cc


# Data Fixtures
SAMPLE_DATA_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'SAMPLE_DATA',
)

SAMPLE_INPUT = os.path.join(SAMPLE_DATA_DIR, 'SAMPLE_INPUT.txt')
SAMPLE_INPUT_2 = os.path.join(SAMPLE_DATA_DIR, 'SAMPLE_INPUT_2.txt')
SAMPLE_SOLUTION = os.path.join(SAMPLE_DATA_DIR, 'SAMPLE_SOLUTION.txt')
SAMPLE_SOLUTION_2 = os.path.join(SAMPLE_DATA_DIR, 'SAMPLE_SOLUTION_2.txt')

SAMPLE_PLAYER_NAMES = {1: 'Shady', 2: 'Rocky', 3: 'Danny', 4: 'Lil'}

SAMPLE_INITIAL_HANDS = {
    'Shady': {'Round 1': ['+??', '+??', '+??', '+??']},
    'Rocky': {'Round 1': ['+QH', '+KD', '+8S', '+9C']},
    'Danny': {'Round 1': ['+??', '+??', '+??', '+??']},
    'Lil':   {'Round 1': ['+8H', '+9H', '+JS', '+6H']},
}


def test_extract_player_names():
    players = cc.get_players(inp_file=SAMPLE_INPUT, playercount=4)
    player_names = players.values()
    for player in player_names:
        assert player in SAMPLE_PLAYER_NAMES.values()


def test_store_initial_hands():
    initial_hands = cc.initial_hands(inp_file=SAMPLE_INPUT, players=SAMPLE_PLAYER_NAMES)
    assert initial_hands == SAMPLE_INITIAL_HANDS
