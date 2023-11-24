
from colorama import init, Fore

def custom_menu():

    init(autoreset=True)

    print(Fore.RED + '\033[1mCUSTOM RECON AND VULNERABILITY OPTIONS HELP:\n')

    print(Fore.RED + '\033[1mRECON:')
    print(Fore.RED + 'You can addd more tools to be used for recon other than the default ones.')
    print(Fore.RED + 'They will show up on the report and the discovered subdomains will be vulnerability scanned.')
    print(Fore.RED + 'To add a new recon tool you must make a .txt file with the name of the tool. The name must be lower case!')
    print(Fore.RED + 'Inside the file you have to write the terminal command you want to execute, replacing the name of the seed domain with $domain$ and the name of the out file, if any, to $file$/seed_name.txt.')
    print(Fore.RED + '035Recon will atempt to find subdomains in the output of the command, looking any words strating with "https://", "http://" and any word sthat have one or more "." inside.')
    print(Fore.RED + 'To run the custom tool add the flag -cr <.txt file location or folder where it is located>\n')

    print(Fore.RED + '\033[1mVULNERABILITY SCANNING:')
    print(Fore.RED + 'You can addd more tools to be used for vulnerability scanning other than the default ones.')
    print(Fore.RED + 'Any found vulnerabilities will show up on the report.')
    print(Fore.RED + 'To add a new vulnerability scanning tool you must make a .txt file with the name of the tool. The name must be lower case!')
    print(Fore.RED + 'Inside the file you have to write the terminal command you want to execute, replacing the domain with $domain$ and the name of the out file, if any, to $file$/tool_name.txt.')
    print(Fore.RED + 'Any lines of output that you want parsed as a vulnerability for the report must look like:')
    print(Fore.RED + '[VULN],tool,domain,info,severity')
    print(Fore.RED + 'Example: [VULN],subzy,sub.example.com,Subdomain Takeover!!!,high')
    print(Fore.RED + 'If you want to use multiple threads for the tool add the number of threads you want after the name of the file.')
    print(Fore.RED + 'Example: -cv example.txt 10')
    print(Fore.RED + 'To run the custom tool add the flag -cv <.txt file location or folder where it is located>')