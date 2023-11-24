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

class Assetfinder(Tool):
    def run(self, domain):

        start_time = datetime.now().time()
        
        time_start = time.time()

        write_output(f"Beginning Assetfinder scanning for {domain} at {str(start_time)[:-7]}")
        
        make_dir(utils.file_utils.get_working_directory.get_wd() + '/assetfinder')

        command = ["assetfinder", domain, '-subs-only']

        result = subprocess.run(command, check=True, stdout=subprocess.PIPE)

        with open(utils.file_utils.get_working_directory.get_wd() + '/assetfinder/assetfinder_' + domain, 'a') as file:
            file.writelines(result.stdout.decode('utf-8'))
            [utils.file_utils.subs.add_sub('assetfinder', x) for x in result.stdout.decode('utf-8').split('\n')]

        end_time = time.time()

        elapsed_time = end_time - time_start

        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        utils.file_utils.get_time.add_time(('assetfinder', hours * 3600 + minutes * 60 + seconds))

        write_output(f"Assetfinder scan done for {domain} at {str(datetime.now().time())[:-7]} in {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")
        