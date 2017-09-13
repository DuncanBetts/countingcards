SAMPLE_INITIAL_HANDS = {
    'Lil': ['+8H', '+9H', '+JS', '+6H'],
    'Shady': ['+??', '+??', '+??', '+??'],
    'Danny': ['+??', '+??', '+??', '+??'],
    'Rocky': ['+QH', '+KD', '+8S', '+9C']
}

SAMPLE_ROUND_DICT = {1: [
    ['Shady', '+??', '+??', '+??', '+??'],
    ['Rocky', '+QH', '+KD', '+8S', '+9C'],
    ['Danny', '+??', '+??', '+??', '+??'],
    ['Lil', '+8H', '+9H', '+JS', '+6H'],
    ['Shady', '-QD:discard', '-2S:discard'],
    ['Rocky', '-KD:Shady', '+7H'],
    ['Danny', '-QC:Rocky', '+??', '+??'],
    ['Lil', '-6H:Rocky', '-??:Shady', '-8H:discard',
     '+??', '-10S:discard', '+??'],
    ['*', '-JS:Shady', '+10S', '+QS']
], 2: [
    ['Shady', '+KD:Rocky', '+??:Lil', '-KD:discard', '-??:Lil'],
    ['Rocky', '+QC:Danny', '+6H:Lil', '-9C:Danny',
     '-6H:discard', '-7H:discard', '+3D', '+3H'],
    ['Danny', '+9C:Rocky', '-AD:discard', '+??'],
    ['Lil', '+??:Shady', '+??', '-??:Danny', '-??:Shady', '+??'],
    ['*', '+AH:Shady', '+8D', '-8D:Danny', '-QS:Shady', '+8C']
], 3: [
    ['Shady', '+??:Lil', '-7S:discard', '+??', '-10H:discard'],
    ['Rocky', '-QH:Lil', '+5D', '-8S:Shady', '-3H:discard', '-QC:discard'],
    ['Danny', '+??:Lil', '+??', '+??', '-??:Lil', '-3S:Rocky', '-??:Shady'],
    ['Lil', '+QH:Rocky', '+??:Danny', '-AH:Rocky', '-QH:discard'],
    ['*', '+4D:Danny']
], 4: [
    ['Shady', '+8S:Rocky', '+??:Danny', '-JS:discard',
     '+??', '+??', '+??', '+??'],
    ['Rocky', '+3S:Danny', '+AH:Lil', '+AS', '+4H'],
    ['Danny', '-10D:discard', '+??', '-6S:discard',
     '-JC:discard', '-8D:discard'],
    ['Lil', '-8C:discard', '-??:Shady', '+??', '-??:Danny'],
    ['*', '-4D:Shady', '+KH', '-KH:Danny']
], 5: [
    ['Shady', '+??:Lil', '-??:Danny', '+??', '-2H:discard'],
    ['Rocky', '+5C', '-5D:discard', '+3C', '-3D:discard',
     '-5C:discard', '+KS'],
    ['Danny', '+??:Lil', '+??:Shady', '-??:Lil', '-6D:discard', '+??'],
    ['Lil', '+??:Danny', '-??:Shady', '-??:Danny'],
    ['*', '+KH:Danny', '-9H:Shady', '-KH:Danny']
]}

# I am using this, because the individual functions are reliant on each
# other whilst processing the data - as I am using pop to remove
# items as I work through the round dict.
SAMPLE_SIGNAL_ONLY_ROUND_DICT = {
    1: [ ['*', '-JS:Shady', '+10S', '+QS'] ],
    2: [ ['*', '+AH:Shady', '+8D', '-8D:Danny', '-QS:Shady', '+8C'] ],
    3: [ ['*', '+4D:Danny'] ],
    4: [ ['*', '-4D:Shady', '+KH', '-KH:Danny'] ],
    5: [ ['*', '+KH:Danny', '-9H:Shady', '-KH:Danny'] ]
}

SAMPLE_ROUND_2_SIGNALS = {
    1: ['+AH:Shady', '+8D', '-8D:Danny', '-QS:Shady', '+8C']
}
