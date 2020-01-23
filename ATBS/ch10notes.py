"""Organizing files"""

"""The shutil module"""

#shutil stands for "Shell Utilities". It lets you copy, move rename and delete files. 
import shutil 


"""Copying files and folders"""


#shutil.copy(): Lets you copy the file at the path SOURCE to a new DESTINATION.
shutil.copy(source, destination)

#Examples:

p = "You're source filepath here" 
shutil.copy(p/'spam.txt', p/'some_folder')
#This copies the file spam.txt into 'some_folder'

shutil.copy(p/'eggs.txt', p/'some_folder/eggs2.txt')
#This moves eggs.txt to 'some_folder' AND renames it eggs2.txt

#shutil.copytree(: Works the same as .copy() except it copies the entire folder and subfolders/files into the new path.
shutil.copytree(source, destination)

shutil.copytree(p/'spam', p/'spam_backup')
