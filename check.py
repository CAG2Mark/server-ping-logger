import os
import os.path
from datetime import datetime

# Read hosts
hosts = [x.replace("\n", "") for x in open("hosts.txt", "r").readlines()]

def time_obj(unix_time):
    return datetime.utcfromtimestamp(int(unix_time)).strftime('%Y-%m-%d %H:%M:%S')


for host in hosts:
    filepath = f"out/{host}.csv"
    exists = os.path.isfile(filepath)
    # read file
    data_raw = open(filepath, "r").read().split("\n")[1:]
    data = [
        [int(x.split(",")[0].strip()), 
        float(x.split(",")[1].strip())]
        for x in data_raw]
    
    # get sum
    sm = 0
    mn = data[0][1]
    min_time = data[0][0]
    cnt = len(data)
    for d in data:
        sm += d[1]
        if d[1] < mn: # get min
            mn = d[1]
            min_time = d[0]

    avg = sm / cnt

    # get sdev
    sdev = 0
    for d in data:
        diff = d[1] - avg
        sdev += diff*diff
    sdev /= cnt
    sdev **= 0.5
    
    i = len(data) - 1
    while not(avg - 3*sdev < data[i][1] < avg + 3*sdev):
        i -= 1

    latest = data[i]


    print(f"""{host} [relevant: {int(latest[1])}ms]:
                    \tmin: {int(mn)}ms at {time_obj(min_time)}z
                    \tavg: {int(avg)}ms from {cnt} data points, with sdev {sdev}
                    \tnew: {int(latest[1])}ms at {time_obj(latest[0])}z\n""")

