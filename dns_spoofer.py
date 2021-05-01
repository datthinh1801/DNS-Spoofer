#! /bin/python

from netfilterqueue import NetfilterQueue
import subprocess


def process_packet(packet):
    print(packet)
    packet.accept()


subprocess.call("sudo iptables -I FORWARD -j NFQUEUE --queue-num 0", shell=True)
try:
    queue = NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
except KeyboardInterrupt:
    subprocess.call("sudo iptables --flush", shell=True)
