class Instances:

    def __init__(self, values, classes, num_classes = 1):
        self.values = values
        self.classes = classes
        self.num_classes = num_classes

    def getNumInstances(self):
        return len(self.values)

    def getInstanceValues(self, index):
        return self.values[index]

    def getInstanceClasses(self, index):
        return self.classes[index]

    def getValues(self):
        return self.values

    def getClasses(self):
        return self.classes