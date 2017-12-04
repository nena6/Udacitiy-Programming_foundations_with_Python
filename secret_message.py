#Rename a bunch of files

# 1) Get filenames from folder

# 3)

import os

def rename_files():
   file_list = os.listdir(r'C:\Users\enevvid\Desktop\Self-learning\Projects\Udacity-Programming Foundations with Python\prank')
   #print(file_list)
   os.chdir(r'C:\Users\enevvid\Desktop\Self-learning\Projects\Udacity-Programming Foundations with Python\prank')
   # 2)For each file - rename
   for file_name in file_list:
       #Deletes all the digits from string. For string objects, set the table argument to None for translations that only delete characters.
       #new_name = file_name.translate("0123456789", None) #Need to use unicode.translate in Python 3, pass deletechars
       new_name = file_name.translate(str.maketrans('', '', '1234567890')) #Check maketrans
       print("Renaming file from " + file_name + " to " + new_name)
       os.rename(file_name, new_name)

rename_files()