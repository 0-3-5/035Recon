import threading
from utils.file_utils.tool_getters import *
from utils.file_utils.output_writer import *
from vuln_scanning.tools.takeover import *
from vuln_scanning.tools.social import *
from vuln_scanning.custom_vuln import *
from vuln_scanning.tools.nuclei import *
import utils.tool_utils.brutespray_utils.brutespray
from vuln_scanning.tools.brutespray import *
import sys

def vuln_scan_init(domains):
    def nuclei():
        if get_nuclei():
            for i in range(get_nuclei_exec()):
                run_nuclei(domains)

    def takeover():
        if get_takeover():
            for i in range(get_takeover_exec()):
                takeover = Takeover(' ')
                takeover.run(domains)
    
    def social():
        if get_social():
            for i in range(get_social_exec()):
                social = Social(' ')
                social.run(domains)

    def spray():
        if get_spray():
            for i in range(get_spray_exec()):
                utils.tool_utils.brutespray_utils.brutespray.run_brutespray(domains)

    threads = []

    func_list = [nuclei, takeover, social, spray]

    use_list = custom_init(domains) + func_list

    for func in use_list:
        thread = threading.Thread(target=func)
        threads.append(thread)

    for thread in threads:
        thread.start()
        if '-mv' not in sys.argv:
            thread.join()

    for thread in threads:
        thread.join()