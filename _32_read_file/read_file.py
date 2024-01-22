path = 'C:\\workspaceVSC\\Estudos_Python\\_32_read_file\\test.txt'

try: 
    with open(path) as file:
        print(file.read())
except FileNotFoundError as e:
    print(f'{e}, The file does not exist!')