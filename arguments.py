import argparse

def get_args():
    parser = argparse.ArgumentParser(
        prog = "Network Scanner",
        description = "A program to scan for IP(s) on a network."
    )

    parser.add_argument('-t', '--target', dest='target', help='Target IP Address/Adresses')
    parser.add_argument('-n', '--name', dest='name', help='Target a given hostname')
    options = parser.parse_args()

    # Check for errors I.E. if the user does not specify a target IP address
    if not options.target:
        parser.error("[-] Please specify an IP Address or Addresses, use --help for more info.")

    return options
