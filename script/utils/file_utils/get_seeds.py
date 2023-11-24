import sys

def get_seeds():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-d':
            return [sys.argv[i + 1]]
        
        if sys.argv[i] == '-ds':
            list = sys.argv[i + 1].split(',')
            clist = []
            for i in list:
                clist.append(i)
            return clist
        
        if sys.argv[i] == '-df':
            list = []
            with open(sys.argv[i + 1], 'r') as file:
                words = file.readlines()
                for ii in words:
                    list.append(ii[:-1])
            return list
        

def get_scope():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-s':
            list = []
            with open(sys.argv[i + 1], 'r') as file:
                words = file.readlines()
                for ii in words:
                    list.append(ii[:-1])
            return list
        
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-ss':
            return get_seeds()
