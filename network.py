import socket
import os
import platform

def get_ip():
    name = socket.gethostname()
    ip = socket.gethostbyname(name)
    print("IP:", ip)

def check_port(host, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        result = s.connect_ex((host, port))
        s.close()
        return result == 0
    except:
        return False

def scan_ports(host, start, end):
    for p in range(start, end + 1):
        if check_port(host, p):
            print("port", p, "open")
        else:
            print("port", p, "closed")

def network_check():
    print("ARP table (devices on network?)")
    if platform.system() == "Windows":
        os.system("arp -a")
    else:
        os.system("arp")

    print("\npinging google (8.8.8.8)...")
    if platform.system() == "Windows":
        result = os.system("ping 8.8.8.8")
    else:
        result = os.system("ping -c 4 8.8.8.8")

    if result == 0:
        print("internet’s working")
    else:
        print("no internet?")

def search_files(name, path):
    print("searching for", name, "in", path)
    for root, dirs, files in os.walk(path):
        for f in files:
            if name.lower() in f.lower():
                print("found:", os.path.join(root, f))

while True:
    print("\nMenu:")
    print("A - show IP")
    print("B - scan ports")
    print("C - network monitoring")
    print("D - find a file")
    print("Q - quit")

    choice = input("Pick something (A/B/C/D/Q): ").strip().upper()

    if choice == "A":
        get_ip()
    elif choice == "B":
        h = input("host (blank = localhost): ")
        if h == "":
            h = "localhost"
        try:
            s = int(input("start port: ")) #netstat -an
            e = int(input("end port: "))
            scan_ports(h, s, e)
        except:
            print("bad port numbers error")
    elif choice == "C":
        network_check()
    elif choice == "D":
        f = input("file name: ")
        p = input("folder to search (blank = C:/ or /): ")
        if p == "":
            p = "C:\\" if platform.system() == "Windows" else "/"
        search_files(f, p)
    elif choice == "Q":
        print("bye")
        break
    else:
        print("??? not an option")
