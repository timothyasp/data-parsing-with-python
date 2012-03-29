import sys
import os.path
import csv
import math

class Vector:
    def __init__(self, values):
        self.values = values
    def dump(self):
        print self.values
    def length(self):
        val = 0
        for x in self.values:
            x = float(x)
            val += x*x
        return math.sqrt(val)

    def largest(self):
        return
    def smallest(self):
        return
    def mean(self):
        return
    def median(self):
        return
    def standard_dev(self):
        return

class CSVData:
    def __init__(self, data):
        self.data = data
    @staticmethod
    def largest():
        return
    @staticmethod
    def smallest(vectors):
        return
    @staticmethod
    def mean(vectors):
        return
    @staticmethod
    def median(vectors):
        return
    @staticmethod
    def standard_dev(vectors):
        #ret = []
        #for (vector in vectors)
        #    ret.append(vector.standard_dev())
        #return ret
        return
    @staticmethod
    def dot_product(v1, v2):
        return
    @staticmethod
    def euclidian(v1, v2):
        return
    @staticmethod
    def manhattan(v1, v2):
        return
    @staticmethod
    def pearson(v1, v2):
        return
     

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
    mylist=[]
    j=0
    for row in reader:
        for i, x in enumerate(row):
            if len(x)< 1:
                x = row[i] = 0
        mylist.append(Vector(list(row)))
        print mylist[j].length()
        mylist[j].dump()
        j+=1


def parse_txt(filename):
    infile = open(filename, "r")
    #while file:
    #    line = file.readline()
    #    print line.split(',')


if __name__ == '__main__':
    main()

