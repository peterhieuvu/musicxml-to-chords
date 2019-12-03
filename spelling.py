# utilities for spelling chords, notes, and keys

# Mapping between a root/bass and its Tonal Pitch Class (TPC)
#
# This tonal pitch class is a representation of different notes
# given their relationship between one another
TPC_MAP = {
    'Fbb' : -14, 'Cbb' : -13, 'Gbb' : -12, 'Dbb' : -11, 'Abb' : -10, 'Ebb' : -9, 'Bbb' : -8, 
    'Fb' : -7, 'Cb' : -6, 'Gb' : -5, 'Db' : -4, 'Ab' : -3, 'Eb' : -2, 'Bb' : -1, 
    'F' : 0, 'C' : 1, 'G' : 2, 'D' : 3, 'A' : 4, 'E' : 5, 'B' : 6, 
    'F#' : 7, 'C#' : 8, 'G#' : 9, 'D#' : 10, 'A#' : 11, 'E#' : 12, 'B#' : 13,
    'F##' : 14, 'C##' : 15, 'G##' : 16, 'D##' : 17, 'A##' : 18, 'E##' : 19, 'B##' : 20
}

def step2tpc(step):
    return TPC_MAP[step]

# Opposite mapping of TPC_MAP
STEP_MAP = { val: key for key, val in TPC_MAP.items() }

def tpc2step(tpc):
    return STEP_MAP[tpc]

# The (TPC) difference between enharmonic notes
ENHARMONIC_DIFF = 12
TPC_MIN = -14
TPC_MAX = 20

# Mapping between the quality of a chord and a number representation
#
# This mapping is based off of musicxml <kind> tags which means
# we can use that to reduce all of the different labels down
# to one string. (ex. m, min, - all reduce to <kind>minor</kind>)
QUALITY_MAP = {
    'minor' : 0,
    'major' : 1,
    'augmented' : 2,
    'diminished' : 3
}

def quality2int(quality):
    return QUALITY_MAP[quality]

# TODO: Do opposite conversion

def int2quality(num):
    pass

def key2step(key):
    return tpc2step(key - 1) # tpc is centered around F while key is centered around C

# Mapping between the extension of a chord and a number representation
#
# This mapping is based off of musicxml tags and will be remapped to
# different numbers to help reduce the number of bits required in the representation
EXT_MAP = {

}

ALT_MAP = { -2 : 'bb', -1 : 'b', 0 : '', 1 : '#', 2 : '##' }

def alt2acc(alt):
    return ALT_MAP[alt]
