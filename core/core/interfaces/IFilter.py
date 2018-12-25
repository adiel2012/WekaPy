class IFilter:

    def parseOptionsToDictionary(self, arrOptions):
        result = {}
        for op in arrOptions:
            v = op.split('=')
            if(len(v) > 1):
                result[v[0]] = v[1]
        return result
    def getName(self):
        pass    
    #return an array of instances or only one instance
    def execute(self, pipeddata, arrOptions):
        pass