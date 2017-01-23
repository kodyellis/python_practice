#!/usr/bin/python
import os
from datetime import datetime
# print("Enter a file name to get stats")
# some_file = input()
# modication_time = os.stat(some_file).st_mtime
#
# print(datetime.fromtimestamp(modication_time))

#os.walk is generator a directory tree
#**********************USE in Future******************
# for dirpath, dirnames, filenames in os.walk('/home/marquise/bin'):
#     print('Current path:' , dirpath)
#     print('Directories:' , dirnames)
#     print('Files:' , filenames)

# print(os.environ.get('HOME'))
# file_path = os.path.join(os.environ.get('HOME') ,'test.txt') # joins file and directory to create file
# print(file_path)

print(os.path.basename('/tmp/test.txt'))#name of file
print(os.path.dirname('/tmp/test.txt'))#directory name
print(os.path.split('/tmp/test.txt'))# both
print(os.path.exists('/tmp/test.txt'))# Is it real or fake
print(os.path.isfile('/tmp/test.txt'))# is it a file
print(os.path.isdir('/tmp/test.txt'))# isd it a directory
print(os.path.splitext('/tmp/test.txt'))# seprate the extensions
