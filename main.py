import scapy.all as scapy
import arguments

# TO BE IMPLEMENTED:
'''
Command line argument for providing a hostname instead of an IP
arguments.get_args()
-n
target_IP = gethostbyname(target)
'''
# Retrieves IP and MAC address pairs for devices on a target IP
def device_scanner(target):
    # IP address for the destination
    target_IP = target
    # target_IP = gethostbyname(target)
    print('Starting scan on host: ', target_IP)
    # Create ARP packet
    arp = scapy.ARP(pdst = target_IP)
    # Create the Ether broadcast packet
    # ff:ff:ff:ff:ff:ff MAC Address indicates broadcasting
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # Stack the packets
    packet = ether/arp

    result = scapy.srp(packet, timeout=5)[0]

    # List of clients
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    print("Available devices in the network:")
    print("IP" + " "*18+"MAC")
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))

#device_scanner('192.168.1.1/24')
