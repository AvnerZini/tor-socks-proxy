import requests
import time
import argparse

ips = []
session = requests.session()
session.proxies = {}

ipInfo = 'https://ipinfo.tw/ip'
socksAddress = 'socks5h://127.0.0.1:9150'

myIp = session.get(ipInfo)
print("My current IP without Tor: " + myIp.text)


def ping_tor():
    session.proxies['http'] = socksAddress
    session.proxies['https'] = socksAddress
    tor = session.get(ipInfo)

    if tor.text.strip() not in ips:
        ips.append(tor.text.strip())
        session.close()
        print("My IP using Tor: " + tor.text)
        print("All Ips from Tor: ", ips)

    else:
        print(tor.text.strip() + " The same IP repeated twice, build is failing")
        exit(1)


# Function time.time returns the current time in seconds since 1st Jan 1970
time_to_start = time.time()
time_to_end = time.time() + 60 * 2
while time.time() < time_to_end:
    ping_tor()
    time.sleep(10.0 - ((time.time() - time_to_start) % 10.0))
