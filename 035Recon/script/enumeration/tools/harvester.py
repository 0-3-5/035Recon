import subprocess
from enumeration.tool_class import *
import utils.file_utils.get_working_directory
from utils.file_utils.output_writer import *
from datetime import datetime
import utils.file_utils.subs
import utils.asn_utils.asn_intel_enum
import utils.file_utils.get_time
from utils.file_utils.dir_creator import *
import time
import json

class TheHarvester(Tool):
    def run(self, domain):

        start_time = datetime.now().time()

        time_start = time.time()

        write_output(f"Beginning TheHrvester scanning for {domain} at {str(start_time)[:-7]}")

        make_dir(f"{utils.file_utils.get_working_directory.get_wd()}/harvester")

        command = f"theHarvester -d {domain} -b all -f {utils.file_utils.get_working_directory.get_wd()}/harvester/harvester_{domain}"

        subprocess.run(command, shell=True)

        folder_path = f"{utils.file_utils.get_working_directory.get_wd()}/harvester/"

        json_files = [f for f in os.listdir(folder_path) if f.endswith(".json")]

        for json_file in json_files:

            with open(f"{utils.file_utils.get_working_directory.get_wd()}/harvester/" + json_file, "r") as json_file, open(f"{utils.file_utils.get_working_directory.get_wd()}/harvester/harvested_subs.txt", 'a') as out_file:
                data = json.load(json_file)

                if "hosts" in data:
                    hosts = data["hosts"]
                    for host in hosts:
                        out_file.writelines(host + '\n')
                        utils.file_utils.subs.add_sub('harvester', host)

                if "ips" in data:
                    ips = data["ips"]
                    for ip in ips:
                        out_file.writelines(ip + '\n')
                        utils.file_utils.subs.add_sub('harvester', ip)

                if "asns" in data:
                    asns = data["asns"]
                    for asn in asns:
                        utils.asn_utils.asn_intel_enum.add_asn('harvester', asn)

        end_time = time.time()

        elapsed_time = end_time - time_start

        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        utils.file_utils.get_time.add_time(('harvester', hours * 3600 + minutes * 60 + seconds))

        write_output(f"TheHarvester scan done for {domain} at {str(datetime.now().time())[:-7]} in {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")
        