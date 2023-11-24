from enumeration.tool_class import *
from utils.file_utils.output_writer import *
from utils.file_utils.dir_creator import *
import utils.file_utils.get_working_directory
import vuln_scanning.vulns
import utils.file_utils.get_time
import utils.file_utils.tool_getters
from datetime import datetime
import subprocess
import time

class Takeover(Tool):
    def run(self, domains):

        start_time = datetime.now().time()

        time_start = time.time()

        write_output(f"Beginning subdomain takeover scanning at {str(start_time)[:-7]}")

        command = ['subzy', 'run', '--targets', utils.file_utils.get_working_directory.get_wd() + '/temp/httpx_subdomains.txt', '--concurrency', str(utils.file_utils.tool_getters.get_take_threads())]
        
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE)

        for i in range(len(result.stdout.split(b'\n'))):
            string = result.stdout.split(b'\n')[i].decode('utf-8')
            print(string)
            if 'VULNERABLE' in string and 'NOT VULNERABLE' not in string:
                string = string.split(' ')
                vuln_scanning.vulns.add_vuln_info('subzy', str(string[8]), 'subdomain takeover ' + str(result.stdout.split(b'\n')[i + 1].decode('utf-8').split(' ')[8]), 'high')

        end_time = time.time()

        elapsed_time = end_time - time_start

        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        utils.file_utils.get_time.add_time(('subzy', hours * 3600 + minutes * 60 + seconds))

        write_output(f"Subdomain takeover scanning done at {str(datetime.now().time())[:-7]} in {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")