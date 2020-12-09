def get_ips(ifconfig):
    '''
    This plugin will receive a ifconfig output command and return configured IPs
    '''
    import re

    final_output = re.findall('\\b(?:[0-9]{1,3}\\.){3}[0-9]{1,3}\\b', ifconfig)

    return final_output

def get_macs(ifconfig):
    '''
    This plugin will receive a ifconfig output command and return configured MACs
    '''
    import re

    final_output = re.findall('\\b(?:[0-9]{1,3}\\.){3}[0-9]{1,3}\\b', ifconfig)

    return final_output

class FilterModule(object):
    def filters(self):
        return {
            "get_ips": get_ips,
            "get_macs": get_macs
        }