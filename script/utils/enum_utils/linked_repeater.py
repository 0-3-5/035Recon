import utils.file_utils.get_seeds
import utils.file_utils.get_working_directory
import utils.validity_utils.get_validity
from enumeration.tools.gospider import *
from enumeration.tools.subdomainizer import *
from colorama import Fore
import utils.file_utils.subs
import threading
import sys


def run_go(seeds):
    total_seeds = len(seeds)

    if '-t' in sys.argv:
        num_threads = None
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-t':
                num_threads = int(sys.argv[i + 1])
    else:
        num_threads = 1

    gospider = Gospider('')

    seeds_to_execute = [gospider.run] * total_seeds

    def run_function():
        while seeds_to_execute:
            function = seeds_to_execute.pop()
            seed = seeds.pop()
            if function:
                function(seed, 'gospider-all')

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=run_function)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(Fore.RED + "All subdomains have been enumerated using subdomainizer.")

def run_sub(seeds):
    total_seeds = len(seeds)

    if '-t' in sys.argv:
        num_threads = None
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-t':
                num_threads = int(sys.argv[i + 1])
    else:
        num_threads = 1

    subdomainizer = Subdomainizer('')

    seeds_to_execute = [subdomainizer.run] * total_seeds

    def run_function():
        while seeds_to_execute:
            function = seeds_to_execute.pop()
            seed = seeds.pop()
            if function:
                function(seed, 'subdomainizer-all')

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=run_function)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(Fore.RED + "All subdomains have been enumerated using subdomainizer.")
    