import scapy.all as scapy
g='\033[92m'
y="\033[93m"
r='\033[0m'
c='\033[36m'
try:
    target=input(f"{c}[*]{r} Введите IP/CIDR:")

    def arp(ip):
        broad=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        uzel=scapy.ARP(pdst=ip)
        packet=broad/uzel
        ans,i=scapy.srp(packet,timeout=2,verbose=0)
        if ans:
            for _,received in ans:
                print(f"{g}[+]{r} ip:{received.psrc} mac:{received.hwsrc}")
    arp(target)
except KeyboardInterrupt:
    print(f"\n{y}[!]{r} Остановлено ")
