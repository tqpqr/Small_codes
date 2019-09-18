import os
import shutil

# Path to folder with subfolder, that contain files, needed to be extracted
folder = 'D:/EMULATORS/ROMS/GBA/' # path example
folders_list = os.listdir(folder)
#print(folders_list)

for f in folders_list:
    rom = os.listdir(folder+f)
    #print(name)
    for fil in name:
        print(folder+f+('/')+fil)
        shutil.copy((folder+f+('/')+fil), folder)
        print('FILE '+fil+' is copied')
