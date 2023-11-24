from main_menu.errors import  *

def get_validity(args):
    if ('-d' not in args) and ('-ds' not in args) and ('-df' not in args):
        return no_target()
    
    for i in range(len(args) - 1):
        if ((args[i] == '-d') and (args[i + 1][0] == '-')) or ((args[i] == '-d') and (args[i + 1][0] == '*')):
            return broken_target()
        
    if '-git' in sys.argv and '-git-token' not in sys.argv:
        return broken_github()