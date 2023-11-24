import subprocess
from enumeration.tool_class import *
import utils.file_utils.get_working_directory
from utils.file_utils.output_writer import *
from utils.file_utils.dir_creator import *
import utils.file_utils.tool_getters
import utils.file_utils.get_time
from utils.file_utils.get_seeds import *
from datetime import datetime
import utils.file_utils.subs
import time


class Gospider(Tool):
    def run(self, domain, name):

        word_list = []

        start_time = datetime.now().time()

        time_start = time.time()

        write_output(f"Beginning Gospider scanning for {domain} at {str(start_time)[:-7]}")

        make_dir(utils.file_utils.get_working_directory.get_wd() + '/link-go')

        command = ['gospider', '-s', f"https://{domain}", '-v', '-d', '1']

        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE)

            for i in result.stdout.split():
                string = i.decode('utf-8')
                word_list.append(string)
                print(string)

            print(f"Gospider completed for {domain}.")
        except subprocess.CalledProcessError as e:
            print(f"Error running Gospider for {domain}: {e}")

        output = []

        for i in range(len(word_list)):
            if "https://" in word_list[i] or "http://" in word_list[i]:
                output.append(word_list[i].replace(']', ''))
            elif 'subdomain' in word_list[i]:
                output.append(word_list[i + 2])

        output = set(output)
        output = list(output)

        out_file = utils.file_utils.get_working_directory.get_wd() + '/link-go/' + domain + '.txt'

        out2 = set()

        for i in output:
            if 'http' in i:
                out2.add(i.split('/')[2])
            else:
                out2.add(i)

        with open(out_file, 'w') as file:
            for i in out2:
                for ii in [domain]:
                    if ii in i:
                        file.writelines(i + '\n')
                        utils.file_utils.subs.add_sub(name, i)

        end_time = time.time()

        elapsed_time = end_time - time_start

        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        utils.file_utils.get_time.add_time((name, hours * 3600 + minutes * 60 + seconds))

        write_output(f"Gospider scan done for {domain} at {str(datetime.now().time())[:-7]} in {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")
        