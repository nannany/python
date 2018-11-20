import zipfile
import glob


def unzip(filename, path='.'):
    with zipfile.ZipFile(filename, 'r') as zip_file:
        zip_file.extractall(path=path)


if __name__ == '__main__':
    for i in range(20):
        files = glob.glob("./password*")
        target = sorted(files, key=lambda x: len(x))[0]

        unzip(target)
