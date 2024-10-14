import scapy.all as scapy
from socket import *
import time
import arguments

# arguments.get_args()

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

# Scans for open ports on a target IP
# Works on localhost, not sure about external hosts
def port_scanner(target):
    startTime = time.time()
    target_IP = gethostbyname(target)
    print('Starting scan on host: ', target_IP)

    # Scans ports between the range of 50 and 500
    for i in range (50, 500):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(3)
        # Attempts to connect to port i on the target IP
        connection = s.connect_ex((target_IP, i))

        if(connection == 0):
            print('Port %d: OPEN' % (i,))
        # Closes the socket
        s.close()
    print('Time taken:', time.time() - startTime)

device_scanner('192.168.1.1/24')
