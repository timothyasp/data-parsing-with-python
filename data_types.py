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

    def mean(self):
        return
 
    def median(self):
        return

    def largest(self):
        return

    def smallest(self):
        return

    def standard_ddev(self):
        return

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
            x.dump()

    def largest(self):
        return
   
    def smallest(self):
        return
   
    def mean(self):
        return
   
    def median(self):
        return
   
    def standard_dev(self, c1):
        return
   
    def dot_product(self, i1, i2):
        return
   
    def euclidian(self, i1, i2):
        return
   
    def manhattan(self, i1, i2):
        return
   
    def pearson(self, i1, i2):
        return
