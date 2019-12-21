import glob
# import send2trash
import os
import numpy as np
import shutil
import natsort


#main folder which contains many folder
root_dir = r'H:\vishal\vishal'
#rename file will be saved in this folders
dest_dir =r'H:\vishal'
dir = []

with os.scandir(root_dir) as entries:
#give all folders and files in the main folder
    for entry in entries:
        # to get only directory
        if entry.is_dir():
            # to get full path of referance directory from which images will be rename
            ref_dir = os.path.join(root_dir , entry.name)
            # directory in which rename images will be saved
            folder_dir = os.path.join(dest_dir, entry.name)
            #to check folder to save rename images is present or not if not then create .
            CHECK_FOLDER = os.path.isdir(folder_dir)
            if not CHECK_FOLDER:
                os.makedirs(entry.name)
                print("created folder : ", dest_dir)

            else:
                print(dest_dir, "folder already exists.")
            #to read all images or file in list
            img =[]
            for imag in os.listdir(ref_dir):
                img.append(imag)

            #Apply sorting for random read images
            img = natsort.natsorted(img)
            #to read name of each image one by name
            for name in img:
                # print(name[9:-6])
                #original file path will get
                src_dir = os.path.join(ref_dir, name)
                # print(name[7:8])
                a = name[7:8]
                b = name[7:8]
                d = str(entry.name).zfill(3)
                c = str(name[9:-6]).zfill(2)

                if a == b:
                    NewName = d + 'C1T000' + b + 'F0' + c+".jpg"
                    shutil.move(src_dir,folder_dir+ '/' + NewName)

                else:
                    NewName = d + 'C1T000' + a + 'F0' + c+".jpg"
                    shutil.move(src_dir, folder_dir + '/' + NewName)


