class Instances:

    def __init__(self, values, classes):
        self.values = values
        self.classes = classes
        self.num_classes = len(classes[0])

    def getNumInstances(self):
        return len(self.values)

    def getInstanceValues(self, index):
        return self.values[index]

    def getNumClasses(self):
        return len(self.classes[0])

    def getNumAttributes(self):
        return len(self.values[0])

    def getInstanceClasses(self, index):
        return self.classes[index]

    def getValues(self):
        return self.values

    def getClasses(self):
        return self.classes

    def getClassesIndex(self):
        return map(lambda r: r.index(1), self.classes)

    def __repr__(self):
        num_instances = self.getNumInstances()
        num_attributes = self.getNumAttributes()
        num_classes = self.getNumClasses()

        res = "\n----Print instances---------------------------------------------\n"
        res += "\nNumber of Classes: " + str(num_classes) +'\n'
        res += "Number of Attributes: " + str(num_attributes) +'\n'
        res +=  "Number of Instances: " + str(num_instances) +'\n'

        for i in range(num_instances):
            for j in range(num_attributes):
                print self.values[i][j], ',',
            print ' --> ',
            for j in range(num_classes):
                print self.classes[i][j], ',',
            print ''


        return res
