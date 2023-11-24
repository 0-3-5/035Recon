import sys

def get_wd():
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-wd':
            return sys.argv[i + 1]
    else:
        return '035Recon_Output'