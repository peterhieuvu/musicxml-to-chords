# utilities for spelling chords, notes, and keys

# Mapping between a root/bass and its Tonal Pitch Class (TPC)
#
# This tonal pitch class is a representation of different notes
# given their relationship between one another
TPC_MAP = {
    #'Fbb' : -14, 'Cbb' : -13, 'Gbb' : -12, 'Dbb' : -11, 'Abb' : -10, 'Ebb' : -9, 'Bbb' : -8, 
    'Fb' : -7, 'Cb' : -6, 'Gb' : -5, 'Db' : -4, 'Ab' : -3, 'Eb' : -2, 'Bb' : -1, 
    'F' : 0, 'C' : 1, 'G' : 2, 'D' : 3, 'A' : 4, 'E' : 5, 'B' : 6, 
    'F#' : 7, 'C#' : 8, 'G#' : 9, 'D#' : 10, 'A#' : 11, 'E#' : 12, 'B#' : 13
    #'F##' : 14, 'C##' : 15, 'G##' : 16, 'D##' : 17, 'A##' : 18, 'E##' : 19, 'B##' : 20
}

def step2tpc(step):
    return TPC_MAP[step]

# Opposite mapping of TPC_MAP
STEP_MAP = { val: key for key, val in TPC_MAP.items() }

def tpc2step(tpc):
    return STEP_MAP[tpc]

# The (TPC) difference between enharmonic notes
ENHARMONIC_DIFF = 12
TPC_MIN = -7
TPC_MAX = 13

# Mapping between the kind of a chord and a number representation
#
# This mapping is based off of Fmusicxml <kind> tags which means
# we can use that to reduce all of the different qualities and extensions down
# to one string. (ex. m, min, - all reduce to <kind>minor</kind>)
KIND_MAP =  {
    'major': 0, 
    'minor': 1, 
    'half-diminished': 2, 
    'diminished': 3, 
    'augmented': 4, 
    'major-seventh': 5,
    'minor-seventh': 6,
    'dominant': 7, 
    'major-ninth': 8,
    'minor-ninth': 9, 
    'dominant-ninth': 10,
    'minor-11th': 11, 
    'dominant-11th': 12,
    'minor-13th': 13, 
    'minor-sixth': 14, 
    'major-13th': 15, 
    'dominant-13th': 16,
    'dominant-alt': 17, 
    'suspended-fourth': 18,
    'augmented-seventh': 19,
    'major-sixth': 20, 
    'major-minor': 21, 
    'power': 22, 
    'alt': 23
}

def kind2int(kind):
    return KIND_MAP[kind]

KIND_TEXT_MAP = {
#    0: 'major',
#    1: 'minor', 
#    2: 'half-diminished',
#    3: 'diminished',
#    4: 'augmented',
#    5: 'major-seventh', 
#    6: 'minor-seventh', 
#    7: 'dominant',
#    8: 'major-ninth', 
#    9: 'minor-ninth', 
#    10: 'dominant-ninth',
#    11: 'minor-11th',
#    12: 'dominant-11th',
#    13: 'minor-13th',
#    14: 'minor-sixth',
#    15: 'major-13th',
#    16: 'dominant-13th',
#    17: 'dominant-alt',
#    18: 'suspended-fourth',
#    19: 'augmented-seventh',
#    20: 'major-sixth',
#    21: 'major-minor',
#    22: 'power',
#    23: 'alt'
    0: '',
    1: 'm', 
    2: 'm7(b5)',
    3: 'dim',
    4: 'aug',
    5: 'maj7', 
    6: 'm7', 
    7: '7',
    8: 'maj9', 
    9: 'm9', 
    10: '9',
    11: 'm11',
    12: '11',
    13: 'm13',
    14: 'm6',
    15: 'maj13',
    16: '13',
    17: '7alt',
    18: 'sus4',
    19: '+7',
    20: '6',
    21: 'm(maj7)',
    22: '5',
    23: 'alt'
}

KIND_REV_MAP = { valt: valk for k1, valt in KIND_TEXT_MAP.items() for valk, k2 in KIND_MAP.items() if k1 == k2 }

def int2kindText(num):
    return KIND_TEXT_MAP[num]

def key2step(key):
    return tpc2step(key - 1) # tpc is centered around F while key is centered around C

ALT_MAP = { -2 : 'bb', -1 : 'b', 0 : '', 1 : '#', 2 : '##' }

ACC_MAP = { val: key for key, val in ALT_MAP.items() }

def alt2acc(alt):
    return ALT_MAP[alt]

def isValid(a, b, c):
    return a in KIND_TEXT_MAP and b in STEP_MAP and c in STEP_MAP