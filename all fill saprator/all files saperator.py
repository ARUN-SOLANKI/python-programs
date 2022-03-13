import os , shutil
dict_extentions = {
    'audio_ext' : ('.mp3' , '.wav' , '.flac' , '.m4a'),
    'video_ext' : ('.mp4' , '.avi' , '.mkv' , '.MKV' , '.flv' , '.mpeg'),
    'file_ext' : ('.docx' , '.pptx' , '.pdf' , '.txt'),
    'img_ext' : ('.jpg' , '.png'),
    }
# folderpath = input('enter a folder path')
folderpath = os.getcwd()

def file_finder(folder_path , file_extention):
    files = []
    for file in os.listdir(folder_path):
        for extention in file_extention:
            if file.endswith(extention):
                files.append(file)
    return files

# print(file_finder(folderpath , video_ext))

for extentin_type , extention_tuple in dict_extentions.items() :
    folder_name = extentin_type.split('_')[0] +' ' + 'file'
    folder_path = os.path.join(folderpath , folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath , extention_tuple):
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(folderpath,folder_path)
        shutil.move(item_path,item_new_path)   

# C:\Users\other\Desktop\my_first_project