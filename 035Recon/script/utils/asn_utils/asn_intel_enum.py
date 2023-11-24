from enumeration.tools.gospider import *
from enumeration.tools.subdomainizer import *
from colorama import Fore
import threading
import sys
import enumeration.main_enum
from colorama import Fore
import threading
import sys

def run_asns(seeds):
        total_seeds = len(seeds)

        if '-t' in sys.argv:
            num_threads = None
            for i in range(len(sys.argv)):
                if sys.argv[i] == '-t':
                    num_threads = int(sys.argv[i + 1])
        else:
            num_threads = 1

        seeds_to_execute = [enumeration.main_enum.enum_init] * total_seeds

        def run_function():
            while seeds_to_execute:
                function = seeds_to_execute.pop()
                seed = seeds.pop()
                if function:
                    function(total_seeds - len(seeds_to_execute), seed)

        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=run_function)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        print(Fore.RED + "All ASN seeds have been enumerated.")

asns = set()

def add_asn(tool, asn):
    global asns
    asns.add((tool, asn))

def get_asns():
    global asns
    return asns

def get_asn_tool(tool):
    
    out = set()
    
    for i in get_asns():
        if i[0] == tool:
            out.add(i[1])
            
    return out
    
    
