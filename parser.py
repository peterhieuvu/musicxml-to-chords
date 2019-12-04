import xml.etree.ElementTree as ET
import spelling
import chord

HARMONY_NAME = 'harmony'

def get_chords(xmlfile):
    chords = [] # list of found chords

    try: 
        # TODO: Parse key
        tree = ET.parse(xmlfile)
        root = tree.getroot()

        for h in root.iter(HARMONY_NAME):
            rootstep = h.find('root/root-step')
            rootalt = h.find('root/root-alter')
            bassstep = h.find('bass/bass-step')
            bassalt = h.find('bass/bass-alter')
            kind = h.find('kind')

            root = rootstep.text + spelling.alt2acc(int(rootalt.text) if rootalt is not None else 0)
            bass = root
            if bassstep is not None:
                bass = bassstep.text + spelling.alt2acc(int(bassalt.text) if bassalt is not None else 0)

            chords.append(str(chord.toInt(root, bass, kind.text)))
    except:
        print("!!!!!!ERROR PARSING CHORDS FROM XML FOR FILE {}".format(xmlfile))
    finally:
        return chords
    
    return chords

# Extract vocabulary from xml
def get_vocab(xmlfile):
    roots = set()
    kinds = set()
    tags = set()

    try: 
        tree = ET.parse(xmlfile)
        root = tree.getroot()

        for h in root.iter(HARMONY_NAME):
            rootstep = h.find('root/root-step')
            rootalt = h.find('root/root-alter')
            kind = h.find('kind')

            roots.add(rootstep.text + spelling.alt2acc(int(rootalt.text) if rootalt is not None else 0))
            kinds.add(kind.text)
            for e in h.iter(): 
                tags.add(e.tag)
    except:
        print("!!!!!!ERROR PARSING XML FOR FILE {}".format(xmlfile))
    finally:
        return roots, kinds, tags

    return roots, kinds, tags
