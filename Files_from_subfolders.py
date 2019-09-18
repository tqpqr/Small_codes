import os
import shutil

# Path to folder (C:/MAIN_FOLDER/) with subfolders (C:/MAIN_FOLDER/Sub_folder1, sub_folder2 etc.), that contains files, 
# needed to be copied directly to MAIN_FOLDER
folder = 'C:/MAIN_FOLDER/'
folders_list = os.listdir(folder)
#print(folders_list)

for f in folders_list:
    rom = os.listdir(folder+f)
    #print(name)
    for fil in name:
        print(folder+f+('/')+fil)
        shutil.copy((folder+f+('/')+fil), folder)
        print('FILE '+fil+' is copied')
