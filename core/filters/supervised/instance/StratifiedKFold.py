from core.core.interfaces  import IFilter
import numpy as np
from sklearn.model_selection import StratifiedKFold as sciStratifiedKFold
from core.core  import Instances 

#LoadDataset path=./classification/iris.dat | StratifiedKFold n_splits=5 random_state=None shuffle=False | SaveTrainTestDatasets path=./classification/iris_version3 | Display

def codify(length, index):
    res = [0  for i in range(length)]
    res[index] = 1
    return res


class StratifiedKFold(IFilter.IFilter):

    def getName(self):
        return "StratifiedKFold"    

    def newInstance(self):
        return StratifiedKFold() 

    #return an array of instances or only one instance
    def execute(self, pipeddata=None, arrOptions=None):

        merged_dict = self.merge_two_dicts(self.arrOptions, arrOptions)
        n_splits=2
        random_state=None
        shuffle=False

        if('n_splits' in merged_dict):
            n_splits = int(merged_dict['n_splits'])

        if('random_state' in merged_dict and merged_dict['random_state'] != 'None'):
            random_state = int(merged_dict['random_state'])
        
        if('shuffle' in merged_dict):
            shuffle = merged_dict['shuffle'] == 'True'

        ds = pipeddata
        X = np.array(ds.getValues())
        y = np.array(ds.getClassesIndex())
        skf = sciStratifiedKFold(n_splits = n_splits, random_state = random_state, shuffle = shuffle)
        result = []
        num_classes = ds.getNumClasses()

        i = 0
        for train_index, test_index in skf.split(X, y):
            #print("TRAIN:", train_index, "TEST:", test_index)
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]
            y_train_coded = map(lambda i: codify(num_classes, i) , y_train)
            dst = Instances.Instances(X_train,  y_train_coded)
            dst.setName(ds.getName()+'_train_'+str(i))
            result.append(dst)
            y_test_coded = map(lambda i: codify(num_classes, i) , y_test)
            dst = Instances.Instances(X_test, y_test_coded)
            dst.setName(ds.getName()+'_test_'+str(i))
            result.append(dst)
            i += 1


        if(self.m_next_filter):
            self.m_next_filter.execute(result)
        #return result