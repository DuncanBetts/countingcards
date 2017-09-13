"""
Unit tests for countingcards_parse_input.py

Run with:
$ pytest test_countingcards_parse_input.py

"""
from countingcards_parse_input import _get_hands, _get_signals
from test_samples import (
    SAMPLE_INITIAL_HANDS,
    SAMPLE_ROUND_DICT,
    SAMPLE_SIGNAL_ONLY_ROUND_DICT,
    SAMPLE_ROUND_2_SIGNALS
)


def test_get_initial_hands():
    initial_hands = _get_hands(SAMPLE_ROUND_DICT, round_n=1, playercount=4)
    assert initial_hands == SAMPLE_INITIAL_HANDS


def test_get_round_2_signals():
    round_2_signals = _get_signals(SAMPLE_SIGNAL_ONLY_ROUND_DICT, round_n=2)
    assert round_2_signals == SAMPLE_ROUND_2_SIGNALS
