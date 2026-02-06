from scapy.all import *

packets = rdpcap("capture.pcap")

for i, pkt in enumerate(packets):
    print("\nPacket:", i+1)

    if IP in pkt:
        print("IP checksum:", pkt[IP].chksum)

    if TCP in pkt:
        print("TCP checksum:", pkt[TCP].chksum)

    if UDP in pkt:
        print("UDP checksum:", pkt[UDP].chksum)

    if ICMP in pkt:
        print("ICMP checksum:", pkt[ICMP].chksum)
