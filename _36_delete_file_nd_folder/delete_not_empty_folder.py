import os
import shutil

folder_path = 'c:/workspaceVSC/Estudos_Python/_36_delete_file/target'

try: 
    shutil.rmtree(folder_path)
except FileNotFoundError as e:
    print('The file does not exist!')
except PermissionError as e:
    print('You do not have permission to delete this file!')
except OSError as e:
    print('The folder is not empty!')
else:
    print('The folder was deleted!')
    
    