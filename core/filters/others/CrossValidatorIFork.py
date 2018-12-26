from core.core.interfaces  import IFilter
from core.core.interfaces  import IFork
from core.core  import Instances 
import os.path
import numpy as np
import copy

#LoadDataset path=./timeserie/daily-minimum-temperatures-in-me.dat | CrossValidatorIFork p1={a,b,c} p2={d,e} | Display
def generateCombinations(optionsName, optionsvalues):

        n = len(optionsvalues)

        optionsName_cpy = optionsName[:]
        optionsvalues_cpy = optionsvalues[:]

        fname = optionsName_cpy.pop()
        fvalues = optionsvalues_cpy.pop()
        if(n == 1):
            for fvalue in fvalues:
                res = {}
                res[fname] = fvalue
                yield res
        else:
            for i in generateCombinations(optionsName_cpy[:], optionsvalues_cpy[:]):
                for fvalue in fvalues:
                    it = copy.deepcopy(i)
                    it[fname] = fvalue
                    yield it

class CrossValidatorIFork(IFilter.IFilter, IFork.IFork):
    def getName(self):
        return 'CrossValidatorIFork'   

    def newInstance(self):
        return CrossValidatorIFork() 

    #return an array of instances or only one instance
    def execute(self, pipeddata=None, arrOptions=None):
        if(self.m_next_filter):            
            for i in self.generate( self.merge_two_dicts(self.arrOptions, arrOptions) ):
                self.m_next_filter.execute(pipeddata, i) 

    

    def generate(self, arrOptions):
        adict = arrOptions
        optionsName = []
        optionsvalues = [] 
        for key in adict:
            value = adict[key]
            optionsName.append(key)
            values = value.replace('{', '').replace('}', '').split(',')
            optionsvalues.append(values)

        for i in generateCombinations(optionsName, optionsvalues):
            yield i

