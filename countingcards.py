import sys
import os
import linecache

from countingcards_argparse import parse_args

current_dir = os.getcwd()

player_hands = {}


def get_players(inp_file, playercount):
    players = {}
    for player_num in range(1, playercount+1):
        line = linecache.getline(inp_file, player_num)
        player_name = line.split(' ')[0]
        players[player_num] = player_name

    return players


def initial_hands(inp_file, players):

    def get_hand(inp_file, player):
        """
        Defined here in attempt to avoid implicit
        reliance on external function.
        """
        hand = linecache.getline(inp_file, player)
        hand = hand.strip('\n')
        hand = hand.split(' ')
        hand = hand[1:]

        return hand

    hands = {}

    for player in players:
        hand = get_hand(inp_file, player)
        player_name = players[player]
        hands[player_name] = {'Round 1': hand}

    return hands


def run(args):
    inp_file = os.path.join(current_dir, args.inputfile)

    players = get_players(inp_file, args.playercount)

    player_hands = initial_hands(inp_file, players)

    print(player_hands['Lil']['Round 1'])


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    run(args)
