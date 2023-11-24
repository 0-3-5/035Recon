import utils.file_utils.get_seeds
import utils.file_utils.get_working_directory
import utils.validity_utils.get_validity
from enumeration.tools.subdomainizer import *
import vuln_scanning.vulns
import utils.file_utils.tool_getters
import utils.file_utils.subs
import threading
import utils.file_utils.get_time
from utils.file_utils.output_writer import *

class Nuclei(Tool):
    def run(self, domain):

        try:
            os.mkdir(utils.file_utils.get_working_directory.get_wd() + '/nuclei')
        except:
            pass

        command = ['nuclei', '-u', f"{domain}", '--no-color']
        if get_nuclei_templates() != None:
            command = ['nuclei', '-u', f"{domain}", '--no-color', '-t', get_nuclei_templates()]
        result = subprocess.run(command, stdout=subprocess.PIPE)

        lines = result.stdout.decode('utf-8').splitlines()

        for line in lines:
            print(line)
            l = line.split(' ')
            if 'info' not in l[2]:
                vuln_scanning.vulns.add_vuln_info('nuclei', l[3], l[0][1:][:-1] + ':' + l[4][2:][:-1], l[2][1:][:-1])


def run_nuclei(seeds):

    start_time = datetime.now().time()
    time_start = time.time()
    write_output(f"Beginning nuclei scanning at {str(start_time)[:-7]}")

    total_seeds = len(seeds)

    num_threads = utils.file_utils.tool_getters.get_nuclei_threads()

    nuclei = Nuclei('')

    seeds_to_execute = [nuclei.run] * total_seeds

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

    utils.file_utils.get_time.add_time(('nuclei', hours * 3600 + minutes * 60 + seconds))

    write_output(f"Nuclei scanning done at {str(datetime.now().time())[:-7]} in {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")
    