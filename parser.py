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
       print "Choose the file's index on which to operate (10 to load a new file, 11 to exit): "
       option = input()
       
       if int(option) == 10:
           print "Enter new path and filename to load: "
           new_file = raw_input()
           print new_file 
           check_load_file(new_file, files)
           print_available_files(files)     
       elif int(option) == 11:
           print "Exiting.."
           return
       elif int(option) < len(files):
           if files[int(option)].filetype == 'csv':
               get_file_options_csv(files[int(option)])
           else:
               get_file_options_txt(files[int(option)])
       else:
           print "Error invalid index: ", option

def get_file_options_txt(data_file):
    print 'TXT_OPTIONS'
   
def get_file_options_csv(data_file):
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
    file_option = int(raw_input("Operation: "))
    
    #Switch statment is no more =(
    if file_option == 0:
        data_file.print_vectors()
    elif file_option == 1:
        vector_index = int(raw_input("Vector index: "))
        print data_file.vectors[vector_index].length()
    elif file_option == 2:
        vector_index = raw_input("Vector index pair: ").split(" ")
        print data_file.dot_product(int(vector_index[0]), int(vector_index[1]))    
    elif file_option == 3:
        vector_index = raw_input("Vector index pair: ").split(" ")
        print data_file.euclidian(int(vector_index[0]), int(vector_index[1])) 
    elif file_option == 4:
        vector_index = raw_input("Vector index pair: ").split(" ")
        print data_file.manhattan(int(vector_index[0]), int(vector_index[1])) 
    elif file_option == 5:
        vector_index = raw_input("Vector index pair: ").split(" ")
        print data_file.pearson(int(vector_index[0]), int(vector_index[1])) 
    elif file_option == 6:
        vector_index = raw_input("Vector index pair: ").split(" ")
        print data_file.euclidian(int(vector_index[0]), int(vector_index[1])) 
    elif file_option == 7:
        vector_index = int(raw_input("Vector index: "))
        vector = data_file.vectors[vector_index]
        print "Column: ", vector_index, "\nmean: ", vector.mean(), "\nmedian: ", vector.median(), "\nsmallest: ",  vector.smallest(), "\nlargest: ", vector.largest()  
        return
    elif file_option == 8:
        column = int(raw_input("Column: "))
        print "Vector: ", vector_index, "\nmean: ", data_file.mean(), "\nmedian: ", data_file.median(), "\nsmallest: ",  data_file.smallest(), "\nlargest: ", data_file.largest()  
    elif file_option == 9:
        column = int(raw_input("Column: "))
        vector_index = int(raw_input("Vector index: "))
        vector = data_file.vectors[vector_index]
        print "Standard deviation within vector ", vector_index, ": ", vector.standard_dev(), "\nStandard deviation in column ", column, ": ", data_file.standard_dev(column) 
        return
    else:
        print "Invalid operation." 
   
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

