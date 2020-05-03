# Imports the socket library for our scanning function
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Input Target IP Address to Scan: ")
port = int(input("Input Target Port to Scan: "))

# Function for port scanning
def portScanner(port):
    s.settimeout(int(input("How many seconds before timeout: ")))
    if s.connect_ex((host, port)):
        print("The Port is Closed")
    else:
        print("The Port is Open")

# Runs our portScanner function
portScanner(port)


