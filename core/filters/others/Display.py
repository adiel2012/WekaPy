from core.core.interfaces  import IFilter

class Display(IFilter.IFilter):
    def __init__(self):
        pass

    def getName(self):
        return "Display"    
    #return an array of instances or only one instance
    def execute(self, pipeddata, arrOptions):
        print pipeddata
        return ""