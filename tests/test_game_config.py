import pytest
from blackjack.game_config import GameConfig


def test_init_params():

    # num_decks must be positive int
    with pytest.raises(AssertionError):
        GameConfig(num_decks=None)
        GameConfig(num_decks=True)
        GameConfig(num_decks=[2])
        GameConfig(num_decks=(3))
        GameConfig(num_decks='4')
        GameConfig(num_decks='0')
        GameConfig(num_decks=-1)
        GameConfig(num_decks=0)
    GameConfig(num_decks=1)
    GameConfig(num_decks=2)
    GameConfig(num_decks=10)

    # reshuffle_threshold must be float or int between 0 and 1
    with pytest.raises(AssertionError):
        GameConfig(reshuffle_threshold=None)
        GameConfig(reshuffle_threshold=True)
        GameConfig(reshuffle_threshold=[0.2])
        GameConfig(reshuffle_threshold=(0.3))
        GameConfig(reshuffle_threshold='0.4')
        GameConfig(reshuffle_threshold='0')
        GameConfig(reshuffle_threshold=-1)
        GameConfig(reshuffle_threshold=3.14)
        GameConfig(reshuffle_threshold=2)
    GameConfig(reshuffle_threshold=0)
    GameConfig(reshuffle_threshold=0.25)
    GameConfig(reshuffle_threshold=0.33)
    GameConfig(reshuffle_threshold=0.5)
    GameConfig(reshuffle_threshold=1)

    # double_after_split must be a boolean
    with pytest.raises(AssertionError):
        GameConfig(double_after_split='True')
        GameConfig(double_after_split=None)
        GameConfig(double_after_split=0)
        GameConfig(double_after_split=[False])
        GameConfig(double_after_split=(False))
    GameConfig(double_after_split=True)
    GameConfig(double_after_split=False)

    # max_hands must be positive int
    with pytest.raises(AssertionError):
        GameConfig(max_hands=None)
        GameConfig(max_hands=True)
        GameConfig(max_hands=[2])
        GameConfig(max_hands=(3))
        GameConfig(max_hands='4')
        GameConfig(max_hands='0')
        GameConfig(max_hands=-1)
        GameConfig(max_hands=0)
    GameConfig(max_hands=1)
    GameConfig(max_hands=2)
    GameConfig(max_hands=10)

    # late_surrender must be a boolean
    with pytest.raises(AssertionError):
        GameConfig(late_surrender='True')
        GameConfig(late_surrender=None)
        GameConfig(late_surrender=0)
        GameConfig(late_surrender=[False])
        GameConfig(late_surrender=(False))
    GameConfig(late_surrender=True)
    GameConfig(late_surrender=False)
