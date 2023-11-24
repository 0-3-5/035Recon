from colorama import Fore
import sys

def no_target():
    sys.exit(Fore.RED + 'Please specify aleast one traget using -d, -ds, -df.')

def broken_target():
    sys.exit(Fore.RED + 'Please specify a correct seed domain ex:example.com.')

def broken_threads():
    sys.exit(Fore.RED + 'Threads must be a non null, natural number.')

def broken_github():
    sys.exit(Fore.RED + '-git argument requires -git-token + YOUR_GITHUB_API_TOKEN to run.')

def working_directory_exists():
    sys.exit(Fore.RED + 'The provided working directory already exists.')