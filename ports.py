from socket import *
import time

# Scans for open ports on a target IP
# Works on localhost, not sure about external hosts
def port_scanner(target_IP):
    startTime = time.time()
    print('Starting scan on host: ', target_IP)

    # Scans ports in the given range
    for port in range (1, 65535):
        # Attempts to connect to port on the target IP
        if(is_port_open(target_IP, port)):
            print('Port %d: OPEN' % (port,))
    print('Time taken:', time.time() - startTime)

# Determine whether the port on the host is OPEN
def is_port_open(host, port):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((host, port))
    except:
        # Port is CLOSED, return false
        return False
    else:
        # Connection was established, port is OPEN
        return True

if __name__ == "__main__":
    port_scanner(gethostbyname('localhost'))
