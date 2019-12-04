import spelling

# Contains utility function to map between chord and integer representation

ROOT_BITS = 5 # 21
BASS_BITS = 5 # 21
KIND_BITS = 5 # 24

NO_CHORD = -1 # Number representing no chord/end of piece

# Parse and convert chord to integer representation
# [5 root bits][5 bass bits][5 kind bits]
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
# [5 root bits][5 bass bits][5 kind bits]
def fromInt(number):
    if number == NO_CHORD:
        return "", "", ""

    kindi = number % (1 << KIND_BITS) # get kind bits
    number >>= KIND_BITS # shift right to get bass bits
    bassi = number % (1 << BASS_BITS) + spelling.TPC_MIN
    number >>= BASS_BITS # shift right to get to root bits
    rooti = number + spelling.TPC_MIN

    # convert int values back to strings
    kind = spelling.int2kindText(kindi)
    bass = spelling.tpc2step(bassi)
    root = spelling.tpc2step(rooti)
    
    return root, bass, kind

# Turn int representation back into chord text
def intToText(number):
    if number == NO_CHORD:
        return "N.C."
    r, b, k = fromInt(number)
    if r == b:
        return r + k
    else:
        return r + k + "/" + b

# Turn chord text into int representation
def textToInt(text):
    root = text[0]
    if len(text) == 1: return toInt(root, root, "major")

    alter = ''
    kidx = 1
    if text[1] in spelling.ACC_MAP:
        alter = text[0]
        kidx = 2
    
    slashidx = text.find('/')
    if slashidx == -1: return toInt(root + alter, root + alter, spelling.KIND_REV_MAP[text[kidx:]])
    else: return toInt(root + alter, text[slashidx+1:], spelling.KIND_REV_MAP[text[kidx:slashidx]])
