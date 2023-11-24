from enumeration.tool_class import *
import utils.file_utils.get_working_directory
import utils.file_utils.tool_getters
from utils.file_utils.output_writer import *
from utils.file_utils.dir_creator import *
import utils.file_utils.get_time
import utils.asn_utils.asn_intel_enum
from datetime import datetime
import subprocess
import utils.file_utils.subs
from time import sleep
import time
import os

class Amass(Tool):
    def run(self, domain):

        start_time = datetime.now().time()

        time_start = time.time()

        write_output(f"Beginning Amass scanning for {domain} at {str(start_time)[:-7]}")

        make_dir(f"{utils.file_utils.get_working_directory.get_wd()}/amass")

        domain_output_dir = f"{utils.file_utils.get_working_directory.get_wd()}/amass/{domain}"
    
        make_dir(domain_output_dir)

        amass_command = [
            "amass",
            "enum",
            "-d", domain,
            "-oA", f"{domain_output_dir}/amass_output",
            "-timeout", str(utils.file_utils.tool_getters.get_amass_exec())
        ]

        result = subprocess.run(amass_command, stdout=subprocess.PIPE)

        output_lines = result.stdout.splitlines()

        print(output_lines)

        end_time = time.time()

        elapsed_time = end_time - time_start

        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        utils.file_utils.get_time.add_time(('amass', hours * 3600 + minutes * 60 + seconds))

        input_directory = f"{utils.file_utils.get_working_directory.get_wd()}/amass"

        subdomains = set()

        for dirname in os.listdir(input_directory):
            try:
                with open(f"{input_directory}/{dirname}/amass_output.txt", 'r') as file:

                    f_string = ''

                    for i in file.readlines():
                        f_string = f_string + ' ' + i

                    words = f_string.split()

                    for i in range(len(words)):
                        if words[i].count('.') >= 1:
                            subdomains.add(words[i])
                        elif i == '(ASN)' or i == b'(ASN)':
                            utils.asn_utils.asn_intel_enum.add_asn('amass', words[i - 1])
            except:
                pass
                continue

        output_file = f"{utils.file_utils.get_working_directory.get_wd()}/amass/subdomains.txt"

        with open(output_file, 'w') as out_file:
            for subdomain in subdomains:
                out_file.write(subdomain + '\n')
                utils.file_utils.subs.add_sub(('amass', subdomain))

        write_output(f"Amass scan done for {domain} at {str(datetime.now().time())[:-7]} in {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")

        sleep(10)
        