import scapy.all as scapy
g = '\033[92m'  
y = "\033[93m"  
r = '\033[0m'   
c = '\033[36m'  

def arp(ip):
    
    broad = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    uzel = scapy.ARP(pdst=ip)
    packet = broad/uzel
    
    ans, unans = scapy.srp(packet, timeout=2, verbose=0)
    if ans:  
        print("\n" + "-" * 41)
        print(f"{g}{'IP Address':<24}{'MAC Address'}{r}")
        print("-" * 41)
        
        for _, received in ans:
            print(f"{received.psrc:<24}{received.hwsrc}")
        print("-" * 41)
    else:
        print(f"\n{y}[!]{r} Устройства не найдены.")
try:
    target = input(f"{c}[*]{r} Введите IP/CIDR: ")
    arp(target)
except KeyboardInterrupt:
    print(f"\n{y}[!]{r} Остановлено")
