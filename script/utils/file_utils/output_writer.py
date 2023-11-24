from datetime import datetime
import os
import shutil
import time

import utils.asn_utils.asn_intel_enum
import utils.file_utils.get_time
import utils.file_utils.get_working_directory
import utils.file_utils.subs
from utils.file_utils.tool_getters import *
import utils.time_utils.time_utils
import utils.tool_utils.resolver_utils.resolver
import vuln_scanning.vulns
import utils.asn_utils.asn_intel_enum


output = []

def get_output():
    global output
    return output

def write_output(str):
    print(str)
    with open(f"{utils.file_utils.get_working_directory.get_wd()}/report.txt", 'a') as file:
        file.writelines(str + '\n')
    output.append(str)

def write_subs(domains):
    try:
        os.mkdir(f"{utils.file_utils.get_working_directory.get_wd()}/temp")
    except:
        pass
    with open(f"{utils.file_utils.get_working_directory.get_wd()}/temp/subdomains_temp.txt", 'a') as file:
        for domain in domains:
            file.writelines(domain[1] + '\n')

def write_output_end(subs, vulns):

    start_time = datetime.now().time()

    time_start = time.time()

    write_output(f"Beginning result writing at {str(start_time)[:-7]}")

    with open(f"{utils.file_utils.get_working_directory.get_wd()}/report.txt", 'a') as file:

        total_subdomains = 0

        total_vulns = 0

        file.writelines(60 * '-' + '\n')
        file.writelines('END OF ENUMERATION AND VULNERABILITY SCANNING, RESULTS: \n')

        written_tools = {}

        for sub in subs:
            if sub[0] not in written_tools:
                written_tools[sub[0]] = [x[1] for x in subs if x[0] == sub[0]]

        for tool in written_tools.keys():
            file.writelines(60 * '-' + '\n')
            file.writelines(tool + '\n')
            file.writelines('Total subdomains: ' + str(len(written_tools[tool])) + '\n')

            u_count = 0

            for x in written_tools[tool]:
                
                unique = True

                for y in utils.file_utils.subs.get_subs():
                    if y[1] == x and y[0] != tool:
                        unique = False
                        break
                if unique:
                    u_count += 1

            file.writelines('Unique subdomains: ' + str(u_count) + '\n')
            total_subdomains += u_count

            hours, remainder = divmod(utils.file_utils.get_time.get_time(tool), 3600)
            minutes, seconds = divmod(remainder, 60)

            file.writelines('Total execution time: ' + f"{'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}" + '\n')


        written_tools = {}
        written_tool_info = {}
        written_tool_severity = {}

        for sub in vulns:
            if sub[0] not in written_tools:
                written_tools[sub[0]] = [x[1] for x in vulns if x[0] == sub[0]]
                written_tool_info[sub[0]] = [x[2] for x in vulns if x[0] == sub[0]]
                written_tool_severity[sub[0]] = [x[3] for x in vulns if x[0] == sub[0]]

        for tool in written_tools.keys():
            file.writelines(60 * '-' + '\n')
            file.writelines(tool + '\n')
            file.writelines('Total vulnerabilities discovered: ' + str(len(written_tools[tool])) + '\n')
            total_vulns += len(written_tools[tool])

            for i in range(len(written_tools[tool])):
                file.writelines(tool + ' ' + 'target: ' + written_tools[tool][i] + ' info: ' + written_tool_info[tool][i] + ' severity: ' + written_tool_severity[tool][i] + '\n')

            hours, remainder = divmod(utils.file_utils.get_time.get_time(tool), 3600)
            minutes, seconds = divmod(remainder, 60)

            file.writelines('Total execution time: ' + f"{'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}" + '\n')

        file.writelines(60 * '-' + '\n')

        file.writelines('TOTAL SUBDOMAINS DISCOVERED: ' + str(total_subdomains) + '\n')
        file.writelines('TOTAL VULNERABILITIES DISCOVERED: ' + str(total_vulns) + '\n')

        end_time = time.time()

        elapsed_time = end_time - time_start

        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        write_output(f"Writing output done at {str(datetime.now().time())[:-7]} in {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")
        
        
