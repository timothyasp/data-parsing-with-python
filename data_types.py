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
   
    def standard_dev_column(self, c1):
        float_list = []
        for x in vectors:
            float_list.append(x[c1])
        mean = sum(float_list)/len(float_list)
        for i in range(len(float_list)):
            float_list[i] -= mean
            float_list[i] *= float_list[i]

        list_sum = sum(float_list)
        stddev = Math.sqrt(list_sum / (len(float_list)-1))

        return stddev

    def standard_dev_vector(self, i1):
        float_list = vectors[i1]

        mean = sum(float_list)/len(float_list)
        for i in range(len(float_list)):
            float_list[i] -= mean
            float_list[i] *= float_list[i]
        list_sum = sum(float_list)
        stddev = Math.sqrt(list_sum / (len(float_list)-1))

        return stddev

    def dot_product(self, i1, i2):
        dot_product = 0
        for i in range(len(vectors[i1])):
            dot_product += vectors[i1][i] * vectors[i2][i]
        return dot_product
   
    def euclidian(self, i1, i2):
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
           return Math.sqrt(total)

    def manhattan(self, i1, i2):
        v1 = self.vectors[i1]
        v2 = self.vectors[i2]
        if len(v1) != len(v2): 
           print 'Error can not compute distance between unequal vector lengths.'
           return
        else:
           total = 0
           for i in range(len(v1)):
              val = v1[i] - v2[i]
              total += val
           return total

    def pearson(self, i1, i2):
        v1 = self.vectors[i1]
        v2 = self.vectors[i2]
        mean_v1 = sum(v1)/len(v1)
        mean_v2 = sum(v2)/len(v2) 
        std_v1 = standard_dev_vector(i1)
        std_v2 = standard_dev_vector(i2)
        
        pearson_cor = 0
        for i in range(len(v1)):
            pearson_cor += ((v1[i]-mean_v1) * (v2[i]-mean_v2))/((len(v1)-1)*std_v1*std_v2)
        return pearson_cor


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
        sentances = re.compile(r"""
            (?:(?<=[.!?])|(?<=[.!?]['"])) # Match sentances ending with .! or ?              
            (?<!  Mr\.)(?<!  Mrs\.)(?<!  Jr\.)(?<!  Dr\.)(?<!  Prof\.)(?<!  Sr\.)(?<!  \.\.\.)\s+ # Exclude things that'll break early
            """, 
            re.IGNORECASE | re.VERBOSE)

        return sentances.split(self.document.text)

    def word_tokenize(self):
        return re.findall(r'\w+', self.document.text)

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

