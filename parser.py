import sys
import os.path
import csv
import math
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
           print "Error invalid index: ", option

def get_file_options_txt(data_file):
    print '    [0] - Read file in Paragraph chunks'
    print '    [1] - Read file in Sentence chunks'
    print '    [2] - Read file in Word chunks'
    print '    [3] - Create/Print word list'
    print '    [4] - Create/Print freq list'
    print '    [5] - Document statistics'
    print '    [6] - Document frequency statistics'
    print '    [7] - Check document for word'
    print '    [8] - Return to file list'
    file_option = 0

    while file_option != 8: 
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
            print 'Unique Word List:'
            for x in data_file.unique_word_list():
                print x
        elif file_option == 4:
            print 'Word Frequency List:'
            word_dict = data_file.unique_word_frequency()
            for k in word_dict.keys():
                print k, ":", word_dict[k]
        elif file_option == 5:
            data_file.print_count_statistics()
        elif file_option == 6:
            greater = raw_input("Find words with frequencies greater than: ")
            equal = raw_input("Find words with frequencies equal to: ")
            data_file.print_freq_statistics(equal, greater)
        elif file_option == 7:
            search_word = raw_input("Search for word: ")
            if data_file.word_search(search_word) == False:
                print 'Word not found'
            else: 
                print 'Word found'
        else:
            print "Error invalid index: ", option

def get_file_options_csv(data_file):
    print '    [0]  - Print Vectors'
    print '    [1]  - Vector Length'
    print '    [2]  - Dot Product'
    print '    [3]  - Eucledian Distance'
    print '    [4]  - Manhattan Distance'
    print '    [5]  - Pearson Correlation'
    print '    [6]  - Basic Stats - Vector'
    print '    [7]  - Basic Stats - Column'
    print '    [8]  - Standard Deviation - Vector'
    print '    [9]  - Standard Deviation - Collection'
    print '    [10] - Return to File Selection Menu'
   
    if data_file.filename == 'mydata/unittest.csv':
        print '    [11] - Test'
     
    file_option = 0

    while file_option != 10:
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
            if int(vector_index[0]) >= len(data_file.vectors) or int(vector_index[1]) >= len(data_file.vectors):
				    print "Error invalid index."
            else:
                print data_file.dot_product(int(vector_index[0]), int(vector_index[1]))    
        elif file_option == 3:
            vector_index = raw_input("Vector index pair: ").split(" ")
            if int(vector_index[0]) >= len(data_file.vectors) or int(vector_index[1]) >= len(data_file.vectors):
                print "Error invalid index."
            else:
                print data_file.euclidian(int(vector_index[0]), int(vector_index[1])) 
        elif file_option == 4:
            vector_index = raw_input("Vector index pair: ").split(" ")
            if int(vector_index[0]) >= len(data_file.vectors) or int(vector_index[1]) >= len(data_file.vectors):
                print "Error invalid index."
            else:
                print data_file.manhattan(int(vector_index[0]), int(vector_index[1])) 
        elif file_option == 5:
            vector_index = raw_input("Vector index pair: ").split(" ")
            if int(vector_index[0]) >= len(data_file.vectors) or int(vector_index[1]) >= len(data_file.vectors):
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
        elif file_option == 7:
            column = int(raw_input("Column: "))
            print "Vector: ", column, "\nmean: ", data_file.mean(column), "\nmedian: ", data_file.median(column), "\nsmallest: ",  data_file.smallest(column), "\nlargest: ", data_file.largest(column)  
        elif file_option == 8:
            column = int(raw_input("Column: "))
            print 'Standard deviation of values in column ', column, ': '
            print data_file.standard_dev_column(column)
        elif file_option == 9:
            vector_index = int(raw_input("Vector index: "))
            if vector_index >= len(data_file.vectors):
                print "Error invalid index."
            else:
                vector = data_file.vectors[vector_index]
                print "Standard deviation within vector ", vector_index, ": ", vector.standard_dev() 
        elif file_option == 10:
            return
        elif data_file.filename == 'mydata/unittest.csv':
            if file_option == 11:
                data_file.test() 
        else:
            print "Invalid operation." 

def run_test_suite():
    greater = raw_input("Find words with frequencies greater than: ")
    equal = raw_input("Find words with frequencies equal to: ")
    csvPath = 'data/csv'
    txtPath = 'data/text'

    output = ''

    output += "Grabbing CSV files...\n"
    csvList = os.listdir(csvPath)

    output += "Grabbing TXT files...\n"
    txtList = os.listdir(txtPath)

    output += "Beginning CSV tests\n\n"
    for fname in csvList:
        if fname.split('.')[1] != 'csv':
            continue
        filePath = os.path.join(csvPath, fname)
        data = CSVData(filePath)
        output += "Opening "
        output += fname
        output += "Parsing Vectors...\n"
        data.parse_vectors()


    output += "Beginning TXT tests\n\n"
    for fname in txtList:
        if fname.split('.')[1] != 'txt':
            continue
        filePath = os.path.join(txtPath, fname)
        data = TXTData(filePath) 
        output += "\nOpening "
        output += fname
        data.read_document()
        output += data.print_count_statistics()
        output += data.print_freq_statistics(equal, greater)

    f = open('output.test', 'w')
    f.write(output)
    f.close()

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

