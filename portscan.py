import socket

# Function to perform a port scan on a target
def scan(target, ports):
    print("\n" + " Starting Scan For " + str(target))
    # Loop through each port in the range from 1 to the specified number of ports
    for port in range(1, ports):
        # Call scan_port function to check if the port is open
        scan_port(target, port)

# Function to scan a specific port on a target IP address
def scan_port(ipaddr, port):
    try:
        # Create a socket object
        sck = socket.socket()
        # Attempt to connect to the target IP address and port
        sck.connect((ipaddr, port))
        # If connection is successful, print that the port is open
        print("[+] Port Opened " + str(port))
        # Close the socket
        sck.close()
    except:
        # If connection fails (e.g., port is closed), continue to the next port
        pass

# Prompt the user to enter the target(s) to scan
targets = input("[*] Enter Target To Scan: ")
# Prompt the user to enter the number of ports to scan
ports = int(input("[*] Enter How many ports you want to Scan: "))

# Check if the user entered multiple targets separated by commas
if ',' in targets:
    print("[*] Scanning multiple targets")
    # Split the targets string into a list of individual targets
    for ip_addr in targets.split(','):
        # Remove any leading or trailing spaces from the target IP address
        scan(ip_addr.strip(' '), ports)
else:
    # If only one target is provided, directly call the scan function
    scan(targets, ports)
