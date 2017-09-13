def _get_hands(gameplay_by_round, round_n, playercount):
    return_dict = {}
    for player in range(playercount):
        line = gameplay_by_round[round_n].pop(0)
        player_name, play_data = line[0], line[1:]
        return_dict[player_name] = play_data

    return return_dict


def _get_signals(gameplay_by_round, round_n):
    return_dict = {}
    signal_count = len(gameplay_by_round[round_n])
    for signal_num in range(1, signal_count+1):
        line = gameplay_by_round[round_n].pop(0)
        return_dict[signal_num] = line[1:]

    return return_dict


def file_to_dict(input_file):
    """
    Takes input text file, returns Python dictionary
    with gameplay split by round.
    """
    return_dict = {}

    with open(input_file) as f:
        lines = [line.rstrip('\n').split(' ') for line in f]
        round_n = 1
        signal_data = False

        for line in lines:
            if signal_data and (line[0] != '*'):
                signal_data = False
                round_n += 1

            if round_n in return_dict:
                return_dict[round_n].append(line)
            else:
                return_dict[round_n] = [line]

            if line[0] == '*':
                signal_data = True

    return return_dict


def format_gameplay(gameplay_by_round, playercount):
    """
    Take gameplay dictionary, split by round,
    and break down further into round subsections.
    """

    return_dict = {}

    for round_n in gameplay_by_round:
        return_dict[round_n] = {}
        if round_n == 1:
            return_dict[round_n]['Initial Hands'] = _get_hands(
                gameplay_by_round, round_n, playercount
            )

        return_dict[round_n]['Moves'] = _get_hands(
            gameplay_by_round, round_n, playercount
        )

        return_dict[round_n]['Signals'] = _get_signals(
            gameplay_by_round, round_n
        )

    return return_dict


def parse_inputfile(input_file, playercount):

    gameplay_by_round = file_to_dict(input_file)

    return format_gameplay(gameplay_by_round, playercount)

if __name__ == '__main__':
    # Debugging Only
    from test_samples import SAMPLE_ROUND_DICT
    SAMPLE_FILE_PATH = '/home/_/devel/py/countingcards/' \
        + 'SAMPLE_DATA/SAMPLE_INPUT.txt'
    PLAYER_COUNT = 4
    round_2_signals = _get_signals(SAMPLE_ROUND_DICT, 2)
    print(round_2_signals)
