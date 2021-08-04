def scanner_network():
    try:
        import os
        import time
        import sys
        import subprocess
        from baner import baner
        try:
            from scapy.layers.l2 import ARP , Ether
            from scapy.sendrecv import send , srp
        except:
            time.sleep(1)
            print("[-] Pleass Install The Librery --> scapy")
            sys.exit()
        try:
            from colorama import Fore
        except:
            time.sleep(1)
            print("[-] Pleass Install The Librery --> colorama")
            sys.exit()
        from baner import baner
        import platform
        name_os = platform.system()
        if name_os == "Linux":
            pass
        else:
            time.sleep(1)
            print(Fore.RED + "[-] Your System Not Linux !!!")
            sys.exit()
        baner()
        time.sleep(1)
        ip_target = input(Fore.BLUE + "[!]" + Fore.YELLOW + " ~ " + Fore.BLUE + "Enter Your Ip Target :" + Fore.YELLOW + " ")
        if ip_target == "" or None:
            time.sleep(1)
            print(Fore.RED + "[-] Your Input Is Not Found !!!")
            sys.exit()
        else:
            count = 0
            for i in ip_target:
                if i == ".":
                    count += 1
                else:
                    pass
            if count == 3 :
                pass
            else:
                time.sleep(1)
                print(Fore.RED + "[-] Your Ip Target Is Not Found !!!")
                sys.exit()
        arp_requests = ARP(pdst=ip_target)
        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        broadcast_arp_requests = broadcast / arp_requests
        a = srp(broadcast_arp_requests , time=2 , verbose=False)[0]
        clint_list = []
        for i in a:
            clint_dict = {"ip" : i[1].psrc , "mac" : i[1].hwsrc}
            clint_list.append(clint_dict)
        print("Ip ------------------------------ MAC Address")
        count1 = 1
        for item in clint_list:
            print( f"[{str(count1)}]"  + item["ip"] + " --------------------" + item["mac"])
            count1 += 1
    except KeyboardInterrupt:
        time.sleep(1)
        print(Fore.YELLOW + "\n\n[!] Ok Good Lunch :)))")
        sys.exit()
