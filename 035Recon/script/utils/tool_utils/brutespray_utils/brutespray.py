import utils.file_utils.get_seeds
import utils.file_utils.tool_getters
import utils.file_utils.get_working_directory
import utils.validity_utils.get_validity
from enumeration.tools.subdomainizer import *
from vuln_scanning.tools.brutespray import *
import utils.file_utils.get_time
import utils.file_utils.subs
import threading

def run_brutespray(seeds):

    start_time = datetime.now().time()
    time_start = time.time()
    write_output(f"Beginning brutespray scanning at {str(start_time)[:-7]}")
    total_seeds = len(seeds)

    num_threads = utils.file_utils.tool_getters.get_spray_threads()

    brutespray = Brutespray('')

    seeds_to_execute = [brutespray.run] * total_seeds

    def run_function():
        while seeds_to_execute:
            function = seeds_to_execute.pop()
            seed = seeds.pop()
            if function:
                function(seed)

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=run_function)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()

    elapsed_time = end_time - time_start

    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)

    utils.file_utils.get_time.add_time(('brutespray', hours * 3600 + minutes * 60 + seconds))

    write_output(f"Brutespray scanning scanning done at {str(datetime.now().time())[:-7]} in {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")
    