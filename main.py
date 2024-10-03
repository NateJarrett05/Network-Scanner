import scapy.all as scapy
from socket import *
import time
import arguments

# arguments.get_args()

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

port_scanner('localhost')
