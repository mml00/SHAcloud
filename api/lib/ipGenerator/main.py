def generateIPList(ipRange: list[str]) -> list[str]:
    """Generates list of ip from nmap-like list of strings ["xxx-yyy.zzz-aaa.bbb-ccc.ddd-fff", ...]
       Example:
       [
        '192.168.1.1-2',
        '192-193.1.1
       ] => [
        '192.168.1.1'
        '192.168.1.2'
        '192.168.1.1'
        '193.168.1.1'
       ]
    """

    if type(ipRange) is not list:
        raise TypeError("ipRange must be list")

    ipList = list()

    for netRange in ipRange:

        if type(netRange) is not str:
            raise TypeError("type of ipRange items must be str")

        ipCandidates = list()

        octets = netRange.split(".")


        # Recursive func
        def generateIpFromOctets(currentIp: str = "", depth: int = 0):
            if depth <= 3:
                # "xxx-yyy" (taken from octets list with depth as index) -> ["xxx", "yyy"]
                octetRange = octets[depth].split("-")
                dotDelimiter = "" if depth == 0 else "."

                if len(octetRange) > 1:
                    # Defining range min, max
                    netStart, netEnd = sorted(list(map(int, octetRange)))

                    for i in range(netStart, netEnd + 1):
                        generateIpFromOctets("{}{}{}".format(currentIp, dotDelimiter, i), depth + 1)

                else:
                    generateIpFromOctets("{}{}{}".format(currentIp, dotDelimiter, octetRange[0]), depth + 1)

            else:
                if currentIp not in ipList and currentIp not in ipCandidates:
                    ipCandidates.append(currentIp)


        generateIpFromOctets()
        ipList += ipCandidates

    return ipList

