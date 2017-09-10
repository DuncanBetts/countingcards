# argparse usage pattern inspired by:
# https://github.com/dbader/photosorter/blob/master/sorter.py

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
                        help="File containing input")

    parser.add_argument('--outputfile',
                        required=False,
                        default="countingcards_output.txt",
                        help="File to send output to")

    args = parser.parse_args(argv)
    return args


def run(inputfile, outputfile):
    pass
    # call countingcards


def main(argv):
    args = parse_args(argv)
    run(args.inputfile, args.outputfile)
    return 0


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args)
