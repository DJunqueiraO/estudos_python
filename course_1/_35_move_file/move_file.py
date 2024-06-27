import os

source = "C:\\workspaceVSC\\Estudos_Python\\_35_move_file\\test.txt"
destination = "C:\\workspaceVSC\\Estudos_Python\\_35_move_file\\target\\test.txt"

try: 
    if os.path.exists(destination):
        print("The file already exists!")
    else:
        os.replace(source, destination)
        print(source + " was moved to " + destination)
except FileNotFoundError as e:
    print('File not found!')
    
    