from core.core.interfaces  import IFilter

class Display(IFilter.IFilter):
    def __init__(self):
        pass
    
    def newInstance(self):
        return Display() 

    def getName(self):
        return "Display"    
    #return an array of instances or only one instance
    def execute(self, pipeddata = None, arrOptions = None):
        #print pipeddata
        print arrOptions