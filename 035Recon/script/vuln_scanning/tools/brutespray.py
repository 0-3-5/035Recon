from enumeration.tool_class import *
from utils.file_utils.output_writer import *
from utils.file_utils.dir_creator import *
import utils.file_utils.get_working_directory
import utils.file_utils.get_time
import vuln_scanning.vulns
import subprocess
import os

class Brutespray(Tool):
    def run(self, domain):


        start_time = datetime.now().time()
        time_start = time.time()

        try:
            os.mkdir(utils.file_utils.get_working_directory.get_wd() + '/brutespray')
        except:
            pass

        out_folder = utils.file_utils.get_working_directory.get_wd() + '/brutespray'

        target = domain

        print(target)

        path = f"{target}_nmap.xml"
        if out_folder != None:
            path = f"{out_folder}/{target}_nmap.xml"

        command = ["nmap", "-sV", "-oX", path, target]

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        output_lines = result.stdout.splitlines()

        print(output_lines)

        brute_out = f"{target}_brute"
        if out_folder != None:
            brute_out = f"{out_folder}/{target}_brute.txt"


        command = ["brutespray", "-f", f"{path}", "--threads", '100']

        try:
            with open(brute_out, "w") as output_file:

                result = subprocess.run(command, check=True, stdout=subprocess.PIPE, text=True)

                output_lines = result.stdout.splitlines()

                print(output_lines)

                for i in output_lines:
                    output_file.write(i + '\n')
                    if '[SUCCESS]' in i:
                        vuln_scanning.vulns.add_vuln_info('brutespray', i, f"weak login credentials {i}", 'high')

        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

        end_time = time.time()

        elapsed_time = end_time - time_start

        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        utils.file_utils.get_time.add_time(('brutespray', hours * 3600 + minutes * 60 + seconds))
