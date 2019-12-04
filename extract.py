import os
import sys
import zipfile
import parser

DATA_PATH = 'data/'
OUT_DIR = 'output/'

INTERNAL_FILE_NAME = 'musicXML.xml'
UPDATE_INCREMENT = 5 # How often to update percentage progress (10 would be every 10 percent)

# Traverse from root to find .mxl files
def traverse_directories(root):
    print('Looking for .mxl files in {}...'.format(root))
    files = [] # output list that contains all files

    for dirName, _, subFiles in os.walk(root):
        print('\tlooking in {}'.format(dirName))
        for f in subFiles:
            if not f.endswith('.mxl'):
                continue
            path = os.path.join(dirName, f)
            files.append(path)

    return files

# Extract .xml files from the .mxl files and put into target folder
def extract_xml(files, target):
    print('Extracting files from {}...\n'.format(target))

    # create output directory if it doesn't exist yet
    if not os.path.exists(target):
        os.makedirs(target)

    num_files = len(files)
    incr = num_files // (100 // UPDATE_INCREMENT)
    counter = 0

    # First unzip files and store intermediate result
    for file in files:
        try:
            with zipfile.ZipFile(file) as zf:
                # get absolute path of output file
                # we only take the basename and change the extension to .xml
                outpath = os.path.join(target, os.path.basename(file)).replace('.mxl', '.xml')
                #print('\t extracting file to {}'.format(outpath))
                if INTERNAL_FILE_NAME not in zf.namelist():
                    print("No XML file {} found in zipfile: {}".format(INTERNAL_FILE_NAME, file))
                    continue
                    #raise Exception("No XML file {} found in zipfile: {}".format(INTERNAL_FILE_NAME, file))
                with open(outpath, 'wb+') as f: # create file for writing
                    f.write(zf.read(INTERNAL_FILE_NAME))
        except:
            print("!!!!!!ERROR EXTRACTING XML FOR FILE {}".format(file))
        finally:
            counter += 1
        if counter % incr == 0:
            print("{:.2f}%, file {}/{}".format(100. * counter/num_files, counter, num_files))

# read .xml files from target and extract pure chord data
def extract_chords(target):
    print('Extracting chords from: {}\n'.format(target))
    
    intermediate = os.path.join(target, 'intermediate/')
    files = os.listdir(intermediate)
    num_files = len(files)
    incr = num_files // (100 // UPDATE_INCREMENT)
    counter = 0

    print('{} xml files found'.format(num_files))

    # go through all files in target, parse the xml, and write it comma separated into a file
    for file in os.listdir(intermediate):
        #print(os.path.join(intermediate, file))

        chords = parser.get_chords(os.path.join(intermediate, file))
        with open(os.path.join(target + os.path.basename(file).replace('.xml', '.txt')), 'w+') as f:
            f.write(','.join(chords))
        counter += 1
        if counter % incr == 0:
            print("{:.2f}%, file {}/{}".format(100. * counter/num_files, counter, num_files)) 

def main(dataPath=DATA_PATH, outDir=OUT_DIR):
    path = os.getcwd()
    readpath = path + '/' + dataPath
    writepath = path + '/' + outDir
    print('Processing data in: {}, outputting to: {}\n'.format(readpath, writepath))
    
    # look for .mxl files in the DATA_PATH
    files = traverse_directories(dataPath)
    print('Found {} files\n'.format(len(files)))

    # extract the .xml files from the .mxl
    extract_xml(files, os.path.join(outDir, 'intermediate/'))

    # extract the chord data
    extract_chords(outDir)

    # delete the intermediate result
    #os.remove(os.path.join(outDir, 'intermediate/'))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        #print('Corect Usage:')
        #print('data_directory output_directory')
        main()
    else: 
        main(sys.argv[1], sys.argv[2])