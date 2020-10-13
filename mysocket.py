import socket
import sys
import os
from datetime import datetime

# links
t = 'https://t.me/Liffhy32'
tc = 'https://t.me/LiffhyWTF'
# Os color
os.system('color 3')

# Ask information for the scan

username = input("Please provide your username: ")
print("This a simple port scan for check if are safe by Liffhy")

# Print the information need
os.system('color 4')
os.system('cls' if os.name == 'nt' else 'clear')

print("-" * 60)

print("Your username: ", username)
print("Scanner create by Liffhy32")
print("Time: ", datetime.now())
print("My Telegram: ", t)

print("-" * 60)

# Ge the ip for start the port scan

IpHOST = input("Please provide the host to scan (ex. mc.hypixel.com or 64.89.125.14):  ")
serverIP = socket.gethostbyname(IpHOST)
socket.getaddrinfo('localhost', 8080)

# Information to say the scanning start

print("-" * 60)

print("Username: ", username)
print("Scanner create by Liffhy32")
print("Time: ", datetime.now())
print("My telegram", t)
print("[SCANNER] Please wait, i'm scanning the host: ", serverIP)

print("-" * 60)
try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((serverIP, port))
        if result == 0:
            print("[HOST]", IpHOST, "[PORT] {}: 	OPEN".format(port))
        sock.close()
except socket.error:
    print("[ERROR] I can't connect to the server! Please try another host ")
    sys.exit()
except KeyboardInterrupt:
    print("[SCANNER] You pressed Ctrl+C, the scan will be stopped!")
    sys.exit()
