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
    def execute(self, pipeddata, arrOptions):
        #  LoadTrainTestDatasets ./classification/iris_version3 | Display
        folder_name = ('./'+arrOptions[0]).split('/')        

        my_path = os.path.abspath(os.path.dirname(__file__))
        directory = os.path.join(my_path, "..","..", "..", "..", "datasets", *folder_name)
        ds_name = folder_name 

        alist = os.listdir(directory)
        K = len(alist)/2
        lds = LoadDataset.LoadDataset()
        base_folder = '/'.join(folder_name)
        result = []
        for index in range(K):
            f_train_path = base_folder+ '/train_'+str(index)+'.dat'
            instances = lds.execute(None,[f_train_path])
            result.append(instances)
            f_test_path = base_folder+ '/test_'+str(index)+'.dat'
            instances = lds.execute(None,[f_test_path])
            result.append(instances)


        return result
            



