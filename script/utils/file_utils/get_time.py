times = {}

def add_time(set):
    if set[0] not in times.keys():
        times[set[0]] = set[1]
    else:
        times[set[0]] = times[set[0]] + set[1]

def get_time(tool):
    return times.get(tool)

def get_times():
    return times