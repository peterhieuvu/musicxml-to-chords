import spelling

# Contains utility function to map between chord and integer representation

ROOT_BITS = 5 # 21
BASS_BITS = 5 # 21
KIND_BITS = 5 # 24

NO_CHORD = -1 # Number representing no chord/end of piece

# Parse and convert chord to integer representation
def toInt(root, bass, kind):
    # First parse the chord
    out = -1

    # TODO: I first had the map not start at zero so that we could do some easier squashing
    # Down to the simplest representation, but I'm now thinking it's probably better to
    # just keep double sharps and flats since when they do appear, there's usually
    # a very good reason (functionally)
    rooti = spelling.step2tpc(root) - spelling.TPC_MIN
    bassi = spelling.step2tpc(bass) - spelling.TPC_MIN
    kindi = spelling.kind2int(kind)

    out = rooti
    out <<= BASS_BITS # make room for bass
    out += bassi
    out <<= KIND_BITS # make room for kind
    out += kindi

    return out

# Turn int representation back into root, bass, kind, and extension
def fromInt(number):
    pass

# Turn int representation back into chord text
def intToChord(number):
    pass