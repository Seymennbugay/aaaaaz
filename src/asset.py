import os
import re
import urllib.request
import time
import speedtest
from ipaddress import ip_address as ipchk



def speed_test():
    if _isConnected():
        print("\n\n")
        print("Your Internet Connection is Working Fine")
        print("Waiting for your Download Speed Results")
        time.sleep(2)
        wifi  = speedtest.Speedtest()
        print("\nSpeedTest Results\n")
        print("Wifi Download Speed : ", wifi.download()/(10**6),"Mb")
        print("Wifi Download Speed : ", wifi.upload()/(10**6),"Mb")
    else:
        main()
    return

def main():
    if _isConnected():
        print("Outside Server are Reachable")
    else:
        print("Outside Server are Not Reachable")
        src,path = trace_route()
        print("Router Path : ",path)
        if path == []:
            print("You are not connected to any Network")
            print('''
                  This can be due to :
                  1. You're connected to a known router
                  2. If you are using Ethernet Port, Then the Ethernet is not loose and have LED's Blinking
                  ''')
        elif ipchk(path[-1]).is_private:
            print(path)
            print(f"The packet is Stuck at Hop : {len(path)} at Router : {path[-1]}")
        else:
            print(f'''
                  The packet is Stuck at Public Router (ISP) Hop : {len(path)} at Router : {path[-1]}
                  Your Internet is working Fine, There might be outage in ISP Network.
                  Contact Your ISP.
                  ''')


def trace_route():
    try:
        path = os.popen('traceroute -m10 1.1.1.1').readlines()
        res = []
        for line in path:
            t = line.replace(" ",'')
            if ("***") in t: continue
            else:
                res.extend(re.findall('\(([^()]+)\)',t))
        return(res[0],res[1:])
    except:
        return (0,0)


def _isConnected(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

