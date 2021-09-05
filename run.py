import os
import time
import os.path

# Read hosts
hosts = [x.replace("\n", "") for x in open("hosts.txt", "r").readlines()]

def ping(host):
    # unix-like only
    res = os.popen(f"ping {host} -c 1").read()
    # parse response
    latency = res\
        .split("\n")[-2]\
        .split("= ")[1]\
        .split(" ms")[0]\
        .split("/")[0]
    
    return (int(time.time()), float(latency))

if not os.path.exists("out"): os.makedirs("out")

for host in hosts:
    res = ping(host)
    filepath = f"out/{host}.csv"
    exists = os.path.isfile(filepath)
    # Create file
    outfile = open(filepath, "a")
    # Check if output file exists
    if not exists:
        outfile.write("\"time\",\"ping\"")
    outfile.write(f"\n{res[0]},{res[1]}")
    