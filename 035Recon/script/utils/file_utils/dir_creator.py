import os

def make_dir(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)