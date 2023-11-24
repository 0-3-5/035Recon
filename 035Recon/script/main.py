import main_menu.main_menu
import main_menu.errors
import enumeration.main_enum
import vuln_scanning.main_vuln_scan
import utils.file_utils.get_seeds
import utils.file_utils.get_working_directory
import utils.validity_utils.get_validity
import utils.enum_utils.linked_repeater
import utils.file_utils.tool_getters
import utils.file_utils.output_writer
import utils.file_utils.httpx_writer
import main_menu.custom_menu
import utils.tool_utils.resolver_utils.resolver
import vuln_scanning.vulns
import utils.asn_utils.asn_intel_enum
from enumeration.tools.alteration import *
import utils.asn_utils.get_asns
from colorama import Fore, init
from datetime import datetime
import utils.file_utils.subs
import utils.time_utils.time_utils
import threading
import sys
import os

start_time = datetime.now().time()

time_start = time.time()

subs = set()

def get_subs():
    return subs

def add_sub(domain):
    subs.add(domain)

if (len(sys.argv) == 1) or ('-h' in sys.argv):
    main_menu.main_menu.main_menu()
elif '-custom-help' in sys.argv:
    main_menu.custom_menu.custom_menu()
else:
    valid = utils.validity_utils.get_validity.get_validity(sys.argv)

    if valid == None:
        
        utils.time_utils.time_utils.init_time()

        init(autoreset=True)

        seeds = utils.file_utils.get_seeds.get_seeds()

        try:
            os.mkdir(utils.file_utils.get_working_directory.get_wd())
            os.mkdir(utils.file_utils.get_working_directory.get_wd() + '/temp')
            with open(f"{utils.file_utils.get_working_directory.get_wd()}/report.txt", "w") as file:
                file.writelines(f"Starting scan at {str(datetime.now().time())[:-7]}\n")
        except:
            main_menu.errors.working_directory_exists()
            pass

        total_seeds = len(seeds)

        if '-t' in sys.argv:
            num_threads = None
            for i in range(len(sys.argv)):
                if sys.argv[i] == '-t':
                    num_threads = int(sys.argv[i + 1])
        else:
            num_threads = 1

        seeds_to_execute = [enumeration.main_enum.enum_init] * total_seeds

        def run_function():
            while seeds_to_execute:
                function = seeds_to_execute.pop()
                seed = seeds.pop()
                if function:
                    function(total_seeds - len(seeds_to_execute), seed)

        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=run_function)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        write_output('All seeds have been enumerated.')

        sub_list = [x[1] for x in utils.file_utils.subs.get_subs()]

        checked_subs = []

        while sorted(sub_list) != sorted(checked_subs):

            list_check = []

            for i in sub_list:
                if i not in checked_subs:
                    list_check.append(i)

            checked_subs = sub_list

            if utils.file_utils.tool_getters.get_link_go_all():
                print(Fore.RED + "Beginning gospider subdomain enumeration.")
                utils.enum_utils.linked_repeater.run_go(list_check)

            if utils.file_utils.tool_getters.get_link_sub_all():
                print(Fore.RED + "Beginning subdomainizer subdomain enumeration.")
                utils.enum_utils.linked_repeater.run_sub(list_check)

            sub_list = [x[1] for x in utils.file_utils.subs.get_subs()]

        if utils.file_utils.tool_getters.get_alt():
            alt_list = []
            for alt in sub_list:
                for num in '1234567890':
                    if num in alt:
                        alt_list.append(alt)
            a = Alteration(' ')
            a.run(alt_list)

        utils.file_utils.output_writer.write_subs(utils.file_utils.subs.get_subs())

        if utils.file_utils.tool_getters.get_rec():
            utils.asn_utils.asn_intel_enum.run_asns(utils.asn_utils.get_asns.run_amass_intel(set([x[1] for x in utils.asn_utils.asn_intel_enum.get_asns()])))

        #time.sleep(1000)

        utils.tool_utils.resolver_utils.resolver.resolve()

        utils.file_utils.httpx_writer.write()
        #utils.tool_utils.resolver_utils.resolver.compare_screenshots(utils.tool_utils.resolver_utils.resolver.get_screenshots())
        utils.tool_utils.resolver_utils.resolver.compare_subdomains()
        
        if get_similar():
            vuln_scanning.main_vuln_scan.vuln_scan_init([x for x in utils.tool_utils.resolver_utils.resolver.get_similar_screenshots().keys()])
        else:
            vuln_scanning.main_vuln_scan.vuln_scan_init([x[1] for x in utils.file_utils.subs.get_subs()])

        utils.file_utils.output_writer.write_output_end(utils.file_utils.subs.get_subs(), vuln_scanning.vulns.get_vulns())
        utils.file_utils.output_writer.write_html(utils.file_utils.subs.get_subs(), vuln_scanning.vulns.get_vulns())

        end_time = time.time()

        elapsed_time = end_time - time_start

        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(60 * '-')

        write_output(f"ALL SCANNING DONE AT {str(datetime.now().time())[:-7]} IN {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")
        write_output(60 * '-' + '\n')
        