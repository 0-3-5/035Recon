import subprocess
from enumeration.tool_class import *
import utils.file_utils.get_working_directory
from utils.file_utils.output_writer import *
from utils.file_utils.dir_creator import *
import utils.file_utils.get_time
import utils.file_utils.tool_getters
from datetime import datetime
import utils.file_utils.subs
import time

class Bruteforcer(Tool):
    def get_domains(self, domain):
        list = []

        for i in utils.file_utils.tool_getters.get_brute_list():
            list.append(i + '.' + domain + '\n')

        with open(f"{utils.file_utils.get_working_directory.get_wd()}/temp/brute_subdomains_temp.txt", 'w') as file:
            file.writelines(list)

    def run(self, domain):

        start_time = datetime.now().time()

        time_start = time.time()

        write_output(f"Beginning bruteforcing subdomains for {domain} at {str(start_time)[:-7]}")

        make_dir(utils.file_utils.get_working_directory.get_wd() + '/bruteforce')
        make_dir(utils.file_utils.get_working_directory.get_wd() + '/temp')

        self.get_domains(domain)

        command = ["massdns", "-r", utils.file_utils.tool_getters.get_resolvers(), "-t", "A", "-o", "S", f"{utils.file_utils.get_working_directory.get_wd()}/temp/brute_subdomains_temp.txt", "-w", f"{utils.file_utils.get_working_directory.get_wd()}/bruteforce/bruteforced_subdomains.txt"]
        subprocess.run(command)

        with open(f"{utils.file_utils.get_working_directory.get_wd()}/bruteforce/bruteforced_subdomains.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                x = line[:-1]
                y = x.split(' ')
                for z in y:
                    if z.count('.') >= 1:
                        utils.file_utils.subs.add_sub('bruteforce', z)

        end_time = time.time()

        elapsed_time = end_time - time_start

        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        utils.file_utils.get_time.add_time(('bruteforce', hours * 3600 + minutes * 60 + seconds))

        write_output(f"Bruteforcing subdomains done for {domain} at {str(datetime.now().time())[:-7]} in {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")
        