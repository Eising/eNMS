from collections import OrderedDict

napalm_dispatcher = {
                    # Ax: ASR1000, IOS XE
                    'BNET-A1': ('192.168.243.78', 'ios'),
                    'BNET-A2': ('192.168.243.79', 'ios'),
                    'BNET-A3': ('192.168.243.69', 'ios'),
                    'BNET-A4': ('192.168.243.135', 'ios'),
                    # # C10K, IOS
                    'BNET-E1': ('192.168.243.101', 'ios'),
                    'BNET-E2': ('192.168.243.102', 'ios'),
                    'BNET-E3': ('192.168.243.103', 'ios'),
                    'BNET-E4': ('192.168.243.104', 'ios'),
                    'BNET-E5': ('192.168.243.105', 'ios'),
                    'BNET-E6': ('192.168.243.106', 'ios'),
                    'BNET-E7': ('192.168.243.107', 'ios'),
                    # # C7600, IOS
                    'BNET-I1': ('192.168.243.108', 'ios'),
                    'BNET-I2': ('192.168.243.110', 'ios'),
                    'BNET-I3': ('192.168.243.115', 'ios'),
                    'BNET-I4': ('192.168.243.116', 'ios'),
                    'BNET-I5': ('192.168.243.119', 'ios'),
                    # Gx: GSR12K, IOS XR
                    'BNET-G1': ('192.168.243.21', 'ios-xr'),
                    'BNET-G2': ('192.168.243.22', 'ios-xr'),
                    # ASR9K, IOS XR 
                    'BNET-P1': ('192.168.243.23', 'ios-xr'),
                    # Juniper devices, Junos
                    'BNET-J1': ('192.168.243.77', 'junos'),
                    'BNET-J2': ('192.168.243.82', 'junos'),
                    'BNET-J3': ('192.168.243.83', 'junos'),
                    'BNET-J4': ('192.168.243.117', 'junos'),
                    'BNET-J5': ('192.168.243.118', 'junos'),
                    'BNET-J6': ('192.168.243.133', 'junos'),
                    # Cisco RR, ASK1K, IOS-XE
                    'BNET-R7': ('192.168.243.80', 'ios'),
                    # Cisco nexus
                    'BNET-N1': ('192.168.243.134', 'nx-os'),
                    }
                    
napalm_drivers = napalm_actions = OrderedDict([
('IOS', 'ios'),
('IOS-XR', 'iosxr'),
('NX-OS', 'nxos'),
('NX-OS SSH', 'nxos_ssh'),
('Junos', 'junos'),
('EOS', 'eos')
])

scheduler_choices = OrderedDict([
('', None),
('Every hour', 60*60),
('Once a day', 60*60*24),
('Once a week', 60*60*24*7),
('Once a month', 60*60*24*30),
])

def str_dict(input, depth=0):
    tab = '\t'*depth
    if isinstance(input, list):
        result = '\n'
        for element in input:
            result += '{}- {}\n'.format(tab, str_dict(element, depth + 1))
        return result
    elif isinstance(input, dict):
        result = ''
        for key, value in input.items():
            result += '\n{}{}: {}'.format(tab, key, str_dict(value, depth + 1))
        return result
    else:
        return str(input)
