import requests
from requests.auth import HTTPDigestAuth

from lib.ipGenerator import generateIPList

IP_RANGES = [
    '192.168.1.1-3',
    '192.168.1.6-8',
]

def changePassword(ip: str = "",):
    url="http://{}/cgi-bin/changepassword.cgi&".format(ip)
    r = requests.get(url, auth=HTTPDigestAuth('myUsername', 'myPassword'),
                 timeout=10)
    print(url)

def multipleChangePassword(ipRanges: list[str]) -> bool:
    ipList = generateIPList(ipRanges)

    for ip in IP_LIST:
        changePassword(ip)

if __name__ == '__main__':
    multipleChangePassword(IP_RANGES)
