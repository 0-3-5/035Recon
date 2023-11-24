import subprocess
from enumeration.tool_class import *
import utils.file_utils.tool_getters
from utils.file_utils.output_writer import *
from utils.file_utils.dir_creator import *
import utils.file_utils.get_seeds
import utils.file_utils.get_time
import utils.file_utils.subs

def run_amass_intel(asns):
    c_asns = asns

    for asn in range(len(asns)):
        if asn in utils.file_utils.tool_getters.get_asns():
            c_asns = asns[:asn] + asns[asn + 1:]
            
    out_lines = []

    for i in c_asns:
        command = ["amass", "intel", "-asn", i]
        try:
            print(command)
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, timeout=600)
            print(command)

            lines = result.stdout.decode('utf-8').splitlines()
    
            c_lines = lines
        
            for line in lines:
                if line in utils.file_utils.get_seeds.get_seeds():
                    c_lines = lines[:line] + lines[line + 1:]
                    
            out_lines += c_lines
        except:
            pass

    return out_lines