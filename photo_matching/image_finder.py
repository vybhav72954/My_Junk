import hashlib
import os
import sys


def image_finder(parent_folder):
    # A dictionary to store Hash of Images corresponding to names
    """
    Sample -
    {hash:[names]}
    """
    duplicate_img = {}
    for dirName, subdirs, fileList in os.walk(parent_folder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in duplicate_img:
                duplicate_img[file_hash].append(path)
            else:
                duplicate_img[file_hash] = [path]
    return duplicate_img


# Joins two dictionaries
def join_dicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]


def hashfile(path, blocksize=65536):
    img_file = open(path, 'rb')
    hasher = hashlib.md5()
    buf = img_file.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = img_file.read(blocksize)
    img_file.close()
    return hasher.hexdigest()


def print_results(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates Found:')
        print('The following files are identical. The name could differ, but the content is identical')
        print('___________________')
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            print('___________________')

    else:
        print('No duplicate files found.')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        duplicate = {}
        folders = sys.argv[1:]
        for i in folders:
            # Iterate the folders given
            if os.path.exists(i):
                # Find the duplicated files and append them to the dictionary
                join_dicts(duplicate, image_finder(i))
            else:
                print('%s is not a valid path, please verify' % i)
                sys.exit()
        print_results(duplicate)
    else:
        print('Hint: python image_finder.py <path of folders>')
