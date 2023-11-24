from utils.file_utils.tool_getters import *
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
import os


def custom_init(domain):

    list = []

    def function_creator(i):
        def run():

            start_time = datetime.now().time()
        
            time_start = time.time()

            write_output(f"Beginning {i} scanning for {domain} at {str(start_time)[:-7]}")

            command = get_custom_enum()[i][0].split(' ')
            for a in range(len(command)):
                if command[a] == '$domain$':
                    command[a] = domain
                elif '$file$' in command[a]:
                    splt = -1
                    try:
                        splt = command[a].index('/')
                    except:
                        pass
                        splt = -1
                    if splt != 1:
                        splt_s = command[a][splt:]
                        command[a] = utils.file_utils.get_working_directory.get_wd() + '/custom/' + domain + splt_s
                        try:
                            os.mkdir(utils.file_utils.get_working_directory.get_wd() + '/custom/' + domain)
                        except:
                            pass
                    else:
                        command[a] = utils.file_utils.get_working_directory.get_wd() + '/custom/' + domain
                        command[a] = command[a][:-1]
                        try:
                            os.mkdir(command[a])
                        except:
                            pass
            print(command)
            result = subprocess.run(command, stdout=subprocess.PIPE, check=True)

            lines = result.stdout.decode('utf-8').split('\n')
            for line in lines:
                s_lines = line.split(' ')
                for x in s_lines:
                    if x.count('.') >= 1:
                        utils.file_utils.subs.add_sub(i, x)

            for root, dirs, files in os.walk(utils.file_utils.get_working_directory.get_wd()):
                for file in files:
                    if file == i + '.txt':
                        with open(i + '.txt', 'r') as file:
                            lines = file.readlines()
                            for line in lines:
                                s_lines = line.split(' ')
                                for x in s_lines:
                                    if x.count('.') >= 1:
                                        utils.file_utils.subs.add_sub(i, x)

            end_time = time.time()

            elapsed_time = end_time - time_start

            hours, remainder = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)

            utils.file_utils.get_time.add_time((i, hours * 3600 + minutes * 60 + seconds))

            write_output(f"{i} scan dome for {domain} at {str(datetime.now().time())[:-7]} in {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")

        return run

    for i in get_custom_enum().keys():
        list.append(function_creator(i))

    return list
