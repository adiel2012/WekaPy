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




def runCMDs(cmds, result = None):
    
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

        filter = m_filters[name]
        if(isinstance(filter, CFork.IFork)):
            
            for params in filter.generate(splitted[1:]):
                nexts = cmds[i+1:]
                cpy = map(lambda v: v, nexts)                
                strparams = ' ' + params
                cpy[0] += strparams
                runCMDs(cpy, result)
            return
        else:
            result = filter.execute(result, splitted[1:])


runCMDs(cmds)