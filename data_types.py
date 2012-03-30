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


class Data(object):
    def __init__(self, fn):
        self.filename = fn
        self.filetype = fn.split('.')[1]


class TextData(Data):
    def __init__(self, filename):
        super(CSVData, self).__init__(filename)		  


class CSVData(Data):
    def __init__(self, fn):
        super(CSVData, self).__init__(fn)		  
	
    def parse_vectors(self):
        reader = csv.reader(open(self.filename, 'r'))
        self.vectors=[]

        for row in reader:
            for i, x in enumerate(row):
                if len(x)< 1:
                    x = row[i] = 0
            self.vectors.append(Vector(list(row)))
    
    def print_vectors(self):
        for x in self.vectors:
            print x.dump()

    def largest():
        return
   
    def smallest():
        return
   
    def mean():
        return
   
    def median():
        return
   
    def standard_dev():
        return
   
    def dot_product(i1, i2):
        return
   
    def euclidian(i1, i2):
        return
   
    def manhattan(i1, i2):
        return
   
    def pearson(i1, i2):
        return
