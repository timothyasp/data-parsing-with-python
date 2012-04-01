import sys
import os.path
import csv
import math
import nltk

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


class TXTData(Data):
    def __init__(self, filename):
        super(TXTData, self).__init__(filename)		  

    def read_document(self):
        file_in = open(self.filename, 'r')
        self.document = Document(file_in.read())

    def paragraph_tokenize(self):
        paragraphs = self.document.text.split("\n\n")
        this.document.paragraph_count = len(paragraphs)
        return paragraphs;

    def sentence_tokenize(self):
        regexp = r'\.(\s+|$)'
        #tokenizer = RegexpTokenizer(regexp)
        #sentences = regexp_tokenize(self.document.text, pattern=r'\.(\s+|$)', gaps=True)
        return 

    def word_tokenize(self):
        return

    def print_unique_word_list(self):
        return

    def print_unique_word_frequency(self):
        return

    def print_count_statistics(self):
        return

    def word_search(self, word):
        return


class Document:
    def __init__(self, text):
        self.text = text
        self.word_count = -1 
        self.paragraph_count = -1
        self.sentence_count = -1

