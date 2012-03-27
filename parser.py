import sys
import os.path
import csv

def main():
    if len(sys.argv) <= 1:
        print 'Error no file specified'
        return
    
    if not os.path.exists(sys.argv[1]) or not os.path.isfile(sys.argv[1]): 
        print 'Error can not find the specified file'
        return

    filetype = sys.argv[1].split('.')[1];
    if filetype == 'csv':
        parse_csv(sys.argv[1])
    elif filetype == 'txt':
        parse_txt(sys.argv[1])
    else:
        print 'Error unrecognized file type ', filetype
        return
    print 'Parsing file:', sys.argv[1]

def parse_csv(filename):
    reader = csv.reader(open(filename, 'r'))
    for row in reader:
        print row

def parse_txt(filename):
    infile = open(filename, "r")
    #while file:
    #    line = file.readline()
    #    print line.split(',')


if __name__ == '__main__':
    main()
   
