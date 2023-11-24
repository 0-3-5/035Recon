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

class Alteration(Tool):
    def find_occurrences(self, input_string, target_char):
        return [i for i, char in enumerate(input_string) if char == target_char]


    def get_domains(self, domains):

        list = set()

        for domain in domains:
            d = domain.split('.')
            d = d[0]
            for i in '0123456789':
                occurances = self.find_occurrences(d, i)
                for o in occurances:
                    for num in '0123456789':
                        list.add(domain[:o] + num + domain[o + 1:])
        
        with open(f"{utils.file_utils.get_working_directory.get_wd()}/temp/alteration_subdomains_temp.txt", 'w') as file:
            for line in list:
                if line not in domains:
                    file.writelines(line + '\n')


    def run(self, domains):

        start_time = datetime.now().time()

        time_start = time.time()

        write_output(f"Beginning alteration scanning at {str(start_time)[:-7]}")

        make_dir(utils.file_utils.get_working_directory.get_wd() + '/alteration')
        make_dir(utils.file_utils.get_working_directory.get_wd() + '/temp')

        self.get_domains(domains)

        command = ["massdns", "-r", utils.file_utils.tool_getters.get_resolvers(), "-t", "A", "-o", "S", f"{utils.file_utils.get_working_directory.get_wd()}/temp/alteration_subdomains_temp.txt", "-w", f"{utils.file_utils.get_working_directory.get_wd()}/alteration/alteration_subdomains.txt"]
        subprocess.run(command)

        with open(f"{utils.file_utils.get_working_directory.get_wd()}/alteration/alteration_subdomains.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                x = line[:-1]
                y = x.split(' ')
                for z in y:
                    if z.count('.') >= 1:
                        utils.file_utils.subs.add_sub('alteration', z)

        end_time = time.time()

        elapsed_time = end_time - time_start

        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        utils.file_utils.get_time.add_time(('alteration', hours * 3600 + minutes * 60 + seconds))

        write_output(f"Alteration scanning done at {str(datetime.now().time())[:-7]} in {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")
        