import xml.etree.ElementTree as ET
import spelling
import chord

HARMONY_NAME = 'harmony'

def get_chords(xmlfile):
    chords = [] # list of found chords

    tree = ET.parse(xmlfile)
    root = tree.getroot()

    # TODO: Parse key

    for h in root.iter(HARMONY_NAME):
        # go through each harmony object
        # find root (root/root-step)
        # get kind (kind)
        # find quality within kind
        # find extension within kind
        pass
    
    return chords

# Extract vocabulary from xml
def get_vocab(xmlfile):
    roots = set()
    kinds = set()
    tags = set()

    tree = ET.parse(xmlfile)
    root = tree.getroot()

    for h in root.iter(HARMONY_NAME):
        rootstep = h.find('root/root-step')
        rootalt = h.find('root/root-alter')
        kind = h.find('kind')

        roots.add(rootstep.text + spelling.alt2acc(int(rootalt.text) if rootalt is not None else 0))
        kinds.add(kind.text)
        for e in h.iter(): tags.add(e.tag)

    return roots, kinds, tags
