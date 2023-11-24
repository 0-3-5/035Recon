from enumeration.tools.amass import *
from enumeration.tools.harvester import *
from enumeration.tools.subfinder import *
from enumeration.tools.assetfinder import *
from enumeration.tools.github import *
from enumeration.tools.gospider import *
from enumeration.tools.subdomainizer import *
from enumeration.tools.bruteforcer import *
from utils.file_utils.tool_getters import *
import enumeration.custom_enum
import threading
import sys

def enum_init(count, seed):
    def amass():
        if get_amass():
            for i in range(get_amass_exec1()):
                a = Amass(seed)
                a.run(seed)

    def harvester():
        if get_harvester():
            for i in range(get_harvester_exec()):
                a = TheHarvester(seed)
                a.run(seed)

    def subfinder():
        if get_subfinder():
            for i in range(get_subfinder_exec()):
                a = Subfinder(seed)
                a.run(seed)

    def assetfinder():
        if get_assetfinder():
            for i in range(get_assetfinder_exec()):
                a = Assetfinder(seed)
                a.run(seed)

    def github():
        if get_github():
            for i in range(get_github_exec()):
                a = Github(seed)
                a.run(seed)

    def link_go():
        if get_link_go():
            for i in range(get_link_go_exec()):
                a = Gospider(seed)
                a.run(seed, 'gospider')

    def link_sub():
        if get_link_sub():
            for i in range(get_link_sub_exec()):
                a = Subdomainizer(seed)
                a.run(seed, 'subdomainizer')

    def brute():
        if get_brute():
            for i in range(get_brute_exec()):
                a = Bruteforcer(seed)
                a.run(seed)

    threads = []

    func_list = [amass, harvester, subfinder, assetfinder, github, link_go, link_sub, brute]

    use_list = func_list + enumeration.custom_enum.custom_init(seed)

    for func in use_list:
        thread = threading.Thread(target=func)
        threads.append(thread)

    for thread in threads:
        thread.start()
        if '-m' not in sys.argv:
            thread.join()

    for thread in threads:
        thread.join()