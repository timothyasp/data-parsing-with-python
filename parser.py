import sys
import os.path

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
    print 'test'
    #infile = open(file, "r")
    #while infile: 
    #    line =
def parse_txt(filename):
    print 'test'
    #infile = open(file, "r")
    #while infile: 
    #    line =

if __name__ == '__main__':
    main()
   
