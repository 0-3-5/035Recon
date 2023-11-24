import utils.file_utils.get_working_directory

def write():
    with open(utils.file_utils.get_working_directory.get_wd() + '/subdomains.txt', 'r') as in_file, open(utils.file_utils.get_working_directory.get_wd() + '/temp/httpx_subdomains.txt', 'w') as out_file:
        lines = in_file.readlines()

        for line in lines:
            if (' ' not in line) and ('\\' not in line):
                out_file.writelines('https://' + line)
                out_file.writelines('http://' + line)