from core.core.interfaces  import IFilter
import numpy as np
from sklearn.model_selection import StratifiedKFold as sciStratifiedKFold
from core.core  import Instances 
import SaveDataset
import os
import shutil

#LoadDataset iris.dat | StratifiedKFold n_splits=5 random_state=None shuffle=False | SaveTrainTestDatasets iris_version3
def parseOptions(arrOptions):
    pass

class SaveTrainTestDatasets(IFilter.IFilter):

    def getName(self):
        return "SaveTrainTestDatasets"   

    def newInstance(self):
        return SaveTrainTestDatasets()  

    #return an array of instances or only one instance
    def execute(self, pipeddata=None, arrOptions=None):

        ds_name = self.merge_two_dicts(self.arrOptions, arrOptions)['path']
        datasets = pipeddata
        K = len(datasets)/2

        my_path = os.path.abspath(os.path.dirname(__file__))
        directory = os.path.join(my_path, "..","..", "..", "..", "datasets", *ds_name.split('/'))
        if(os.path.exists(directory)):
            shutil.rmtree(directory)

        os.mkdir(directory)
        for i in range(K):
            train = datasets[i*2]
            test = datasets[i*2+1]
            sds = SaveDataset.SaveDataset()
            sds.execute(train,[ds_name+'/'+train.getName()+'.dat'])
            sds.execute(test,[ds_name+'/'+test.getName()+'.dat'])

        if(self.m_next_filter):
            self.m_next_filter.execute(pipeddata) 
