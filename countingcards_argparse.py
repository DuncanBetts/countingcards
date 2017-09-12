# Inspired by:
# https://github.com/dbader/photosorter/blob/master/sorter.py
# https://github.com/dmerejkowsky/docopt-challenge

from argparse import ArgumentParser, RawDescriptionHelpFormatter
import sys


def parse_args(argv):
    parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
                            description="--------------------------------------------------\n"
                            "Keeps track of Lil's hand, round by round.\n"
                            "http://www.puzzlenode.com/puzzles/5-counting-cards\n"
                            "--------------------------------------------------"
                            )

    parser.add_argument('inputfile',
                        help=("File containing input. "
                              "Must be in current working directory."))

    parser.add_argument('-n', '--num-of-players',
                        default=4,
                        dest='playercount',
                        help="Number of players.")

    parser.add_argument('-p', '--your-player',
                        default='Rocky',
                        dest='mainplayer',
                        help="Your player name.")

    parser.add_argument('-c', '--name-of-colluder',
                        default='Lil',
                        dest='colluder',
                        help="Player you are colluding with.")

    parser.add_argument('-o', '--outputfile',
                        default="countingcards_output.txt",
                        help=("Filename to save output. "
                              "Will be written to current working directory."))

    args = parser.parse_args(argv)
    return args


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
