from core.core.interfaces  import IFilter

class LoadDataset(IFilter.IFilter):
    def __init__(self):
        pass

    def getName(self):
        return "LoadDataset"    
    #return an array of instances or only one instance
    def execute(self, pipeddata, arrOptions):
        return "JAJA " + arrOptions[0]