def write_html(subs, vulns):
    
    jj = '/'
    kk = '_'
    
    os.mkdir(f"{utils.file_utils.get_working_directory.get_wd()}/html_report")
    os.mkdir(f"{utils.file_utils.get_working_directory.get_wd()}/html_report/utils")
    os.mkdir(f"{utils.file_utils.get_working_directory.get_wd()}/html_report/utils/tools")
    os.mkdir(f"{utils.file_utils.get_working_directory.get_wd()}/html_report/utils/subdomains")
    shutil.copy(f"{os.path.dirname(os.path.abspath(sys.argv[0]))}/utils/html_utils/stylesheet.css", f"{utils.file_utils.get_working_directory.get_wd()}/html_report/utils/stylesheet.css")
    
    with open(f"{utils.file_utils.get_working_directory.get_wd()}/html_report/html_report.html", 'w') as file:
        file.writelines(f'<!DOCTYPE html><html><head><title>035Recon Main Vulnerability Report</title><link rel="stylesheet" type="text/css" href="utils/stylesheet.css"></head><body><ul id="resultsList"></ul><br><br><h1>Main Vulnerability Report</h1><div class="search-bar"><input type="text" class="search-input" placeholder="Search..." id="searchInput"></div><div class="gray-rectangle"><a href="utils/all_subdomains.html"><button class="right-button">All Subdomains</button></a><a href="utils/simplified_subdomains.html"><button class="rb2">Simplified Subdomains</button></a><a href="html_report.html"><button class="rb3">Main Menu</button></a></div><ul id="resultsList"></ul><hr class="test"><h2>Target Information</h2><p>Selected seeds: ')
        for i in utils.file_utils.get_seeds.get_seeds():
            file.writelines(i + ', ')
        file.writelines('</p><p>Command: ')
        for i in sys.argv:
            file.writelines(i + ' ')
            
        #time_start = utils.time_utils.time_utils.get_time()
            
        #end_time = time.time()

        #elapsed_time = end_time - time_start
        
        #hours, remainder = divmod(elapsed_time, 3600)
        #minutes, seconds = divmod(remainder, 60)
        
        time_tools = set()
        
        for line in get_output():
            if line == 'All seeds have been enumerated.':
                break
            lines = line.split(' ')
            if lines[0] != 'Beginning':
                if '.txt' not in lines[0]:
                    time_tools.add(lines[0].lower())
                else:
                    time_tools.add(lines[0])
                        
                        
        total_time = 0
        
        for time_tool in time_tools:
            total_time += utils.file_utils.get_time.get_time(time_tool) 

        elapsed_time = total_time
        
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        

        file.writelines(f"<hr><h2>Main Recon Report</h2><p>Total subdomains discovered: {str(len(utils.file_utils.subs.get_subs()))}</p><p>Total photounique subdomains discovered: {str(len(utils.tool_utils.resolver_utils.resolver.get_similar_screenshots()))}</p><p>Total AS numberes discovered: {str(len(utils.asn_utils.asn_intel_enum.get_asns()))}</p><p>Total execution Time: {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}</p><hr><br>")
        
        written_tools = {}

        for sub in subs:
            if sub[0] not in written_tools:
                written_tools[sub[0]] = [x[1] for x in subs if x[0] == sub[0]]

        for tool in written_tools.keys():
            
            u_count = 0

            for x in written_tools[tool]:
                
                unique = True

                for y in utils.file_utils.subs.get_subs():
                    if y[1] == x and y[0] != tool:
                        unique = False
                        break
                if unique:
                    u_count += 1
                    
            p_count = 0

            for x in utils.tool_utils.resolver_utils.resolver.get_similar_screenshots().keys():
                if 'http_' in x:
                    y = x[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_'):-4]
                else:
                    y = x[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_'):-4]
                if y in written_tools[tool]:
                    p_count += 1
                    
            
            pu_count = 0

            for x in utils.tool_utils.resolver_utils.resolver.get_similar_screenshots().keys():
                if 'http_' in x:
                    y = x[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_'):-4]
                else:
                    y = x[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_'):-4]
                    
                unique = True
                
                for k in utils.file_utils.subs.get_subs():
                    if k[1] == y and k[0] != tool:
                        unique = False
                    
                if y in written_tools[tool] and unique:
                    pu_count += 1
                    
            hours, remainder = divmod(utils.file_utils.get_time.get_time(tool), 3600)
            minutes, seconds = divmod(remainder, 60)
            
            y_count = 0
            vulned = []
             
            for i in sorted(written_tools[tool], key=len, reverse=True):
                vulnerable = False
                for ii in [x[1] for x in vuln_scanning.vulns.get_vulns()]:
                    ok = True 
                    for b in vulned:
                        if i in b:
                            ok = False 
                            break
                    if i in ii and ok:
                        vulnerable = True
                        vulned.append(i)
                        break
                    
                if vulnerable:
                    y_count += 1
                    
            yu_count = 0
            
            vulned = []
            
            for i in sorted(written_tools[tool], key=len, reverse=True):
                vulnerable = False
                for ii in [x[1] for x in vuln_scanning.vulns.get_vulns()]:
                    ok = True 
                    for b in vulned:
                        if i in b:
                            ok = False 
                            break
                    if i in ii and ok:
                        vulnerable = True
                        vulned.append(i)
                        break
                    
                if vulnerable:
                    unique = True
                
                    for k in utils.file_utils.subs.get_subs():
                        if k[1] == x and k[0] != tool:
                            unique = False
                    
                    if unique:
                        yu_count += 1
            
            file.writelines(f'<br><h3>{tool.capitalize()} Stats:</h3><p>Subdomains discovered: {str(len(written_tools[tool]))}</p><p>Unique Subdomains discovered: {str(u_count)}</p><p>Photounique subdomains discovered: {str(p_count)}</p><p>Unique photounique subdomains discovered: {str(pu_count)}</p><p>Subdomains with vulnerabilities discovered: {str(y_count)}</p><p>Unique subdomains with vulnerabilities discovered: {str(yu_count)}</p><p>Execution Time: {"0" if len(str(int(hours))) == 1 else ""}{str(int(hours))}:{"0" if len(str(int(minutes))) == 1 else ""}{str(int(minutes))}:{"0" if len(str(int(seconds))) == 1 else ""}{str(int(seconds))}</p><a href="utils/tools/{tool.replace(jj, kk)}.html"><button class="pretty-button">More Info</button></a><br><br>')
            
        file.writelines('<hr>')
            
        vuln_time_tools = set()
        
        for i in utils.file_utils.get_time.get_times().keys():
            if i not in time_tools:
                vuln_time_tools.add(i)
            
        total_time = 0
        
        for time_tool in vuln_time_tools:
            total_time += utils.file_utils.get_time.get_time(time_tool)

        elapsed_time = total_time - utils.tool_utils.resolver_utils.resolver.get_write_time()
        
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        
        file.writelines(f'<h2>Main Vulnerability Report</h2><p>Total vulnerabilities discovered: {str(len(vuln_scanning.vulns.get_vulns()))}</p><p>Total execution Time: {"0" if len(str(int(hours))) == 1 else ""}{str(int(hours))}:{"0" if len(str(int(minutes))) == 1 else ""}{str(int(minutes))}:{"0" if len(str(int(seconds))) == 1 else ""}{str(int(seconds))}</p><hr>')
        
        written_tools = {}
        written_tool_info = {}
        written_tool_severity = {}

        for sub in vulns:
            if sub[0] not in written_tools:
                written_tools[sub[0]] = [x[1] for x in vulns if x[0] == sub[0]]
                written_tool_info[sub[0]] = [x[2] for x in vulns if x[0] == sub[0]]
                written_tool_severity[sub[0]] = [x[3] for x in vulns if x[0] == sub[0]]

        for tool in written_tools.keys():
            
            hours, remainder = divmod(utils.file_utils.get_time.get_time(tool), 3600)
            minutes, seconds = divmod(remainder, 60)
            
            file.writelines(f'<br><h3>{tool.capitalize()}:</h3><p>Vulnerabilities discovered: {str(len(written_tools[tool]))}</p><p>Execution Time: {"0" if len(str(int(hours))) == 1 else ""}{str(int(hours))}:{"0" if len(str(int(minutes))) == 1 else ""}{str(int(minutes))}:{"0" if len(str(int(seconds))) == 1 else ""}{str(int(seconds))}</p><a href="utils/tools/{tool.replace(jj, kk)}.html"><button class="pretty-button">More Info</button></a><br><br>')
        
        
        file.writelines('<hr><h2>LOG</h2><hr>')
        
        for line in output:
            file.writelines(f'<p>{line}</p>')
            
            
        end_time = time.time()

        elapsed_time = end_time - utils.time_utils.time_utils.get_time()

        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

            
        file.writelines(f'<hr><br><h3>TOTAL SUBDOMAINS DISCOVERED: {len(utils.file_utils.subs.get_subs())}</h3><h3>TOTAL VULNERABILITIES DISCOVERED: {len(vuln_scanning.vulns.get_vulns())}</h3><h3>TOTAL EXECUTION TIME: {"0" if len(str(int(hours))) == 1 else ""}{str(int(hours))}:{"0" if len(str(int(minutes))) == 1 else ""}{str(int(minutes))}:{"0" if len(str(int(seconds))) == 1 else ""}{str(int(seconds))}</h3><br><hr>')
        file.writelines('<script>searchList = [')
        
        time_tools = [x[0] for x in subs] + [x[0] for x in vulns]
        time_tools = set(time_tools)
        time_tools = list(time_tools)
        
        for x in range(len(time_tools)):
            if x != len(time_tools) - 1:
                file.writelines(f'"{time_tools[x].replace(jj, kk)}",')
            else:
                file.writelines(f'"{time_tools[x].replace(jj, kk)}"];')
                
        file.writelines("const searchInput = document.getElementById('searchInput');")
        file.writelines("const myList = document.getElementById('resultsList');")
        file.writelines("searchInput.addEventListener('input', function() {const searchQuery = searchInput.value.toLowerCase();while (myList.firstChild) {myList.removeChild(myList.firstChild);}")
        file.writelines("if (searchQuery.length >= 4) {searchList.forEach(function(domain) {if (domain.includes(searchQuery)) {const newItem = document.createElement('h3');")
        file.writelines("newItem.textContent = domain; myList.appendChild(newItem);myList.classList.add('resultList');newItem.addEventListener('click', function() {")
        file.writelines("const destinationURL = `utils/tools/${domain}.html`; window.open(destinationURL, '_blank');});}});}});</script></body></html>")
        
    for tool in list(set([x[0] for x in subs])):
        with open(f'{utils.file_utils.get_working_directory.get_wd()}/html_report/utils/tools/{tool.replace(jj, kk)}.html', 'w') as file:
            file.writelines(f'<!DOCTYPE html><html><head><title>{tool.capitalize()} Report</title>')
            file.writelines(f'<link rel="stylesheet" type="text/css" href="../stylesheet.css">')
            file.writelines(f'</head><body><ul id="resultsList"></ul><br><br>')
            file.writelines(f'<h1>{tool.capitalize()} Report</h1><div class="search-bar">')
            file.writelines(f'<input type="text" class="search-input" placeholder="Search..." id="searchInput"></div>')
            file.writelines(f'<div class="gray-rectangle"><a href="..//all_subdomains.html">')
            file.writelines(f'<button class="right-button">All Subdomains</button></a>')
            file.writelines(f'<a href="../simplified_subdomains.html"><button class="rb2">Simplified Subdomains</button>')
            file.writelines(f'</a><a href="../../html_report.html"><button class="rb3">Main Menu</button></a></div><hr class="test">')
            
            
            domains = set()
            
            for i in utils.file_utils.subs.get_subs():
                if i[0] == tool:
                    domains.add(i[1])
            
            file.writelines(f'<h3>Total Subdomains Discovered: {len(domains)}</h3>')
            
            u_count = 0
            
            written_tools = {}
            
            for sub in subs:
                if sub[0] not in written_tools:
                    written_tools[sub[0]] = [x[1] for x in subs if x[0] == sub[0]]

            for x in written_tools[tool]:
                
                unique = True

                for y in utils.file_utils.subs.get_subs():
                    if y[1] == x and y[0] != tool:
                        unique = False
                        break
                if unique:
                    u_count += 1
                    
            file.writelines(f'<h3>Unique subdomains discovered: {u_count}</h3>')
            
            p_count = 0

            for x in utils.tool_utils.resolver_utils.resolver.get_similar_screenshots().keys():
                if 'http_' in x:
                    y = x[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_'):-4]
                else:
                    y = x[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_'):-4]
                if y in written_tools[tool]:
                    p_count += 1
                    
            file.writelines(f'<h3>Photounique subdomains discovered: {p_count}</h3>')      
            
            pu_count = 0

            for x in utils.tool_utils.resolver_utils.resolver.get_similar_screenshots().keys():
                if 'http_' in x:
                    y = x[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_'):-4]
                else:
                    y = x[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_'):-4]
                    
                unique = True
                
                for k in utils.file_utils.subs.get_subs():
                    if k[1] == y and k[0] != tool:
                        unique = False
                    
                if y in written_tools[tool] and unique:
                    pu_count += 1
                    
            file.writelines(f'<h3>Unique Photounique subdomains discovered: {pu_count}</h3>')
            
            y_count = 0
            
            vulned = []
             
            for i in sorted(written_tools[tool], key=len, reverse=True):
                vulnerable = False
                for ii in [x[1] for x in vuln_scanning.vulns.get_vulns()]:
                    ok = True 
                    for b in vulned:
                        if i in b:
                            ok = False 
                            break
                    if i in ii and ok:
                        vulnerable = True
                        vulned.append(i)
                        break
                    
                if vulnerable:
                    y_count += 1
                        
                    
            file.writelines(f'<h3>Vulnerable subdomains discovered: {y_count}</h3>')
                    
            yu_count = 0
            
            vulned = []
            
            for i in sorted(written_tools[tool], key=len, reverse=True):
                vulnerable = False
                for ii in [x[1] for x in vuln_scanning.vulns.get_vulns()]:
                    ok = True 
                    for b in vulned:
                        if i in b:
                            ok = False 
                            break
                    if i in ii and ok:
                        vulnerable = True
                        vulned.append(i)
                        break
                    
                if vulnerable:
                    unique = True
                
                    for k in utils.file_utils.subs.get_subs():
                        if k[1] == x and k[0] != tool:
                            unique = False
                    
                    if unique:
                        yu_count += 1
            
            file.writelines(f'<h3>Unique vulnerable subdomains discovered: {yu_count}</h3>')
            
            hours, remainder = divmod(utils.file_utils.get_time.get_time(tool), 3600)
            minutes, seconds = divmod(remainder, 60)
            
            file.writelines(f'<h3>Total execution Time: {"0" if len(str(int(hours))) == 1 else ""}{str(int(hours))}:{"0" if len(str(int(minutes))) == 1 else ""}{str(int(minutes))}:{"0" if len(str(int(seconds))) == 1 else ""}{str(int(seconds))}</h3>')
            
            asns = set()
                    
            for i in utils.asn_utils.asn_intel_enum.get_asn_tool(tool):
                asns.add(i)
            
            file.writelines(f'<h3>Total AS numbers discovered: {len(asns)}</h3>')
            file.writelines(f'<hr><h2>SUBDOMAINS DISCOVERED:</h2><hr><br>')
            
            non_vuln = []
            vulned = []
            
            search_list = []
            
            for i in sorted(written_tools[tool], key=len, reverse=True):
                search_list.append(i)
                vulnerable = False
                for ii in [x[1] for x in vuln_scanning.vulns.get_vulns()]:
                    ok = True 
                    for b in vulned:
                        if i in b:
                            ok = False 
                            break
                    if i in ii and ok:
                        vulnerable = True
                        vulned.append(i)
                        break
                        
                        
                if vulnerable:
                    file.writelines(f'<a href="../subdomains/{i}.html" class="normal-link" target="_blank">{i} [VULNERABLE]</p>')
                else:
                    non_vuln.append(i)
                        
            for i in non_vuln:
                file.writelines(f'<a href="../subdomains/{i}.html" class="normal-link" target="_blank">{i}</p>')
                
            file.writelines('<script>searchList = [')
            
            for x in range(len(search_list)):
                if x != len(search_list) - 1:
                    file.writelines(f'"{search_list[x]}",')
                else:
                    file.writelines(f'"{search_list[x]}"];')
                    
            file.writelines("const searchInput = document.getElementById('searchInput');")
            file.writelines("const myList = document.getElementById('resultsList');")
            file.writelines("searchInput.addEventListener('input', function() {const searchQuery = searchInput.value.toLowerCase();while (myList.firstChild) {myList.removeChild(myList.firstChild);}")
            file.writelines("if (searchQuery.length >= 4) {searchList.forEach(function(domain) {if (domain.includes(searchQuery)) {const newItem = document.createElement('h3');")
            file.writelines("newItem.textContent = domain; myList.appendChild(newItem);myList.classList.add('resultList');newItem.addEventListener('click', function() {")
            file.writelines("const destinationURL = `../subdomains/${domain}.html`; window.open(destinationURL, '_blank');});}});}});</script></body></html>")
                
    vulnerabilities = set([x[0] for x in vulns])
    for tool in vulnerabilities:
        with open(f'{utils.file_utils.get_working_directory.get_wd()}/html_report/utils/tools/{tool.replace(jj, kk)}.html', 'w') as file:
            file.writelines(f'<!DOCTYPE html><html><head><title>{tool.capitalize()} Report</title>')
            file.writelines(f'<link rel="stylesheet" type="text/css" href="../stylesheet.css">')
            file.writelines(f'</head><body><ul id="resultsList"></ul><br><br>')
            file.writelines(f'<h1>{tool.capitalize()} Report</h1><div class="search-bar">')
            file.writelines(f'<input type="text" class="search-input" placeholder="Search..." id="searchInput"></div>')
            file.writelines(f'<div class="gray-rectangle"><a href="../all_subdomains.html">')
            file.writelines(f'<button class="right-button">All Subdomains</button></a>')
            file.writelines(f'<a href="../simplified_subdomains.html"><button class="rb2">Simplified Subdomains</button>')
            file.writelines(f'</a><a href="../../html_report.html"><button class="rb3">Main Menu</button></a></div><hr class="test">')
            
            tool_vulns = vuln_scanning.vulns.get_vulns_for(tool)
            
            hours, remainder = divmod(utils.file_utils.get_time.get_time(tool), 3600)
            minutes, seconds = divmod(remainder, 60)
            
            file.writelines(f'<h3>Total vulnerabilities discovered: {len(tool_vulns)}</h3><h3>Total execution Time: {"0" if len(str(int(hours))) == 1 else ""}{str(int(hours))}:{"0" if len(str(int(minutes))) == 1 else ""}{str(int(minutes))}:{"0" if len(str(int(seconds))) == 1 else ""}{str(int(seconds))}</h3><hr><h2>VULNERABILITIES DISCOVERED:</h2><hr>')
            
            for vulnerability in tool_vulns:
                file.writelines(f'<h4><a href="../subdomains/{vulnerability[1]}.html" class="normal-link" target="_blank">{vulnerability[1]}</a></h4><p>info: {vulnerability[2]}</p><p>severity: {vulnerability[3]}</p><br>')
                
            file.writelines('<script>searchList = [')
            
            search_list = [x[1] for x in tool_vulns]
            
            for x in range(len(search_list)):
                if x != len(search_list) - 1:
                    file.writelines(f'"{search_list[x]}",')
                else:
                    file.writelines(f'"{search_list[x]}"];')
                    
            file.writelines("const searchInput = document.getElementById('searchInput');")
            file.writelines("const myList = document.getElementById('resultsList');")
            file.writelines("searchInput.addEventListener('input', function() {const searchQuery = searchInput.value.toLowerCase();while (myList.firstChild) {myList.removeChild(myList.firstChild);}")
            file.writelines("if (searchQuery.length >= 4) {searchList.forEach(function(domain) {if (domain.includes(searchQuery)) {const newItem = document.createElement('h3');")
            file.writelines("newItem.textContent = domain; myList.appendChild(newItem);myList.classList.add('resultList');newItem.addEventListener('click', function() {")
            file.writelines("const destinationURL = `../subdomains/${domain}.html`; window.open(destinationURL, '_blank');});}});}});</script></body></html>")
            
    for sub in list(set([x[1] for x in subs])):
        with open(f'{utils.file_utils.get_working_directory.get_wd()}/html_report/utils/subdomains/{sub}.html', 'w') as file:
            file.writelines(f'<!DOCTYPE html><html><head><title>{sub} Report</title>')
            file.writelines(f'<link rel="stylesheet" type="text/css" href="../stylesheet.css">')
            file.writelines(f'</head><body><ul id="resultsList"></ul><br><br>')
            file.writelines(f'<h1>{sub} Report</h1><div class="search-bar">')
            file.writelines(f'<input type="text" class="search-input" placeholder="Search..." id="searchInput"></div>')
            file.writelines(f'<div class="gray-rectangle"><a href="../all_subdomains.html">')
            file.writelines(f'<button class="right-button">All Subdomains</button></a>')
            file.writelines(f'<a href="../simplified_subdomains.html"><button class="rb2">Simplified Subdomains</button>')
            file.writelines(f'</a><a href="../../html_report.html"><button class="rb3">Main Menu</button></a></div><hr class="test">')
            file.writelines(f'<h3><a href="https://{sub}" target="_blank" class="normal-link">https://{sub}</h3></a>')
            file.writelines(f'<h3><a href="http://{sub}" target="_blank" class="normal-link">http://{sub}</h3></a>')
            file.writelines(f'<img src="../../../screenshots/http_{sub}.png" onerror="this.src=\'../../../screenshots/https_{sub}.png\'" class="image" style="border-radius: 30px;">')
            
            file.writelines('<hr><h2>DISCOVERED BY: </h2>')
            
            for i in subs:
                if i[1] == sub:
                    file.writelines(f'<a href="../tools/{i[0]}.html" class="normal-link"><h3>{i[0].capitalize()}</h3></a>')
                    
            file.writelines('<hr><h2>SIMILAR SUBDOMAINS:</h2>')
            
            similar_subdomains = []
            
            for i in utils.tool_utils.resolver_utils.resolver.get_similar_screenshots().keys():
                for ii in utils.tool_utils.resolver_utils.resolver.get_similar_screenshots()[i]:
                    if 'http_' in ii:
                        y = ii[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_'):-4]
                    else:
                        y = ii[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_'):-4]
                    if y == sub:
                        for iii in utils.tool_utils.resolver_utils.resolver.get_similar_screenshots()[i]:
                            if 'https_' in iii:
                                similar_subdomains.append(iii[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_'):-4])
                            else:
                                similar_subdomains.append(iii[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_'):-4])
                                
            for i in list(set(similar_subdomains)):
                if i != sub:
                    file.writelines(f'<a href="{i}.html" class="normal-link"><h3>{i}</h3></a>')
                
            file.writelines(f'<hr><h2>VULNERABILITIES:</h2><hr>')
            
            subdomain_vulnerabilities = []
            vulned = []

            for i in sorted([x[1] for x in subs], key=len, reverse=True):
                for x in  vuln_scanning.vulns.get_vulns():
                    ii = x[1]
                    ok = True 
                    for b in vulned:
                        if i in b:
                            ok = False 
                            break
                    if i in ii and ok:
                        vulned.append(i)
                        if i == sub:
                            subdomain_vulnerabilities.append(x)
                        break
                    
            written = set()
            
            for sub_vuln in subdomain_vulnerabilities:
                file.writelines(f'<a href="../tools/{sub_vuln[0]}.html" class="normal-link"><h3>{sub_vuln[0].capitalize()}</h3></a>')
                for k in subdomain_vulnerabilities:
                    if k[0] == sub_vuln[0] and k[0] not in written:
                        file.writelines(f'<br><p>Info: {k[2]}</p><p>Severity: {k[3]}</p>')
                written.add(sub_vuln[0])
                
            file.writelines('<hr><script>searchList = [')
            
            search_list = [x[1] for x in subs]
            
            for x in range(len(search_list)):
                if x != len(search_list) - 1:
                    file.writelines(f'"{search_list[x]}",')
                else:
                    file.writelines(f'"{search_list[x]}"];')
                    
            file.writelines("const searchInput = document.getElementById('searchInput');")
            file.writelines("const myList = document.getElementById('resultsList');")
            file.writelines("searchInput.addEventListener('input', function() {const searchQuery = searchInput.value.toLowerCase();while (myList.firstChild) {myList.removeChild(myList.firstChild);}")
            file.writelines("if (searchQuery.length >= 4) {searchList.forEach(function(domain) {if (domain.includes(searchQuery)) {const newItem = document.createElement('h3');")
            file.writelines("newItem.textContent = domain; myList.appendChild(newItem);myList.classList.add('resultList');newItem.addEventListener('click', function() {")
            file.writelines("const destinationURL = `../subdomains/${domain}.html`; window.open(destinationURL, '_blank');});}});}});</script></body></html>")
            
    with open(f'{utils.file_utils.get_working_directory.get_wd()}/html_report/utils/simplified_subdomains.html', 'w') as file:
            file.writelines(f'<!DOCTYPE html><html><head><title>Simplified Subdomains</title>')
            file.writelines(f'<link rel="stylesheet" type="text/css" href="stylesheet.css">')
            file.writelines(f'</head><body><ul id="resultsList"></ul><br><br>')
            file.writelines(f'<h1>Simplified Subdomains</h1><div class="search-bar">')
            file.writelines(f'<input type="text" class="search-input" placeholder="Search..." id="searchInput"></div>')
            file.writelines(f'<div class="gray-rectangle"><a href="all_subdomains.html">')
            file.writelines(f'<button class="right-button">All Subdomains</button></a>')
            file.writelines(f'<a href="simplified_subdomains.html"><button class="rb2">Simplified Subdomains</button>')
            file.writelines(f'</a><a href="../html_report.html"><button class="rb3">Main Menu</button></a></div><hr class="test">')
                        
            non_vuln = []
            vulned = []
            
            search_list = []
            
            for i in sorted([x[1] for x in subs], key=len, reverse=True):
                search_list.append(i)
                vulnerable = False
                for ii in [x[1] for x in vuln_scanning.vulns.get_vulns()]:
                    ok = True 
                    for b in vulned:
                        if i in b:
                            ok = False 
                            break
                    if i in ii and ok:
                        vulnerable = True
                        vulned.append(i)
                        break
                        
                        
                if vulnerable:
                    file.writelines(f'<a href="subdomains/{i}.html" class="normal-link" target="_blank"><h3>{i} [VULNERABLE]</h3></a>')
                else:
                    non_vuln.append(i)
                        
            for i in non_vuln:
                file.writelines(f'<a href="subdomains/{i}.html" class="normal-link" target="_blank"><h3>{i}</h3></a>')
                
            file.writelines('<script>searchList = [')
            
            search_list = [x[1] for x in subs]
            
            for x in range(len(search_list)):
                if x != len(search_list) - 1:
                    file.writelines(f'"{search_list[x]}",')
                else:
                    file.writelines(f'"{search_list[x]}"];')
                    
            file.writelines("const searchInput = document.getElementById('searchInput');")
            file.writelines("const myList = document.getElementById('resultsList');")
            file.writelines("searchInput.addEventListener('input', function() {const searchQuery = searchInput.value.toLowerCase();while (myList.firstChild) {myList.removeChild(myList.firstChild);}")
            file.writelines("if (searchQuery.length >= 4) {searchList.forEach(function(domain) {if (domain.includes(searchQuery)) {const newItem = document.createElement('h3');")
            file.writelines("newItem.textContent = domain; myList.appendChild(newItem);myList.classList.add('resultList');newItem.addEventListener('click', function() {")
            file.writelines("const destinationURL = `subdomains/${domain}.html`; window.open(destinationURL, '_blank');});}});}});</script></body></html>")
            
    with open(f'{utils.file_utils.get_working_directory.get_wd()}/html_report/utils/all_subdomains.html', 'w') as file:
            file.writelines(f'<!DOCTYPE html><html><head><title>All Subdomains</title>')
            file.writelines(f'<link rel="stylesheet" type="text/css" href="stylesheet.css">')
            file.writelines('<style>body {text-align: center;}.centered-content {display: inline-block;text-align: left;}</style>')
            file.writelines(f'</head><body><ul id="resultsList"></ul><hr><hr><br>')
            file.writelines('<div class="centered-content">')
            file.writelines(f'<div class="search-bar">')
            file.writelines(f'<input type="text" class="search-input" placeholder="Search..." id="searchInput"></div>')
            file.writelines(f'<div class="gray-rectangle"><a href="all_subdomains.html">')
            file.writelines(f'<button class="right-button">All Subdomains</button></a>')
            file.writelines(f'<a href="simplified_subdomains.html"><button class="rb2">Simplified Subdomains</button>')
            file.writelines(f'</a><a href="../html_report.html"><button class="rb3">Main Menu</button></a></div><hr class="test">')
            
            dv_count = 0
            
            def write_image_subdomain(domain, vulnerable, count):
                c = 1
                file.writelines(f'<div id="dv{count}" class="invisible"><hr class="all-hr">')
                file.writelines(f'<h3><a class="normal-link" href="subdomains/{domain}.html" target="_blank" id="{domain}_main">{domain}{"[VULNERABLE]" if vulnerable else ""}</a></h3>')
                file.writelines(f'<h4><a class="normal-link" href="https://{domain}" id="{domain}_https" target="_blank">https://{domain}</a></h4>')
                file.writelines(f'<h4><a class="normal-link" href="http://{domain}" id="{domain}_http" target="_blank">http://{domain}</a></h4>')
                file.writelines(f'<br><img src="../../screenshots/http_{domain}.png" onerror="this.src=\'../../screenshots/https_{domain}.png\'" class="all-image" id="{domain}_image">')
                file.writelines(f'<button class="arrow-button1" onclick="cycleImage(domain_{domain.replace(".", "_").replace("-", "p")}, 1)">></button>')
                file.writelines(f'<button class="arrow-button2" onclick="cycleImage(domain_{domain.replace(".", "_").replace("-", "p")}, -1)"><</button>')
                file.writelines(f'<h3 class="counter" id="{domain}_counter"></h3><br><br></div>')
                file.writelines(f'<script>')
                file.writelines(f"let domain_{domain.replace('.', '_').replace('-', 'p')} ")
                file.writelines("= {\n")
                file.writelines(f'domains: ["{domain}"')
                try:
                    for i in utils.tool_utils.resolver_utils.resolver.get_similar_screenshots()[f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_' + domain + '.png']:
                        if 'https_' in i:
                            y = i[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_'):-4]
                        else:
                            y = i[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_'):-4]
                        if y != domain:
                            vulned = []
                            ok = False
                            search_list = []
                            
                            for i in sorted([x[1] for x in subs], key=len, reverse=True):
                                search_list.append(i)
                                vulnerable = False
                                for ii in [x[1] for x in vuln_scanning.vulns.get_vulns()]:
                                    ok = True 
                                    for b in vulned:
                                        if i in b:
                                            ok = False 
                                            break
                                    if i in ii and ok:
                                        vulnerable = True
                                        vulned.append(i)
                                        break
                                    
                                if y == i and vulnerable:
                                    file.writelines(f', "{y}[VULNERABLE]"')
                                    ok = True
                                    
                            if not ok:
                                file.writelines(f', "{y}"')
                    file.writelines(f'],\n')
                except:
                    pass
                    for i in utils.tool_utils.resolver_utils.resolver.get_similar_screenshots()[f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_' + domain + '.png']:
                        if 'https_' in i:
                            y = i[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_'):-4]
                        else:
                            y = i[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_'):-4]
                        if y != domain:
                            vulned = []
                            ok = False
                            search_list = []
                            
                            for i in sorted([x[1] for x in subs], key=len, reverse=True):
                                search_list.append(i)
                                vulnerable = False
                                for ii in [x[1] for x in vuln_scanning.vulns.get_vulns()]:
                                    ok = True 
                                    for b in vulned:
                                        if i in b:
                                            ok = False 
                                            break
                                    if i in ii and ok:
                                        vulnerable = True
                                        vulned.append(i)
                                        break
                                    
                                if y == i and vulnerable:
                                    file.writelines(f', "{y}[VULNERABLE]"')
                                    ok = True
                                    
                            if not ok:
                                file.writelines(f', "{y}"')
                    file.writelines(f'],\n')
                
                file.writelines(f'imageList: ["../../screenshots/http_{domain}.png"')
                try:
                    for i in utils.tool_utils.resolver_utils.resolver.get_similar_screenshots()[f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_' + domain + '.png']:
                        if i[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_'):-4] != domain and i[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_'):-4] != domain:
                            file.writelines(f', "../../{i[len(utils.file_utils.get_working_directory.get_wd()) + 1:]}"')
                            c += 1
                    file.writelines(f'],\n')
                except:
                    pass
                    for i in utils.tool_utils.resolver_utils.resolver.get_similar_screenshots()[f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_' + domain + '.png']:
                        if i[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_'):-4] != domain and i[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_'):-4] != domain:
                            file.writelines(f', "../../{i[len(utils.file_utils.get_working_directory.get_wd()) + 1:]}"')
                            c += 1
                    file.writelines(f'],\n')

                file.writelines(f'imageElement: document.getElementById("{domain}_image"),\n')
                file.writelines("index: 0,\n")
                file.writelines(f'counterElement: document.getElementById("{domain}_counter"),\n')
                file.writelines(f'he1: document.getElementById("{domain}_https"),\n')
                file.writelines(f'he2: document.getElementById("{domain}_http"),\n')
                file.writelines(f'he3: document.getElementById("{domain}_main")')
                file.writelines("};\n")
                file.writelines(f"domain_{domain.replace('.', '_').replace('-', 'p')}.counterElement.textContent = '1/{c}'")
                file.writelines(f'</script>')
                
                nonlocal dv_count
                dv_count += c
                        
            non_vuln = []
            vulned = []
            
            search_list = []
            
            sub_count = 1
            
            for i in sorted([x for x in utils.tool_utils.resolver_utils.resolver.get_similar_screenshots().keys()], key=len, reverse=True):
                search_list.append(i)
                vulnerable = False
                for ii in [x[1] for x in vuln_scanning.vulns.get_vulns()]:
                    ok = True 
                    for b in vulned:
                        if i in b:
                            ok = False 
                            break
                    if i in ii and ok:
                        vulnerable = True
                        vulned.append(i)
                        break
                        
                        
                if vulnerable:
                    if 'https_' in i:
                        write_image_subdomain(i[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_'):-4], True, sub_count)
                    else:
                        write_image_subdomain(i[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_'):-4], True, sub_count)
                    sub_count += 1
                else:
                    non_vuln.append(i)
                        
            for i in non_vuln:
                if 'https_' in i:
                    write_image_subdomain(i[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_'):-4], False, sub_count)
                else:
                    write_image_subdomain(i[len(f'{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_'):-4], False, sub_count)
                sub_count += 1
                
            file.writelines('<hr class="all-hr"><button class="pretty-button more-button" id="moreButton">More</button><hr class="all-hr"> </div><script>searchList = [')
            
            search_list = [x[1] for x in subs]
            
            for x in range(len(search_list)):
                if x != len(search_list) - 1:
                    file.writelines(f'"{search_list[x]}",')
                else:
                    file.writelines(f'"{search_list[x]}"];')
                    
            file.writelines("const searchInput = document.getElementById('searchInput');")
            file.writelines("const myList = document.getElementById('resultsList');")
            file.writelines("searchInput.addEventListener('input', function() {const searchQuery = searchInput.value.toLowerCase();while (myList.firstChild) {myList.removeChild(myList.firstChild);}")
            file.writelines("if (searchQuery.length >= 4) {searchList.forEach(function(domain) {if (domain.includes(searchQuery)) {const newItem = document.createElement('h3');")
            file.writelines("newItem.textContent = domain; myList.appendChild(newItem);myList.classList.add('resultList');newItem.addEventListener('click', function() {")
            file.writelines("const destinationURL = `subdomains/${domain}.html`; window.open(destinationURL, '_blank');});}});}});")
            file.writelines("function setVisible(elementName) {const element = document.getElementById(elementName);element.classList.remove('invisible');};let counter = 0;")
            file.writelines("function handleClick() {\n")
            file.writelines("counter += 10;\n")
            file.writelines("if (document.getElementById('dv' + String(counter))) {")
            file.writelines("setVisible('dv' + String(counter))\n}\n")
            file.writelines("if (document.getElementById('dv' + String(counter - 1))) {")
            file.writelines("setVisible('dv' + String(counter - 1))\n}\n")
            file.writelines("if (document.getElementById('dv' + String(counter - 2))) {")
            file.writelines("setVisible('dv' + String(counter - 2))\n}\n")
            file.writelines("if (document.getElementById('dv' + String(counter - 3))) {")
            file.writelines("setVisible('dv' + String(counter - 3))\n}\n")
            file.writelines("if (document.getElementById('dv' + String(counter - 4))) {")
            file.writelines("setVisible('dv' + String(counter - 4))\n}\n")
            file.writelines("if (document.getElementById('dv' + String(counter - 5))) {")
            file.writelines("setVisible('dv' + String(counter - 5))\n}\n")
            file.writelines("if (document.getElementById('dv' + String(counter - 6))) {")
            file.writelines("setVisible('dv' + String(counter - 6))\n}\n")
            file.writelines("if (document.getElementById('dv' + String(counter - 7))) {")
            file.writelines("setVisible('dv' + String(counter - 7))\n}\n")
            file.writelines("if (document.getElementById('dv' + String(counter - 8))) {")
            file.writelines("setVisible('dv' + String(counter - 8))\n}\n")
            file.writelines("if (document.getElementById('dv' + String(counter - 9))) {")
            file.writelines("setVisible('dv' + String(counter - 9))}\n}\n")
            file.writelines("const button = document.getElementById('moreButton');\n")
            file.writelines("button.addEventListener('click', handleClick);\n")
            file.writelines('function getListLength(domain, element) {\n')
            file.writelines('document.getElementById(element).textContent = "1/" + String(domain.imageList.length)\n')
            file.writelines('domain.he1.textContent = "https://" + domain.domains[0]\n')
            file.writelines('domain.he2.textContent = "http://" + domain.domains[0]\n')
            file.writelines('domain.he3.textContent = domain.domains[0]\n')
            file.writelines('}\n')
 
            file.writelines('function cycleImage(domain, count) {\n')
            file.writelines('domain.index = (domain.index + count) % domain.imageList.length;\n')
            file.writelines('if (domain.index === -1) {\n')
            file.writelines('domain.index = domain.imageList.length - 1;\n')
            file.writelines('}\n')
            file.writelines('domain.imageElement.src = domain.imageList[domain.index];\n')
            file.writelines('domain.counterElement.textContent = String(domain.index + 1) + "/" + String(domain.imageList.length);\n')
            
            file.writelines("const v_domain = domain.domains[domain.index].split('[');\n")
            file.writelines("let p_domain = v_domain[0];\n")
            file.writelines('domain.he3.textContent = domain.domains[domain.index]\n')
            file.writelines('domain.he1.textContent = "https://" + p_domain\n')
            file.writelines('domain.he2.textContent = "http://" + p_domain\n')
            file.writelines('domain.he1.href = "https://" + domain.domains[domain.index]\n')
            file.writelines('domain.he2.href = "http://" + domain.domains[domain.index]\n')
            file.writelines('domain.he3.href = "subdomains/" + domain.domains[domain.index] + ".html"\n')
            file.writelines('}\n')
            file.writelines("</script></body></html>\n")    
            
                    
        
    
        
