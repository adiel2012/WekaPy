from core.core.interfaces  import IFilter
import numpy as np
from sklearn.model_selection import StratifiedKFold as sciStratifiedKFold
from core.core  import Instances 
import os.path

def parseOptions(arrOptions):
    pass

class SaveDataset(IFilter.IFilter):

    def getName(self):
        return "SaveDataset"    

    #return an array of instances or only one instance
    def execute(self, pipeddata, arrOptions):
        relative = arrOptions[0]
        ds = pipeddata
        num_classes = ds.getNumClasses()
        num_attributes = ds.getNumAttributes()
        num_instances = ds.getNumInstances()        

        parts = relative.split('/')

        #LoadDataset ./classification/iris.dat | SaveDataset ./classification/iris2.dat
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "..","..", "..", "..", "datasets", *parts)

        lines = []
        header = ''
        for i in range(num_attributes):
            header += '0,'
        for i in range(num_classes-1):
            header += '1,'
        header += '1\n'
        lines.append(header)
        values = ds.getValues()
        classes = ds.getClasses()

        for i in range(num_instances):
            line = ''
            for j in range(num_attributes):
                line += str(values[i][j])+','
            for j in range(num_classes):
                line +=  str(classes[i][j]) 
                if(num_classes-1!=j):
                    line += ','
            if(i != num_instances-1):
                line += '\n'
            lines.append(line)

        f = open(path, "a")
        f.writelines(lines)
        f.close()

        