import os

class FileManager:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        file = open(file=self.path, mode=self.mode)
        self.file = file
        return file

    def __exit__(self, *args, **kwargs):
        self.file.close()
def ls():
    return os.listdir()

def touch(file_name):
    with FileManager(file_name, 'w') as f:
        t = input("Enter text: ")
        f.write(t)
        while True:
            if t == 'exit':
                break
            t = input("Enter text: ")
            f.write(f'\n{t}')
        return 0

def mkdir(dir_name):
    os.mkdir(dir_name)
    return 0
def cd(dirname):
    if dirname == '..':
        os.chdir('..')
    os.chdir(dirname)
    return 0

def mv(file_name):
    folder = file_name[1].split('/')[0]
    file = file_name[0]
    moved = file_name[1].split('/')[1]
    with FileManager(file, 'r') as f:
        text = f.read()
    os.remove(file)
    os.chdir(folder)
    # s = 1
    # if file in os.listdir(folder):
    #     s += 1
    # with FileManager(f'{file}{s}', 'w') as f:
    with open(moved, 'w') as f:
        f.write(text)
    return 0


if __name__ == '__main__':
    com = input("--> ")
    if com == 'ls':
        print(ls())

    if com == 'touch':
        file_name = input("Enter filename: ")
        touch(file_name)

    if com == 'mkdir':
        dir_name = input("Enter foldername: ")
        mkdir(dir_name)

    if com == 'cd':
        dirname = input("Enter foldername: ")
        cd(dirname)

    if com == 'mv':
        file_name = input().split()
        mv(file_name)






