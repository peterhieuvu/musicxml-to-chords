import spelling

# Contains utility function to map between chord and integer representation

ROOT_BITS = 6 # 35
BASS_BITS = 6 # 35
KIND_BITS = 2 # 4
EXT_BITS = 3 # 8

# Parse and convert chord to integer representation
def toInt(root, bass, kind, extention):
    # First parse the chord
    out: int = -1

    # TODO: I first had the map not start at zero so that we could do some easier squashing
    # Down to the simplest representation, but I'm now thinking it's probably better to
    # just keep double sharps and flats since when they do appear, there's usually
    # a very good reason (functionally)
    rooti = spelling.step2tpc(root) + TPC_MIN
    bassi = spelling.step2tpc(bass) + TPC_MIN
    kindi = QUALITY_MAP[kind]
    exti = EXT_MAP[extension]

    out += rooti
    out <<= BASS_BITS # make room for bass
    out += bassi
    out <<= KIND_BITS # make room for kind
    out += kindi
    out <<= EXT_BITS # make room for extension
    out += exti

# Turn int representation back into root, bass, kind, and extension
def fromInt(number):
    pass

# Turn int representation back into chord text
def intToChord(number):
    pass