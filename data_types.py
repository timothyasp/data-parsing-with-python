import sys
import os.path
import csv
import math
import re
#import nltk

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
        val = 0
        for x in self.values:
            val += float(x);
        return val/len(self.values)
 
    def median(self):
        nums = sorted(self.values)
        size = len(nums)
        midPos = size / 2

        if size % 2 == 0:
            median = (nums[midPos] + nums[midPos-1]) / 2.0
        else:
            median = nums[midPos]

        return median

    def largest(self):
        max = float("-inf")
        for x in self.values:
            num = float(x)
            if num > max:
                max = num
            
        return max

    def smallest(self):
        min = float("inf")
        for x in self.values:
            num = float(x)
            if num < min:
                min = num
            
        return min

    def standard_dev(self):
        n = len(self.values)
        m = mean()
        for a in self.values:
            a = float(a)
            std = std + (a - m)**2
        return sqrt(std / float(n-1))

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

    def largest(self, c1):
        max_val = float("-inf")
        for x in self.vectors:
            if x[c1] >= max_val:
                max_val = x[c1]

        return max_val
   
    def  smallest(self, c1):
        min_val = float("inf")
        for x in self.vectors:
            if x[c1] <= min_val:
                min_val = x[c1] 
        return min_val
   
    def mean(self, c1):
        sum = 0;
        for x in self.vectors:
            sum += x[c1]
        return sum / len(self.vectors)
   
    def median(self, c1):
        float_list = []
        for x in self.vectors:
            float_list.append(x[c1])
        float_list = sorted(float_list)

        if len(float_list) % 2 == 0:
            low_index = int(len(float_list)/2)
            avg = float_list[low_index]
            avg += float_list[low_index+1]
            return float(avg/2)
        else: 
            return float_list[len(float_list)/2]
   
    def standard_dev(self, c1):
        return
   
    def dot_product(self, i1, i2):
        return
   
    def euclidian(self, i1, i2):
        val = manhattan(i1, i1);
        return Math.sqrt(val)

    def manhattan(self, i1, i2):
        v1 = vectors[i1]
        v2 = vectors[i2]
        if len(v1) != len(v2): 
           print 'Error can not compute distance between unequal vector lengths.'
           return
        else:
           total = 0
           for i in range(len(v1)):
              val = v1[i] - v2[i]
              val = val * val
              total += val
           return total

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
        #se_break = re.compile([.?!])
        #return se_break.split(self.document.text)
        #tokenizer = RegexpTokenizer(regexp)
        #sentences = regexp_tokenize(self.document.text, pattern=r'\.(\s+|$)', gaps=True)
        return

    def word_tokenize(self):
        return self.document.text.split();

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

