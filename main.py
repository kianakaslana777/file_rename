import os

path = '/Users/kiana/Desktop/1/'
with open('oldfilename.txt', 'r') as f:
    _filename = [i.strip('\n') for i in f.readlines()]

with open('filename.txt', 'r') as f:
    filename = [i.strip('\n') for i in f.readlines()]

files = os.listdir(path)


def do(files, _filename, filename):
    for i in files:
        for j in _filename:
            if i == j:
                oldname = path + i
                name = path + filename[_filename.index(j)]
                os.rename(oldname, name)


if __name__ == '__main__':
    do(files, _filename, filename)
