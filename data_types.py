import sys
import os.path
import csv
import math
import re

class Vector:
    def __init__(self, values):
        self.values = []
        for x in values:
            self.values.append(float(x))        
    
    def dump(self):
        print self.values
    
    def length(self):
        val = 0
        for x in self.values:
            x = x
            val += x*x
        return math.sqrt(val)

    def mean(self):
        val = 0
        for x in self.values:
            val += x;
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
        float_list = self.values
        mysum = 0
        sum_sqrs = 0

        for i in range(len(float_list)):
            mysum += float_list[i]
            sum_sqrs += float_list[i] * float_list[i]
        average = mysum / len(self.values)
        variance = sum_sqrs / len(self.values) - average * average

        return math.sqrt(variance)
  
 
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
    
    def test(self):
        print 'Testing VECTOR methods: '
        if self.vectors[2].length() == 2:
            print 'Passed vector length'
        if self.vectors[2].mean() - 0.44444444444 < .0001:
            print 'Passed vector mean'
        else: 
            print self.vectors[2].mean()
        if self.vectors[2].median() == 0:
            print 'Passed vector median test'
        if self.vectors[2].smallest() == 0:
            print 'Passed vector smallest test'
        if self.vectors[2].largest() == 1:
            print 'Passed vector largest test'
        if self.vectors[2].standard_dev() - .4969 < .001:
            print 'Passed vector standard dev test'    
        print 'Passed 6/6 vector methods...'
        print 'Testing CSVData methods:'
        
        
        return

class TXTData(Data):
    def __init__(self, filename):
        super(TXTData, self).__init__(filename)		  
        self.words = []
        self.paragraphs = []
        self.sentences = []

    def read_document(self):
        file_in = open(self.filename, 'r')
        self.document = Document(file_in.read())

    def paragraph_tokenize(self):
        if len(self.paragraphs) == 0:
            self.paragraphs = self.document.text.split("\n\n")
               
        return self.paragraphs;

    def sentence_tokenize(self):
        if len(self.sentences) == 0:
            sentence_reg_exp = re.compile(r"""
                (?:(?<=[.!?])|(?<=[.!?]['"])) # Match sentances ending with .! or ?              
                (?<!  Mr\.)(?<!  Mrs\.)(?<!  Jr\.)(?<!  Dr\.)(?<!  Prof\.)(?<!  Sr\.)(?<!  \.\.\.)\s+ # Exclude things that'll break early
                """, 
                re.IGNORECASE | re.VERBOSE)
            self.sentences = sentence_reg_exp.split(self.document.text)
        return self.sentences 

    def word_tokenize(self):
        if len(self.words) == 0:
            self.words = re.findall(r"""\w+(?:')\w+|\w+(?:-)\w+|\w+""", self.document.text)
        return self.words

    def unique_word_list(self):
        if len(self.words) == 0:
            self.word_tokenize()
 
        word_set = set()
        for x in self.words:
           word_set.add(x)
        return word_set   
         
    def unique_word_frequency(self):
        if len(self.words) == 0:
            self.word_tokenize()
       
        freq_dict = dict()
        for x in self.words:
            if freq_dict.has_key(x):
                freq_dict[x] += 1
            else:
                freq_dict[x] = 1 
        return freq_dict

    def print_count_statistics(self):
        print 'Length of document in words: ', len(self.word_tokenize())
        print 'Unique words: ', len(self.unique_word_list())
        print 'Sentence count: ', len(self.sentence_tokenize())
        print 'Paragraph count: ', len(self.paragraph_tokenize())
        return

    def print_freq_statistics(self, equal, greater):
        word_dict = self.unique_word_frequency() 
        greater_flist = []
        equal_flist = []
        highest_freq = 0
        highest_freq_list = []
      
        for x in word_dict.keys():
            if word_dict[x] > highest_freq:
                highest_freq_list = []
                highest_freq_list.append(x)
                highest_freq = word_dict[x]
            if word_dict[x] == highest_freq:
                highest_freq_list.append(x)  
            if word_dict[x] > int(greater):
                greater_flist.append(x)
            if word_dict[x] == int(equal):
                equal_flist.append(x)

        print 'Highest Frequency: ', highest_freq 
        print 'Words with frequency ', highest_freq
        print highest_freq_list
        print 'Words with frequency greater than ', greater
        print greater_flist
        print 'Words with frequency equal to ', equal
        print equal_flist
        return

    def word_search(self, word):
        word_dict = self.unique_word_frequency() 
        return word_dict.has_key(word)


class Document:
    def __init__(self, text):
        self.text = text
        self.word_count = -1 
        self.paragraph_count = -1
        self.sentence_count = -1

