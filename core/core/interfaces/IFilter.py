class IFilter:

    def __init__(self):
        self.m_next_filter = None
        self.arrOptions = []

    def newInstance(self):
        pass

    def merge_two_dicts(self, x, y):
        z = x.copy() if x else {}  # start with x's keys and values
        if(y):
            z.update(y)    # modifies z with y's keys and values & returns None
        return z

    def GetOptions(self):
        return self.arrOptions

    def SetOptions(self, value):
        self.arrOptions = value
        return self

    def SetNextFilter(self, ifilter):
        self.m_next_filter = ifilter
        return self

    def GetNextFilter(self):
        return self.m_next_filter

    def parseOptionsToDictionary(self, arrOptions):
        result = {}
        for op in self.arrOptions:
            v = op.split('=')
            if(len(v) > 1):
                result[v[0]] = v[1]

        for op in arrOptions:
            v = op.split('=')
            if(len(v) > 1):
                result[v[0]] = v[1]

        
        return result
    def getName(self):
        pass    
    #return an array of instances or only one instance
    def execute(self, pipeddata = None, arrOptions=None):
        pass