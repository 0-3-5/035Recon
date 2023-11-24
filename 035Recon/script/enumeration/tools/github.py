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

class Github(Tool):
    def run(self, domain):

        start_time = datetime.now().time()

        time_start = time.time()

        write_output(f"Beginning Github-Subdomains scanning for {domain} at {str(start_time)[:-7]}")

        make_dir(utils.file_utils.get_working_directory.get_wd() + '/github')

        results = set()

        with open(f"{utils.file_utils.get_working_directory.get_wd()}/github/subdomains.txt", 'w') as file:
            for i in range(1):
                command = ["python3", f"{os.path.dirname(os.path.abspath(sys.argv[0]))}/utils/tool_utils/github-utils/github-subdomains.py", "-t", utils.file_utils.tool_getters.get_git_token() , "-d", domain, "-e"]
                process = subprocess.run(command, stdout=subprocess.PIPE, text=True)

                for result in process.stdout.splitlines():
                    if len([x for x in get_seeds() if f".{x}JO#GCH+_+" in result + 'JO#GCH+_+']) != 0:
                        if result not in results:
                            file.writelines(result + '\n')
                            utils.file_utils.subs.add_sub('github', result)
                    results.add(result)
                    print(result)

                time.sleep(30)
                print(domain, str(i + 1))

        end_time = time.time()

        elapsed_time = end_time - time_start

        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        utils.file_utils.get_time.add_time(('github', hours * 3600 + minutes * 60 + seconds))

        write_output(f"Github-Subdomains scan done for {domain} at {str(datetime.now().time())[:-7]} in {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")
        