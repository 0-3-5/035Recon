import subprocess
from enumeration.tool_class import *
import utils.file_utils.get_working_directory
from utils.file_utils.output_writer import *
from utils.file_utils.dir_creator import *
import utils.file_utils.tool_getters
from utils.file_utils.get_seeds import *
import utils.file_utils.get_time
from datetime import datetime
import utils.file_utils.subs
import time
import os
import sys

class Subdomainizer(Tool):
    def run(self, domain, name):

        start_time = datetime.now().time()

        time_start = time.time()

        write_output(f"Beginning Subdomainizer scanning for {domain} at {str(start_time)[:-7]}")

        make_dir(utils.file_utils.get_working_directory.get_wd() + '/link-sub')

        result_set = set()

        to_check_set = set()

        domains = get_seeds()

        inp = domains


        for i in inp:
            to_check_set.add(i)

        def search(domain):
            result_set.add(domain)
            subdomainizer_command = ["python3", f"{os.path.dirname(os.path.abspath(sys.argv[0]))}/utils/tool_utils/subdomainizer_utils/SubDomainizer.py", "-u", domain]

            result = subprocess.run(subdomainizer_command, stdout=subprocess.PIPE)

            output_lines = result.stdout.decode('utf-8').splitlines()

            start = False

            for i in output_lines:
                if 'Start of Results' in i:
                    start = True
                if 'End of Results' in i:
                    start = False
                if start and i.count('.') >= 1 and len([x for x in get_seeds() if f".{x}JO#GCH+_+" in i + 'JO#GCH+_+']) != 0:
                    to_check_set.add(i)
                print(i)

        finished = False
        while finished == False:
            copy = list(to_check_set)
            for i in copy:
                a = True
                if i in result_set:
                    continue
                search(i)
                a = False
            if a:
                finished = True

        out_file = utils.file_utils.get_working_directory.get_wd() + '/link-sub/' + domain + '.txt'

        with open(out_file, 'w') as file:
            for i in result_set:
                for ii in domains:
                    if ii in i:  
                        file.writelines(i + '\n')  
                        utils.file_utils.subs.add_sub(name, i) 

        end_time = time.time()

        elapsed_time = end_time - time_start

        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        utils.file_utils.get_time.add_time((name, hours * 3600 + minutes * 60 + seconds))

        write_output(f"Subdomainizer scan done for {domain} at {str(datetime.now().time())[:-7]} in {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")
        