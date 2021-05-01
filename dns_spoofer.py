#! /bin/python

from NetfilterQueue import NetfilterQueue
import subprocess


def process_packet(packet):
    print(packet)
    packet.accept()


subprocess.run("sudo iptables -I FORWARD -j NFQUEUE --queue-num 0")
try:
    queue = NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
except KeyboardInterrupt:
    subprocess.run("sudo iptables --flush")
