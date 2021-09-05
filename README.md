# server-ping-logger
Log and presents ping data to a list of servers for your bad ISP

# How to use
1. Create a file called `hosts.txt` in the project directory. Enter a list of hosts, separated by a line that you want to log the ping to. For example:
```
foo.host1.xyz
bar.host2.xyz
what.host3.xyz
```
2. Run `run.py` to ping all of the hosts ONCE EACH. The results of these pings will be logged to the file `out/<hostname>.csv`.
3. To get stats on all of the hosts, run `check.py` and the stats will be outputted in your console.

# Caveats
If the host cannot be resolved or if the ping times out, this script will break.
