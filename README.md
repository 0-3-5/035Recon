# 035Recon
Recon framework for bug bounty hunting and pentesting

# Installation
```
git clone https://github.com/0-3-5/035Recon
cd 035Recon
chmod +x setup.sh
./setup.sh
```
# Usage
035Recon [args]\n
If this does not work run the script directly from the file:\n
python3 path/to/035Recon/script/main.py\n

# Commands

```
################################################################################
                                                                                                                                                                                                                                           
    ░█████╗░██████╗░███████╗    ██████╗░███████╗░█████╗░░█████╗░███╗░░██╗                                                                                                                                                                  
    ██╔══██╗╚════██╗██╔════╝    ██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░██║
    ██║░░██║░█████╔╝██████╗░    ██████╔╝█████╗░░██║░░╚═╝██║░░██║██╔██╗██║
    ██║░░██║░╚═══██╗╚════██╗    ██╔══██╗██╔══╝░░██║░░██╗██║░░██║██║╚████║
    ╚█████╔╝██████╔╝██████╔╝    ██║░░██║███████╗╚█████╔╝╚█████╔╝██║░╚███║
    ░╚════╝░╚═════╝░╚═════╝░    ╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚══╝
    
################################################################################
Made By 035#0824
https://www.google.com
Do not use for illegal activity!
Tools not included, you must download them yourself!
Parallel lines have so much in common. It's a shame they'll never meet.
################################################################################
                                                                                                                                                                                                                                           
Flags:
                                                                                                                                                                                                                                           
TARGET DOMAIN INFORMATION:
-d : Target domain.
-df : Target domain .txt file, domains have to be separated by \n newline delimiter.
-ds : Target domains separated by commas.
-s : Specify scope domains from a file (default null).
-ss : Set scope domains to target domains.
                                                                                                                                                                                                                                           
SUBDOMAIN ENUMERATION OPTIONS:
-amass : Use Amass enum. https://github.com/owasp-amass/amass
-amass-exec : Amass max Execution time per domain in minutes.
-harv : Use TheHarvester. https://github.com/laramies/theHarvester
-sub : Use Subfinder. https://github.com/projectdiscovery/subfinder
-asset : Use Assetfinder. https://github.com/tomnomnom/assetfinder
-git : Scrape Github for subdomains. https://github.com/gwen001/github-search
-git-token : Github api key for -git argument.
-brute : DNS bruteforcing. https://github.com/blechschmidt/massdns
-brute-list : Wordlist for DNS bruteforcing.(Do not include for default 7 million subdomain list.)
-alt : Alteration scanning.
-link-go : Linked discovery using Gospider. https://github.com/jaeles-project/gospider
-link-sub : Linked discovery using Subdomainizer. https://github.com/nsonaniya2010/SubDomainizer
-link-go-all : Linked discovery using Gospider on all previously discovered subdomains. https://github.com/jaeles-project/gospider
-link-sub-all : Linked discovery using Subdomainizer on all previously discovered subdomains. https://github.com/nsonaniya2010/SubDomainizer
-cname : Cname resolution for additonal domains.
-all-recon : All enumeration options.
-all-recon-short : All enumeration options except amass, bruteforcing and heavy linked discovery.
                                                                                                                                                                                                                                           
VULENRABILITY SCANNING OPTIONS:
-take : Check for subdomain takeover vulnerabilities using subzy. https://github.com/PentestPad/subzy
-take-t : How many threads to use for subzy (default 100)
-spray : Check for default credentials on ports using Brutespray. https://github.com/x90skysn3k/brutespray
-spray-t : How many threads to use for brutespray (default 25)
-social : Check for social media link takeover. https://github.com/utkusen/socialhunter
-social-t : How many threads to use for social media link takeover (default 100)
-nuclei : Use default nuclei scanning templates. https://github.com/projectdiscovery/nuclei
-nuclei-t : Threads to run nuclei (default 10).
-nuclei-c : Run nuclei using custom templates (follow this argument with the template directory).
-similar : Only run vulnerability scanning on unique subdomains.
-all-vuln : All vulnerability scanning options.
                                                                                                                                                                                                                                           
OUTPUT OPTIONS:
-wd : Working directory of 035 Recon (default ".").
-screenshot-t : Threads for taking screenshots and final subdmoain resolution (default 20).
                                                                                                                                                                                                                                           
PREFORMANCE OPTIONS:
-t : How many threads to use (default 5).
-m : Use multithreading in single domain enumeration.
-mv : Use multithreading in vulnerability scanning.
-rec : Use amass intel on any AS numbers found by TheHarvester and Amass and repeat the process.
-asns : Input known AS numbers from a file if using -rec.
-casns : Input comma separated known AS numbers.
-resolvers : Custom resolver file for subdomain bruteforcing and subdomain resolution.
-rep : How many times to repeat running a certaing tool per domain (default 1, ex: -sub -sub-count 5).
                                                                                                                                                                                                                                           
CUSTOM SUBDOMAIN ENUMERATION AND VULNERABILITY SCANNING:
-cr : Custom recon tool config file name or folder location, can be used multiple times.
-cv : Custom vulnerability scanning tool config file name or folder location, can be used multiple times.
-custom-help : Custom vulnerability and recon help.
