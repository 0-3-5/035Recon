import time

time_start = None

def init_time():
    global time_start
    time_start = time.time()


def get_time():
    global time_start
    return time_start