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
            if x.values[c1] >= max_val:
                max_val = x.values[c1]

        return max_val
   
    def smallest(self, c1):
        min_val = float("inf")
        for x in self.vectors:
            if x.values[c1] <= min_val:
                min_val = x.values[c1] 
        return min_val
   
    def mean(self, c1):
        float_list = []
        for x in self.vectors:
            float_list.append(x.values[c1])
        return sum(float_list)/len(float_list)
 
    def median(self, c1):
        float_list = []
        for x in self.vectors:
            float_list.append(x.values[c1])
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
        for x in self.vectors:
            float_list.append(x.values[c1])
        mysum = 0
        sum_sqrs = 0

        for i in range(len(float_list)):
            mysum += float_list[i]
            sum_sqrs += float_list[i] * float_list[i]
        average = mysum / len(float_list)
        variance = sum_sqrs / len(float_list) - average * average

        return math.sqrt(variance)

    def dot_product(self, i1, i2):
        dot_product = 0
        for i in range(len(self.vectors[i1].values)):
            dot_product += self.vectors[i1].values[i] * self.vectors[i2].values[i]
        return dot_product
   
    def euclidian(self, i1, i2):
        v1 = self.vectors[i1].values
        v2 = self.vectors[i2].values
        if len(v1) != len(v2): 
           print 'Error can not compute distance between unequal vector lengths.'
           return
        else:
           total = 0
           for i in range(len(v1)):
              val = v1[i] - v2[i]
              val = val * val
              total += val
           return math.sqrt(total)

    def manhattan(self, i1, i2):
        v1 = self.vectors[i1].values
        v2 = self.vectors[i2].values
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
        v1 = self.vectors[i1].values
        v2 = self.vectors[i2].values
        mean_v1 = sum(v1)/len(v1)
        mean_v2 = sum(v2)/len(v2) 
        std_v1 = self.vectors[i1].standard_dev()
        std_v2 = self.vectors[i2].standard_dev() 
        
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
        
        if self.mean(0) - .3333333 < .0001:
            print 'Passed column mean'
        if self.median(0) == 0:
            print 'Passed column median'
        if self.largest(0) == 1:
            print 'Passed column largest'
        if self.smallest(0) == 0:
            print 'Passed column smallest'
        if self.standard_dev_column(0) -.4717 < .001:
            print 'Passed column stddev'
        else:
            print self.standard_dev_column(0)
        
        if self.dot_product(1, 2) == 4.0:
            print 'Passed dot product'
        else:
            print self.dot_product(1, 2)
        if self.euclidian(1, 2) - 2.236 < .001 :
            print 'Passed vectors dot product'
        else:
            print self.euclidian(1,2)
        if self.manhattan(1, 2) == 5.0:
            print 'Passed vectors manhattan'
        else: 
            print self.manhattan(1,2)
        if self.pearson(2, 2) - 1.125 < .001:
            print 'Passed vectors pearson'
        else:
            print self.pearson(2, 2)
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
        output = ''
        output += '\nLength of document in words: ' 
        output += str(len(self.word_tokenize()))
        output += '\nUnique words: ' 
        output += str(len(self.unique_word_list()))
        output += '\nSentence count: ' 
        output += str(len(self.sentence_tokenize()))
        output += '\nParagraph count: ' 
        output += str(len(self.paragraph_tokenize()))
        return output

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

        output = ''

        output += '\nHighest Frequency: '
        output += str(highest_freq)
        output += '\nWords with highest frequency '
        output += str(highest_freq)
        output += ': '
        output += str(len(highest_freq_list))
        #print highest_freq_list
        output += '\nWords with frequency greater than ' 
        output += str(greater)
        output += ': '
        output += str(len(greater_flist))
        #print greater_flist
        output += '\nWords with frequency equal to '
        output += str(equal)
        output += ': '
        output += str(len(equal_flist))
        #print equal_flist
        output += "\n\n"
        return output

    def word_search(self, word):
        word_dict = self.unique_word_frequency() 
        return word_dict.has_key(word)

class Document:
    def __init__(self, text):
        self.text = text
        self.word_count = -1 
        self.paragraph_count = -1
        self.sentence_count = -1

