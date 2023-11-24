vulns = set()

def get_vulns():
    return vulns

def add_vuln_info(tool, domain, info, severity):
    vulns.add((tool, domain, info, severity))

def set_vulns(vulns):
    vulns.update(vulns)
    
def get_vulns_for(tool):
    out = []
    for i in vulns:
        if i[0] == tool:
            out.append(i)
    return out