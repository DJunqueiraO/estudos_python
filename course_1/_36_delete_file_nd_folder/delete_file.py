import os

file_path = 'c:/workspaceVSC/Estudos_Python/_36_delete_file/test.txt'

try: 
    os.remove(file_path)
except FileNotFoundError as e:
    print('The file does not exist!')
except PermissionError as e:
    print('You do not have permission to delete this file!')
else:
    print('The file was deleted successfully!')
    
    