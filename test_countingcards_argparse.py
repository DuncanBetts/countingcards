"""
Unit tests for countingcards.py

Run with:

$ pytest

"""

import countingcards_argparse

import pytest


def parse(cmd=""):
    return countingcards_argparse.parse_args(cmd.split())


def test_help():
    with pytest.raises(SystemExit) as e:
        parse("--help")
    assert e.value.code == 0


def test_parse_blank_input(capsys):
    """
    Ensure sensible message returned if no input file provided.
    """
    with pytest.raises(SystemExit) as excinfo:
        parse()
    assert excinfo.value.code == 2
    out, err = capsys.readouterr()
    assert 'the following arguments are required' in err
    assert out == ''


def test_parse_blank_input_and_provided_output(capsys):
    """
    Ensure sensible message returned if no input file provided,
    whilst output file is provided.
    """
    outputfile = "bar.txt"
    with pytest.raises(SystemExit) as excinfo:
        parse("--outputfile {}".format(outputfile))
    assert excinfo.value.code == 2
    out, err = capsys.readouterr()
    assert 'the following arguments are required' in err
    assert out == ''

def test_parse_input_and_output():
    """
    Ensure both an input and output filename are captured when passed at runtime.
    """
    inputfile = "foo.txt"
    outputfile = "bar.txt"
    args = parse("{} --outputfile {}".format(inputfile, outputfile))
    assert args.inputfile == inputfile
    assert args.outputfile == outputfile


def test_parse_input_and_blank_output():
    """
    Ensure input filename is captured when passed at runtime,
    and if no output filename provided, default is used.
    """
    inputfile = "foo.txt"
    defaultoutputfile = "countingcards_output.txt"
    args = parse(inputfile)
    assert args.inputfile == inputfile
    assert args.outputfile == defaultoutputfile
