from core.core.interfaces  import IFilter
import numpy as np
from sklearn.model_selection import StratifiedKFold as sciStratifiedKFold
from core.core  import Instances 

#LoadDataset ./classification/iris.dat | StratifiedKFold n_splits=5 random_state=None shuffle=False | SaveTrainTestDatasets ./classification/iris_version3 | Display

def codify(length, index):
    res = [0  for i in range(length)]
    res[index] = 1
    return res

def parseOptions(arrOptions):
    n_splits=2
    random_state=None
    shuffle=False
    for op in arrOptions:
        v = op.split('=')
        if(v[0] == 'n_splits'):
           n_splits = int(v[1]) 
        if(v[0] == 'shuffle'):
           shuffle = v[1] == 'True'

    return [n_splits, random_state, shuffle]

class StratifiedKFold(IFilter.IFilter):

    def getName(self):
        return "StratifiedKFold"    

    #return an array of instances or only one instance
    def execute(self, pipeddata, arrOptions):

        #n_splits=2, random_state=None, shuffle=False
        [n_splits, random_state, shuffle] = parseOptions(arrOptions)
        ds = pipeddata
        X = np.array(ds.getValues())
        y = np.array(ds.getClassesIndex())
        skf = sciStratifiedKFold(n_splits = n_splits, random_state = random_state, shuffle = shuffle)
        result = []
        num_classes = ds.getNumClasses()

        for train_index, test_index in skf.split(X, y):
            #print("TRAIN:", train_index, "TEST:", test_index)
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]
            y_train_coded = map(lambda i: codify(num_classes, i) , y_train)
            result.append(Instances.Instances(X_train,  y_train_coded))
            y_test_coded = map(lambda i: codify(num_classes, i) , y_test)
            result.append(Instances.Instances(X_test, y_test_coded))


        return result