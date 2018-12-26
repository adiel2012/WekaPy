from core.core.interfaces  import IFilter
from core.core.interfaces  import IFork
from core.core  import Instances 
import os.path
import numpy as np

#LoadDataset ./timeserie/daily-minimum-temperatures-in-me.dat | CrossValidatorIFork p1={a,b,c} p2={d,e} | Display
def generateCombinations(optionsName, optionsvalues):

        n = len(optionsvalues)

        optionsName_cpy = optionsName[:]
        optionsvalues_cpy = optionsvalues[:]

        fname = optionsName_cpy.pop()
        fvalues = optionsvalues_cpy.pop()
        if(n == 1):
            for fvalue in fvalues:
                yield fname + '=' + fvalue
        else:
            for i in generateCombinations(optionsName_cpy[:], optionsvalues_cpy[:]):
                for fvalue in fvalues:
                    yield fname + '=' + fvalue + ' ' + i

class CrossValidatorIFork(IFilter.IFilter, IFork.IFork):
    def getName(self):
        return 'CrossValidatorIFork'    

    #return an array of instances or only one instance
    def execute(self, pipeddata, arrOptions):
        return pipeddata

    

    def generate(self, arrOptions):
        adict = self.parseOptionsToDictionary(arrOptions)
        optionsName = []
        optionsvalues = [] 
        for key in adict:
            value = adict[key]
            optionsName.append(key)
            values = value.replace('{', '').replace('}', '').split(',')
            optionsvalues.append(values)

        for i in generateCombinations(optionsName, optionsvalues):
            yield i

