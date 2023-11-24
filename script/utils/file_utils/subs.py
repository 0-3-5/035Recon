import utils.file_utils.get_seeds
import sys

seeds = set()

def get_subs():
    return seeds

def add_sub(tool, domain):
    if '-s' in sys.argv or '-ss' in sys.argv:
        for x in utils.file_utils.get_seeds.get_scope():
            if domain.find(x) != -1:
               if domain != '\n' and domain != ' ' and domain != '':
                seeds.add((tool, domain))
               return
    else:
        if domain != '\n' and domain != ' ' and domain != '':
            seeds.add((tool, domain))

def set_subs(subs):
    global seeds
    seeds = subs