import os
import sys

from countingcards_argparse import parse_args
from countingcards_parse_input import parse_inputfile


def run(args):
    input_file = os.path.join(
        os.path.dirname(__file__),
        args.inputfile
    )

    game_data = parse_inputfile(input_file, args.playercount)

    # SCAFFOLDING
    print(game_data)


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    run(args)
