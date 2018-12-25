import sys
import re 
import inspect
import core
import Configuration as conf

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

result = None

for cmd  in cmds:
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

    result = filter.execute(result, splitted[1:])


