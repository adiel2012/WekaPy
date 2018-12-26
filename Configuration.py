import core.filters.unsupervised.instance.LoadDataset as filters_unsupervised_instance_LoadDataset
import core.filters.unsupervised.instance.Display as filters_unsupervised_instance_Display
import core.filters.supervised.instance.StratifiedKFold as filters_supervised_instance_StratifiedKFold

import core.filters.unsupervised.instance.SaveDataset as filters_unsupervised_instance_SaveDataset
import core.filters.unsupervised.instance.SaveTrainTestDatasets as filters_unsupervised_instance_SaveTrainTestDatasets
import core.filters.unsupervised.instance.LoadTrainTestDatasets as filters_unsupervised_instance_LoadTrainTestDatasets
import core.filters.unsupervised.instance.ConvertDataSetToRegressionDS as filters_unsupervised_instance_ConvertDataSetToRegressionDS


import core.filters.others.CrossValidatorIFork as CCrossValidatorIFork


class Configuration:

    @staticmethod
    def getRegisteredFilters():
        result = {}
        #others
        attachFilter(result, filters_unsupervised_instance_LoadDataset.LoadDataset())
        attachFilter(result, filters_unsupervised_instance_Display.Display())
        attachFilter(result, filters_supervised_instance_StratifiedKFold.StratifiedKFold())        
        attachFilter(result, filters_unsupervised_instance_SaveDataset.SaveDataset())        
        attachFilter(result, filters_unsupervised_instance_SaveTrainTestDatasets.SaveTrainTestDatasets())        
        attachFilter(result, filters_unsupervised_instance_LoadTrainTestDatasets.LoadTrainTestDatasets())
        attachFilter(result, filters_unsupervised_instance_ConvertDataSetToRegressionDS.ConvertDataSetToRegressionDS())
        attachFilter(result, CCrossValidatorIFork.CrossValidatorIFork())
        

        return result


def attachFilter(obj, afilter):
    obj[afilter.getName()] = afilter