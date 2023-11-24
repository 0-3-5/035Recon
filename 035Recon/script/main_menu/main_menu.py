import time
from colorama import init, Fore
import random

def main_menu():

    print(Fore.RED + 80 * '#')

    init(autoreset=True)

    ascii_art = """
    ░█████╗░██████╗░███████╗    ██████╗░███████╗░█████╗░░█████╗░███╗░░██╗
    ██╔══██╗╚════██╗██╔════╝    ██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░██║
    ██║░░██║░█████╔╝██████╗░    ██████╔╝█████╗░░██║░░╚═╝██║░░██║██╔██╗██║
    ██║░░██║░╚═══██╗╚════██╗    ██╔══██╗██╔══╝░░██║░░██╗██║░░██║██║╚████║
    ╚█████╔╝██████╔╝██████╔╝    ██║░░██║███████╗╚█████╔╝╚█████╔╝██║░╚███║
    ░╚════╝░╚═════╝░╚═════╝░    ╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚══╝
    """

    for char in ascii_art:
        if char != '\n':
            print(f"{Fore.RED}{char}", end='')
        else:
            print(char, end='')

    print(Fore.RESET)

    print(Fore.RED + 80 * '#')

    quotes = [
        'test1',
        'V1c5MUlHaGhkbVVnYzI5c2RtVmtJSFJvWlNCamFHRnNiR0Z1WjJVaA==',
        'skibidy toilet',
        '<script>alert()</script>',
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "How do you organize a space party? You 'planet'!",
    "Why couldn't the bicycle stand up by itself? It was two-tired.",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "I used to play piano by ear, but now I use my hands.",
    "I'm on a seafood diet. I see food and I eat it!",
    "Why did the math book look sad? Because it had too many problems.",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why don't scientists trust stairs? Because they're always up to something!",
    "How do you make a tissue dance? You put a little boogie in it!",
    "What do you call a can opener that doesn't work? A can't opener!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "What's orange and sounds like a parrot? A carrot!",
    "I used to play piano by ear, but now I use my hands.",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Why don't skeletons fight each other? They don't have the guts!"
              ]

    print(Fore.RED + '\033[1mMade By 035#0824')
    print(Fore.RED + '\033[1mhttps://www.google.com')
    print(Fore.RED + '\033[1mDo not use for illegal activity!')
    print(Fore.RED + '\033[1mTools not included, you must download them yourself!')
    print(Fore.RED + '\033[1m' + quotes[random.randint(0, len(quotes) - 1)])

    print(Fore.RED + 80 * '#' + '\n')

    print(Fore.RED + '\033[1mFlags:\n')

    print(Fore.RED + '\033[1mTARGET DOMAIN INFORMATION:')
    print(Fore.RED + '-d : Target domain.')
    print(Fore.RED + '-df : Target domain .txt file, domains have to be separated by \\n newline delimiter.')
    print(Fore.RED + '-ds : Target domains separated by commas.')
    print(Fore.RED + '-s : Specify scope domains from a file (default null).')
    print(Fore.RED + '-ss : Set scope domains to target domains.\n')

    print(Fore.RED + '\033[1mSUBDOMAIN ENUMERATION OPTIONS:')
    print(Fore.RED + '-amass : Use Amass enum. https://github.com/owasp-amass/amass')
    print(Fore.RED + '-amass-exec : Amass max Execution time per domain in minutes.')
    print(Fore.RED + '-harv : Use TheHarvester. https://github.com/laramies/theHarvester')
    print(Fore.RED + '-sub : Use Subfinder. https://github.com/projectdiscovery/subfinder')
    print(Fore.RED + '-asset : Use Assetfinder. https://github.com/tomnomnom/assetfinder')
    print(Fore.RED + '-git : Scrape Github for subdomains. https://github.com/gwen001/github-search')
    print(Fore.RED + '-git-token : Github api key for -git argument.')
    print(Fore.RED + '-brute : DNS bruteforcing. https://github.com/blechschmidt/massdns')
    print(Fore.RED + '-brute-list : Wordlist for DNS bruteforcing.(Do not include for default 7 million subdomain list.)')
    print(Fore.RED + '-alt : Alteration scanning.')
    print(Fore.RED + '-link-go : Linked discovery using Gospider. https://github.com/jaeles-project/gospider')
    print(Fore.RED + '-link-sub : Linked discovery using Subdomainizer. https://github.com/nsonaniya2010/SubDomainizer')
    print(Fore.RED + '-link-go-all : Linked discovery using Gospider on all previously discovered subdomains. https://github.com/jaeles-project/gospider')
    print(Fore.RED + '-link-sub-all : Linked discovery using Subdomainizer on all previously discovered subdomains. https://github.com/nsonaniya2010/SubDomainizer')
    print(Fore.RED + '-cname : Cname resolution for additonal domains.')
    print(Fore.RED + '-all-recon : All enumeration options.')
    print(Fore.RED + '-all-recon-short : All enumeration options except amass, bruteforcing and heavy linked discovery.\n')

    print(Fore.RED + '\033[1mVULENRABILITY SCANNING OPTIONS:')
    print(Fore.RED + '-take : Check for subdomain takeover vulnerabilities using subzy. https://github.com/PentestPad/subzy')
    print(Fore.RED + '-take-t : How many threads to use for subzy (default 100)')
    print(Fore.RED + '-spray : Check for default credentials on ports using Brutespray. https://github.com/x90skysn3k/brutespray')
    print(Fore.RED + '-spray-t : How many threads to use for brutespray (default 25)')
    print(Fore.RED + '-social : Check for social media link takeover. https://github.com/utkusen/socialhunter')
    print(Fore.RED + '-social-t : How many threads to use for social media link takeover (default 100)')
    print(Fore.RED + '-nuclei : Use default nuclei scanning templates. https://github.com/projectdiscovery/nuclei')
    print(Fore.RED + '-nuclei-t : Threads to run nuclei (default 10).')
    print(Fore.RED + '-nuclei-c : Run nuclei using custom templates (follow this argument with the template directory).')
    print(Fore.RED + '-similar : Only run vulnerability scanning on unique subdomains.')
    print(Fore.RED + '-all-vuln : All vulnerability scanning options.\n')

    print(Fore.RED + '\033[1mOUTPUT OPTIONS:')
    print(Fore.RED + '-wd : Working directory of 035 Recon (default ".").')
    print(Fore.RED + '-screenshot-t : Threads for taking screenshots and final subdmoain resolution (default 20).\n')

    print(Fore.RED + '\033[1mPREFORMANCE OPTIONS:')
    print(Fore.RED + '-t : How many threads to use (default 5).')
    print(Fore.RED + '-m : Use multithreading in single domain enumeration.')
    print(Fore.RED + '-mv : Use multithreading in vulnerability scanning.')
    print(Fore.RED + '-rec : Use amass intel on any AS numbers found by TheHarvester and Amass and repeat the process.')
    print(Fore.RED + '-asns : Input known AS numbers from a file if using -rec.')
    print(Fore.RED + '-casns : Input comma separated known AS numbers.')
    print(Fore.RED + '-resolvers : Custom resolver file for subdomain bruteforcing and subdomain resolution.')
    print(Fore.RED + '-rep : How many times to repeat running a certaing tool per domain (default 1, ex: -sub -sub-count 5).\n')

    print(Fore.RED + '\033[1mCUSTOM SUBDOMAIN ENUMERATION AND VULNERABILITY SCANNING:')
    print(Fore.RED + '-cr : Custom recon tool config file name or folder location, can be used multiple times.')
    print(Fore.RED + '-cv : Custom vulnerability scanning tool config file name or folder location, can be used multiple times.')
    print(Fore.RED + '-custom-help : Custom vulnerability and recon help.')
    