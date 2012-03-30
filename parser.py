import sys
import os.path
import csv
import math
from data_types import Data, CSVData, TextData, Vector

def main():
    files=[]
    if len(sys.argv) <= 1:
        print 'Error no files specified'
        return

    #load all files appearing in arguments
    for x in range(1, len(sys.argv)):
        check_load_file(sys.argv[x], files)     

    print_available_files(files)
    while True:
       print "Choose the index of one of the above files to operate upon it or choose 10 to load a new file."
       option = input()
       
       if int(option) == 10:
           print "Enter new path and filename to load:"
           new_file = raw_input()
           print new_file 
           check_load_file(new_file, files)
           print_available_files(files)     
       else:
           get_available_file_options(files[int(option)])

def get_available_file_options(data_file):
    if data_file.filetype == 'csv':
        print '    [0] - Print Vectors'
        print '    [1] - Vector Length'
        print '    [2] - Dot Product'
        print '    [3] - Eucledian Distance'
        print '    [4] - Manhattan Distance'
        print '    [5] - Pearson Correlation'
        print '    [6] - Basic Stats - Vector'
        print '    [7] - Basic Stats - Collection'
        print '    [8] - Standard Deviation - Column'
        print '    [9] - Standard Deviation - Collection'
        file_option = int(input())
        
        #Switch statment is no more =(
        if file_option == 0:
            data_file.print_vectors() 
    elif data_file.filetype == 'txt':
        print 'TXT_OPTIONS'
    return

def print_available_files(files):
    for x in range(0, len(files)):
        print "[",x,"] - ", files[x].filename

def check_load_file(filename, files):
    if not os.path.exists(filename) or not os.path.isfile(filename): 
        print 'Error can not find the specified file'
        return

    filetype = filename.split('.')[1]
    if filetype == 'csv':
        csv_data = CSVData(filename)
        csv_data.parse_vectors()
        #csv_data.print_vectors()
    elif filetype == 'txt':
        parse_txt(sys.argv[1])
    else:
        print 'Error unrecognized file type ', filetype
        return

    files.append(csv_data)
    print 'Parsed file: ', filename 

if __name__ == '__main__':
    main()

