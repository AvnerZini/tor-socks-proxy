import requests
import time
import argparse

ips = []
session = requests.session()
session.proxies = {}

myIp = session.get('https://ipinfo.tw/ip')
print("My current IP without Tor: " + myIp.text)

port_cli = 'port'

parser = argparse.ArgumentParser(description='Process command line arguments')
parser.add_argument('--port',
                    required=True,
                    dest=port_cli,
                    type=str,
                    help='Root folder to grab dependencies recursively')

args = parser.parse_args()
print('Arguments:')
for arg in vars(args):
    print('  %s: %s' % (arg, getattr(args, arg)))

port = getattr(args, port_cli)


def ping_tor():
    current_port = port
    session.proxies['http'] = 'socks5://127.0.0.1:%s' % current_port
    session.proxies['https'] = 'socks5://127.0.0.1:%s' % current_port
    tor = session.get('https://ipinfo.tw/ip')
    if tor.text.strip() in ips:
        print(tor.text.strip() + " The same IP repeated twice, build is failing")
        exit(1)
    else:
        ips.append(tor.text.strip())
        session.close()
        print("My IP using Tor: " + tor.text)
        print("All Ips from Tor: ", ips)


# Function time.time returns the current time in seconds since 1st Jan 1970
time_to_start = time.time()
time_to_end = time.time() + 60 * 2
while time.time() < time_to_end:
    ping_tor()
    time.sleep(10.0 - ((time.time() - time_to_start) % 10.0))
