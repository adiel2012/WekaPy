#ConvertDataSetToRegressionDS
from core.core.interfaces  import IFilter
from core.core import Instances

class ConvertDataSetToRegressionDS(IFilter.IFilter):
    def __init__(self):
        pass

#LoadDataset ./timeserie/daily-minimum-temperatures-in-me.dat | ConvertDataSetToRegressionDS K=4 | Display
    def getName(self):
        return "ConvertDataSetToRegressionDS"    


    def newInstance(self):
        return ConvertDataSetToRegressionDS() 
    #return an array of instances or only one instance
    def execute(self, pipeddata = None, arrOptions = None):
        ds = pipeddata

        parsed = self.parseOptionsToDictionary(arrOptions)
        K = 3
        if('K' in parsed):
            K = int(parsed['K'])
        
        num_instanced = ds.getNumInstances()
        values_arr = map(lambda r: map(lambda v: v, r) , ds.getValues()) #[v for row in ds.getValues() for v in row ]
        classes_arr = map(lambda r: map(lambda v: v, r) , ds.getClasses())

        values = []
        classes = []

        num_iter = num_instanced-K
        for i in range(num_iter):
            line = []
            class_line = map(lambda r: r, classes_arr[K-1+i])
            for j in range(K):
                line = line + map(lambda r: r, values_arr[i+j])
                if(j != K-1):
                    line = line + map(lambda r: r, classes_arr[i+j])
            values.append(line)
            classes.append(class_line)

        if(self.m_next_filter):
            self.m_next_filter.execute(Instances.Instances(values, classes))
        #return Instances.Instances(values, classes)