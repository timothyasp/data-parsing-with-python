import sys
import os
import csv
import math
#import nltk
from data_types import Data, CSVData, TXTData, Vector

def main():
    files=[]
    if len(sys.argv) <= 1:
        run_test_suite()

    # load all files appearing in arguments
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
            print "Error invalid option: ", option

def run_test_suite():
    csvPath = 'data/csv'
    txtPath = 'data/text'

    print "Grabbing CSV files...\n"
    csvList = os.listdir(csvPath)

    print "Grabbing TXT files...\n"
    txtList = os.listdir(txtPath)
    
    print "Beginning CSV tests\n\n"
    for fname in csvList:
        if fname.split('.')[1] != 'csv':
            continue
        filePath = os.path.join(csvPath, fname)
        data = CSVData(filePath)
        print "Opening ",fname
        print "Parsing Vectors...\n"
        data.parse_vectors()

    print "Beginning TXT tests\n\n"
    for fname in txtList:
        if fname.split('.')[1] != 'txt':
            continue
        filePath = os.path.join(txtPath, fname)
        data = TXTData(filePath)
        print "Opening ",fname
        print "Parsing Text and reading into Document...\n"
        data.read_document()

def get_file_options_txt(data_file):
    print '    [0] - Read file in Paragraph chunks'
    print '    [1] - Read file in Sentence chunks'
    print '    [2] - Read file in Word chunks'
    print '    [3] - Create/Print word list'
    print '    [4] - Create/Print freq list'
    print '    [5] - Document statistics'
    print '    [6] - Document frequency statistics'
    print '    [7] - Check document for word'
    file_option = int(raw_input("    Operation: "))

    if file_option == 0:
        for i, v in enumerate(data_file.paragraph_tokenize()):
            print "Paragraph[",i,"]:\n", v
    elif file_option == 1:
        for i, v in enumerate(data_file.sentence_tokenize()):
            print "Sentence[",i,"]:\n", v
    elif file_option == 2:
        for i, v in enumerate(data_file.word_tokenize()):
            print "Word[",i,"]:\n", v
    elif file_option == 3:
        for i, v in enumerate(data_file.word_tokenize()):
            print "Word[",i,"]:\n", v
    elif file_option == 4:
        for i, v in enumerate(data_file.word_tokenize()):
            print "Word[",i,"]:\n", v
    elif file_option == 5:
        for i, v in enumerate(data_file.word_tokenize()):
            print "Word[",i,"]:\n", v
    elif file_option == 6:
        for i, v in enumerate(data_file.word_tokenize()):
            print "Word[",i,"]:\n", v
    elif file_option == 7:
        for i, v in enumerate(data_file.word_tokenize()):
            print "Word[",i,"]:\n", v
    else:
        print "Error invalid index: ", option

def get_file_options_csv(data_file):
    print '    [0] - Print Vectors'
    print '    [1] - Vector Length'
    print '    [2] - Dot Product'
    print '    [3] - Eucledian Distance'
    print '    [4] - Manhattan Distance'
    print '    [5] - Pearson Correlation'
    print '    [6] - Basic Stats - Vector'
    print '    [7] - Basic Stats - Column'
    print '    [8] - Standard Deviation - Column'
    print '    [9] - Standard Deviation - Collection'
    file_option = int(raw_input("Operation: "))
    
    if file_option == 0:
        data_file.print_vectors()
    elif file_option == 1:
        vector_index = int(raw_input("Vector index: "))
        if vector_index >= len(data_file.vectors):
            print "Error invalid index."
        else:
            print data_file.vectors[vector_index].length()
    elif file_option == 2:
        vector_index = raw_input("Vector index pair: ").split(" ")
        if vector_index[0] >= len(data_file.vectors) or vector_index[1] >= len(data_file.vectors):
				print "Error invalid index."
        else:
            print data_file.dot_product(int(vector_index[0]), int(vector_index[1]))    
    elif file_option == 3:
        vector_index = raw_input("Vector index pair: ").split(" ")
        if vector_index[0] >= len(data_file.vectors) or vector_index[1] >= len(data_file.vectors):
            print "Error invalid index."
        else:
            print data_file.euclidian(int(vector_index[0]), int(vector_index[1])) 
    elif file_option == 4:
        vector_index = raw_input("Vector index pair: ").split(" ")
        if vector_index[0] >= len(data_file.vectors) or vector_index[1] >= len(data_file.vectors):
            print "Error invalid index."
        else:
            print data_file.manhattan(int(vector_index[0]), int(vector_index[1])) 
    elif file_option == 5:
        vector_index = raw_input("Vector index pair: ").split(" ")
        if vector_index[0] >= len(data_file.vectors) or vector_index[1] >= len(data_file.vectors):
				print "Error invalid index."
        else:
            print data_file.pearson(int(vector_index[0]), int(vector_index[1])) 
    elif file_option == 6:
        vector_index = int(raw_input("Vector index: "))
        if vector_index >= len(data_file.vectors):
            print "Error invalid index."
        else:
            vector = data_file.vectors[vector_index]
            print "Row: ", vector.values, "\nmean: ", vector.mean(), "\nmedian: ", vector.median(), "\nsmallest: ",  vector.smallest(), "\nlargest: ", vector.largest()  
        return
    elif file_option == 7:
        #  TODO
        vector_index = int(raw_input("Vector column index: "))
        if vector_index >= len(data_file.vectors):
            print "Error invalid index."
        else:
            vector = data_file.h
            print "Row: ", vector_index, "\nmean: ", vector.mean(), "\nmedian: ", vector.median(), "\nsmallest: ",  vector.smallest(), "\nlargest: ", vector.largest()  
        return
    elif file_option == 8:
        column = int(raw_input("Column: "))
        print "Vector: ", column, "\nmean: ", data_file.mean(), "\nmedian: ", data_file.median(), "\nsmallest: ",  data_file.smallest(), "\nlargest: ", data_file.largest()  
    elif file_option == 9:
        column = int(raw_input("Column: "))
        vector_index = int(raw_input("Vector index: "))
        if vector_index >= len(data_file.vectors):
            print "Error invalid index."
        else:
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
        files.append(csv_data)
        #csv_data.print_vectors()
    elif filetype == 'txt':
        txt_data = TXTData(filename)
        txt_data.read_document()
        files.append(txt_data)
    else:
        print 'Error unrecognized file type ', filetype
        return

    print 'Parsed file: ', filename 

if __name__ == '__main__':
    main()

