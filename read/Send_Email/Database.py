from collections import namedtuple

class Database:
    '''
    This is a Database.py file

    It is basically read the given CSV file.
    it is a lazy iterator class and give the len() , next(), repr() like function.
      1) len() - give the no. of lines CSV file have.
      2) next() -  give the second line of CSV file.
      3) repr() - represent some relevent text of the Database class

    it has one argument - Path ( the path of the CSV file )
    
    '''
    def __init__(self,path):
        self.i = 1
        self.headers = ['Name','Score','Email']
        self.entry = namedtuple('Entry',self.headers)
        self.file = open(path)
        self.csv = self.file.readlines()
        self.len = len(self.csv)
        
    def __repr__(self):
        return f'Database(Size={self.len})'
    
    def __iter__(self):
        return self
    
    def __len__(self):
        return self.len

    def header(self):
        return self.headers
    
    def __next__(self):
        if self.i>=self.len:
            raise StopIteration
        else:
            lines = self.csv[self.i].strip('\n').split(',')
            result = self.entry(*lines)
            self.i += 1
            return result
        