import utils.file_utils.get_working_directory
import sys
import os

def get_amass():
    if '-all-recon' in sys.argv or '-amass' in sys.argv:
        return True
    return False

def get_alt():
    if '-all-recon-short' in sys.argv or '-all-recon' in sys.argv or '-alt' in sys.argv:
        return True
    return False

def get_amass_exec():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-amass-exec':
            return sys.argv[i + 1]
    return 9999999

def get_harvester():
    if '-all-recon-short' in sys.argv or '-all-recon' in sys.argv or '-harv' in sys.argv:
        return True
    return False

def get_subfinder():
    if '-all-recon-short' in sys.argv or '-all-recon' in sys.argv or '-sub' in sys.argv:
        return True
    return False

def get_assetfinder():
    if '-all-recon-short' in sys.argv or '-all-recon' in sys.argv or '-asset' in sys.argv:
        return True
    return False

def get_github():
    if '-all-recon-short' in sys.argv or '-all-recon' in sys.argv or '-git' in sys.argv:
        return True
    return False

def get_git_token():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-git-token':
            return sys.argv[i + 1]
        
def get_link_go():
    if '-all-recon-short' in sys.argv or '-all-recon' in sys.argv or '-link-go' in sys.argv:
        return True
    return False

def get_spray():
    if '-all-vuln' in sys.argv or '-spray' in sys.argv:
        return True
    return False

def get_link_sub():
    if '-all-recon-short' in sys.argv or '-all-recon' in sys.argv or '-link-sub' in sys.argv:
        return True
    return False

def get_link_go_all():
    if '-all-recon' in sys.argv or '-link-go-all' in sys.argv:
        return True
    return False

def get_link_sub_all():
    if '-all-recon' in sys.argv or '-link-sub-all' in sys.argv:
        return True
    return False

def get_link_go_exec():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-link-go-count':
            return int(sys.argv[i + 1])
    return 1

def get_alt_exec():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-alt-count':
            return int(sys.argv[i + 1])
    return 1

def get_link_sub_exec():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-link-sub-count':
            return int(sys.argv[i + 1])
        return 1

def get_link_go_all_exec():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-link-go-all-count':
            return int(sys.argv[i + 1])
    return 1

def get_link_sub_all_exec():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-link-sub-all-count':
            return int(sys.argv[i + 1])
    return 1

def get_brute_exec():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-brute-count':
            return int(sys.argv[i + 1])
    return 1

def get_harvester_exec():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-harv-count':
            return int(sys.argv[i + 1])
    return 1

def get_subfinder_exec():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-sub-count':
            return int(sys.argv[i + 1])
    return 1

def get_assetfinder_exec():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-asset-count':
            return int(sys.argv[i + 1])
    return 1

def get_takeover_exec():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-take-count':
            return int(sys.argv[i + 1])
    return 1

def get_github_exec():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-git-count':
            return int(sys.argv[i + 1])
    return 1

def get_spray_exec():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-spray-count':
            return int(sys.argv[i + 1])
    return 1

def get_nuclei_threads():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-nuclei-t':
            return int(sys.argv[i + 1])
    return 10

def get_screenshot_threads():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-screenshot-t':
            return int(sys.argv[i + 1])
    return 20

def get_screenshot():
    return True

def get_spray_threads():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-spray-t':
            return int(sys.argv[i + 1])
    return 25

def get_resolvers():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-resolvers':
            return sys.argv[i + 1]
    return f"{os.path.dirname(os.path.abspath(sys.argv[0]))}/utils/tool_utils/resolver_utils/resolvers.txt"

def get_take_threads():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-take-t':
            return int(sys.argv[i + 1])
    return 100

def get_social_threads():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-social-t':
            return int(sys.argv[i + 1])
    return 100

def get_nuclei_templates():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-nuclei-c':
            return sys.argv[i + 1]
    return None

def get_nuclei_exec():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-nuclei-count':
            return int(sys.argv[i + 1])
    return 1

def get_social_exec():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-social-count':
            return int(sys.argv[i + 1])
    return 1

def get_amass_exec1():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-amass-count':
            return int(sys.argv[i + 1])
    return 1

def get_asns():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-casns':
            list = sys.argv[i + 1].split(',')
            clist = []
            for i in list:
                clist.append(i)
            return clist
        
        if sys.argv[i] == '-asns':
            list = []
            with open(sys.argv[i + 1], 'r') as file:
                words = file.readlines()
                for ii in words:
                    list.append(ii[:-1])
            return list
        return []
    
def get_rec():
    if '-rec' in sys.argv:
        return True
    return False

def get_brute():
    if '-all-recon' in sys.argv or '-brute' in sys.argv:
        return True
    return False

def get_takeover():
    if '-all-vuln' in sys.argv or '-take' in sys.argv:
        return True
    return False

def get_nuclei():
    if '-all-vuln' in sys.argv or '-nuclei' in sys.argv:
        return True
    return False

def get_social():
    if '-all-vuln' in sys.argv or '-social' in sys.argv:
        return True
    return False

def get_brute_list():
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == '-brute-list':
            list = []
            with open(sys.argv[i + 1], 'r') as file:
                words = file.readlines()
                for ii in words:
                    list.append(ii[:-1])
            return list
    with open(f"{os.path.dirname(os.path.abspath(sys.argv[0]))}/utils/tool_utils/bruteforcing_utils/subdomains.txt", 'r') as file:
        return [x[:-1] for x in file.readlines()]
    
custom_enum = {}
custom_vuln = {}

def get_custom_enum():
    if custom_enum:
        return custom_enum
    else:
        try:
            os.mkdir(utils.file_utils.get_working_directory.get_wd() + '/custom')
        except:
            pass
        for i in range(len(sys.argv) - 1):
            if sys.argv[i] == '-cr':
                if '.txt' in sys.argv[i + 1]:
                    with open(sys.argv[i + 1], 'r') as file:
                        line = [x[:-1] for x in file.readlines()]
                    custom_enum[sys.argv[i + 1]] = line
                else:
                    for root, dirs, files in os.walk(sys.argv[i + 1]):
                        for file in files:
                            if file.endswith(".txt"):
                                with open(f"{sys.argv[i + 1]}/{file}", 'r') as in_file:
                                    line = [x[:-1] for x in in_file.readlines()]
                                custom_enum[file] = line
        return custom_enum
    
def get_custom_vuln():
    if custom_vuln:
        return custom_vuln
    else:
        try:
            os.mkdir(utils.file_utils.get_working_directory.get_wd() + '/custom_vuln')
        except:
            pass
        for i in range(len(sys.argv) - 1):
            if sys.argv[i] == '-cv':
                if '.txt' in sys.argv[i + 1]:
                    with open(sys.argv[i + 1], 'r') as file:
                        line = [x[:-1] for x in file.readlines()]
                    custom_vuln[sys.argv[i + 1]] = line
                else:
                    for root, dirs, files in os.walk(sys.argv[i + 1]):
                        for file in files:
                            if file.endswith(".txt"):
                                with open(f"{sys.argv[i + 1]}/{file}", 'r') as in_file:
                                    line = [x[:-1] for x in in_file.readlines()]
                                custom_vuln[file] = line
        return custom_vuln
    

def get_custom_vuln_t(name):
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == name:
            return int(sys.argv[i + 1])
    return 1

def get_cname():
    if '-all-recon-short' in sys.argv or '-all-recon' in sys.argv or '-cname' in sys.argv:
        return True
    return False

def get_similar():
    if '-similar' in sys.argv:
        return True
    return False



