from core.core.interfaces  import IFilter
import numpy as np
from sklearn.model_selection import StratifiedKFold as sciStratifiedKFold
from core.core  import Instances 
import LoadDataset
import os
import shutil



class LoadTrainTestDatasets(IFilter.IFilter):

    def getName(self):
        return "LoadTrainTestDatasets"    

    #return an array of instances or only one instance
    def execute(self, pipeddata=None, arrOptions=None):
        #  LoadTrainTestDatasets path=./classification/iris_version5 | Display
        folder_name = self.merge_two_dicts(self.arrOptions, arrOptions)['path'].split('/')       

        my_path = os.path.abspath(os.path.dirname(__file__))
        directory = os.path.join(my_path, "..","..", "..", "..", "datasets", *folder_name)
        #ds_name = folder_name 

        alist = os.listdir(directory)

         
        K = len(alist)/2
        result = ['' for i in range(2*K)]

        lds = LoadDataset.LoadDataset()
        base_folder = '/'.join(folder_name)
        nf = ResultKeep()
        #result = []
        for f in alist:
            temp = f[0:-4]
            parts = temp.split('_')
            pos = 2*int(parts[len(parts)-1]) 
            if(parts[len(parts)-2] == 'test'):
                pos += 1
            lds.SetNextFilter(nf)
            lds.execute(None,{"path":base_folder + '/'+ f})
            result[pos] = nf.result

        
      


        if(self.m_next_filter):
            self.m_next_filter.execute(result) 
        #return result
            
    def newInstance(self):
        return LoadTrainTestDatasets() 


class ResultKeep(IFilter.IFilter):

    def __init__(self):
        self.result = None

    def getName(self):
        return "none"    

    #return an array of instances or only one instance
    def execute(self, pipeddata=None, arrOptions=None):
        self.result = pipeddata