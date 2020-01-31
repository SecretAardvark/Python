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


#Examples:

shutil.copytree(p/'spam', p/'spam_backup')
#Makes a copy of the spam folder in the new directory

"""Moving and renaming files and folders"""

#Shutil.move(): This moves the file or folder at <source> to the new <destination>
shutil.move(source, destination)

#Examples:

shutil.move('c:/bacon.txt', 'c:/Eggs')
#Move the file 'bacon.text' into the folder 'eggs'
#If there was already a 'bacon.txt' file in 'c:/eggs', it gets overwritten. Be careful!

shutil.move('c:/bacon.txt', 'c:/eggs/new_bacon.txt')
#Moves 'bacon.txt' into 'c:/eggs' AND renames it. 

#Both examples above assume the folder C:/eggs already exists. If not, bacon just gets renamed.

"""Permanently deleting files and folders"""

# os.unlink(): Deletes the file at path
os.unlink(path)

#Example:
os.unlink('c:/bacon.txt')
#Deletes bacon.txt:

#os.rmdir():  Deletes the folder at path. The folder must be empty.
os.rmdir(path)

#Example:
os.rmdir('c:/eggs/')
#Deletes the 'eggs' folder

#os.rmtree(): Works the same as rmdir(), but ALSO deletes any files and folders inside.
os.rmtree(path)

#example:
os.rmtree('c:/eggs/bacon.txt')
#Deletes the eggs folder AND the bacon.txt inside


"""Safe deleting with the send2trash module"""

# The built in shutil.rmtree() function permanently deletes files and folders, 
# So it can be dangerous to use. Using send2trash is much safer because it sends
# the files/folders to the recycling bin instead of permanent deletion. 

#Example: 

send2trash.send2trash('bacon.txt') #Sends bacon.txt to the recycling bin

"""Walking as directory tree"""

os.walk(path)
#os.walk(): This function lets you iterate of the directory tree given in the 'path' argument.
#   This can be useful if you want to rename all the files in a certain folder, etc. 

"""Compressing files with the zipfile module"""

#Your python programs can create and open compressed .zip files with the zipfile module

zipfile.Zipfile(source)
#This creates a zipfile object to work with. 

#Ex: 
p = Path.home()
examplezip = zipfile.Zipfile('p/example.zip')

examplezip.namelist()
#This returns a list of strings for all the files and folders contained in the zip file.
#['spam.txt,'cats/','cats/catnames.txt', 'cats/zophie.jpg']

examplezip.getinfo(file)
#.getinfo(): This method returns a zipinfo object about that particular file. These have their own
#   attributes such as: .file_size and .compress_size

#Example: 

spaminfo= examplezip.getinfo('spam.txt')
#Returns an object with info about spam.txt 

spaminfo.file_size
#Returns the original filesize in bytes. 

spaminfo.compress_size
#returns the compressed filesize in bytes. 

"""Extracting from .zip files"""

examplezip.extractall(*path)
#.extractall(): extracts all the files and folders in the .zip to the current working directory.
#   It can also be passed a a folder name to extract all the files into that folder. This will also
#   create the folder if it doesn't exist. 

examplezip.extract(file, *path)
# .extract(): Extracts one file from a .zip into the current working directory. If given a path, it will 
#   extract the file to that destination. 


#Examnples: 
p= Path.home()

examplezip = zipfile.Zipfile('p/example.zip')
examplezip.extractall()
#Extracts all the files into c:/ 

examplezip.extractall('p/new_folder/')
#Extracts the files into c:/new_folder/

"""Creating and adding to zip files"""

newzip = zipfile.Zipfile(zipfile_name, 'w')
#To create a ZIP file, open the ZipFile object in write mode by passing 'w' as the second argument. 
#   This works similar to the open() function. 


newzip.write(filename, compress_type)
#.write(): When you pass .write a filename or path, it will compress the file at that path 
#   and add it to the zipfile. The second argument tells the computer what compression type 
#   to use. zipfile.ZIP_DEFLATED is reccommended. 
   
#IMPORTANT: write mode will erase all existing contents of a zip file. If you want to ADD 
#   a file to a .zip, open the file with 'a' (append mode) as the second argument. 

