import os

def verify(path):
    if os.path.exists(path):
        print('The file exists')
        if os.path.isfile(path):
            print('The path is a file')
        elif os.path.isdir(path):
            print('The path is a directory')
    else:
        print('The file does not exist')

path = 'C:\\workspaceVSC\\Estudos_Python\\_31_file_detection\\fest.txt'

verify(path)
print()

path = 'C:\\workspaceVSC\\Estudos_Python\\_31_file_detection\\test.txt'

verify(path)