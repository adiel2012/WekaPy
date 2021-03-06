import sys
import re 
import inspect
import core
import Configuration as conf
import core.core.interfaces.IFork as CFork 

num_params = len(sys.argv)

if(num_params == 1):
    print 'only one parameter needed'
    sys.exit()

def clean(str):
    res = re.sub(r'\s+',' ', str)
    res = res.strip()
    return res

m_filters = conf.Configuration.getRegisteredFilters()
cmds = sys.argv[1].split('|')


def ParseOptions(options):
    res = {}
    for i in options:
        v = i.split('=')
        if(len(v) > 1):
            res[v[0]] = v[1]
    return res

first = None
prev_filter = None
for i in range(len(cmds)):
    cmd = cmds[i]
    cmd = clean(cmd)
    splitted = cmd.split(" ")
    if(len(splitted) == 0):
        print 'empty name'
        sys.exit()

    name = splitted[0]
    if((name in m_filters) == False):
        print 'filter '+ name + ' not present'
        sys.exit()

    curr_filter = m_filters[name].newInstance().SetOptions(ParseOptions(splitted[1:]))

    if(prev_filter):
        prev_filter.SetNextFilter(curr_filter)
    else:
        first = curr_filter
    prev_filter = curr_filter
    


if(first):
    first.execute()



# PIPEDDATA DEBERIA PASARSE DICTIONARY COMO PYPEDDATA

#load dataset
#kfold
#split into pairs train test    # CADA DATASET DEBERIA TENER NOMBRE UNICO QUE AYUDE AL CONSOLIDADOR, CADA PASO DEBERIA VARIAR EL NOMBRE DEL DATASET
#CrossvalidateFork   entrada: X  salida X
#train classifier    entrada: par de datasets(train, test)   salida: evaluaciones(train, test) del classifier entrenado   
#metricaAll         entrada: salida del train classifier   salida: dictionary the metrics
#metricsConsolidator				salida: texto    CUANDO CONSOLIDAR METRICAS Y COMO
                                # IDEA 1 (EN EL DESTRUCTOR) USAR EL PYPED DATA PARA ALMACENAR EL CURRENT TRAIN-DATASET, CURRENT TEST DATASET, Y EL NOMBRE DE CADA DATASET
#