import core.filters.others.LoadDataset as filters_others_LoadDataset
import core.filters.others.Display as filters_others_Display



class Configuration:

    @staticmethod
    def getRegisteredFilters():
        result = {}
        #others
        attachFilter(result, filters_others_LoadDataset.LoadDataset())
        attachFilter(result, filters_others_Display.Display())

        return result


def attachFilter(obj, afilter):
    obj[afilter.getName()] = afilter