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

