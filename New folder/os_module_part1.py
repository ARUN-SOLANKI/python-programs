import os
import shutil
# print(os.getcwd())
# os.mkdir('mafbypython')
# print(os.path.exists('movies'))
# if os.path.exists('movies') :
#     print("it exists") 
# else:
#     print("it not exsist")
#     os.mkdir('movies')

# print(os.listdir(r'C:\Users\other\Documents\FlashIntegro\VideoEditor'))

# for item in os.listdir() :
    # print(os.getcwd()  + ' \\' + item )
    # print(os.path.join(os.getcwd() , item))

# getfiles = os.walk(os.getcwd())
# for current_path , folder_names , file_names in getfiles :
#     print(f'current path : {current_path}')
#     print(f'folder name : {folder_names}')
#     print(f'file names : {file_names}')
 
print(os.getcwd())
# shutil.copytree('movies','files/copied')
shutil.copy('os_module_part1.py' , 'movies/copied_file') 