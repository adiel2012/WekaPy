from core.core.interfaces  import IFilter
from core.core  import Instances 
import os.path
import numpy as np

def clean(str):
    return str.strip().replace(" ", "")

class LoadDataset(IFilter.IFilter):
    def __init__(self):
        pass

    def getName(self):
        return "LoadDataset"    
    #return an array of instances or only one instance
    def execute(self, pipeddata, arrOptions):
        dataset_name = arrOptions[0]
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "..","..", "..", "datasets", "classification", dataset_name)

        f = open(path, "r")
        # use readlines to read all lines in the file
        # The variable "lines" is a list containing all lines in the file
        lines = f.readlines()
        # close the file after reading the lines.
        f.close()
        colums_description = clean(lines[0]).split(',')
        num_classes = 0
        num_attributes = 0
        for c in colums_description:
            if(c == '0'):
                num_attributes += 1
            else:
                num_classes += 1

        num_records = len(lines)-1
        values = [[float(0)] * num_attributes for i in range(num_records)] 
        classes = [[float(0)] * num_classes for i in range(num_records)]
        for ri in range(1,num_records+1):
            vals = clean(lines[ri]).split(',')
            for ind in range(num_attributes):
                values[ri-1][ind] = float(vals[ind])
            for ind in range(num_classes):
                classes[ri-1][ind] = float(vals[num_attributes+ind])

        return Instances.Instances(values, classes)