import os
import sys
import time
import subprocess
try:
    from colorama import Fore
except:
    time.sleep(1)
    print("[-] Pleass Install The Librery --> colorama")
    sys.exit()
from baner import baner
baner()
time.sleep(1)
print(Fore.LIGHTBLACK_EX + "        \t\t    [1] ~ MAC Changer")
print(Fore.LIGHTBLACK_EX + "        \t\t    [2] ~ Scanner Network")
print(Fore.LIGHTBLACK_EX + "        \t\t    [3] ~ ARP Spoofer")
print(Fore.LIGHTBLACK_EX + "        \t\t    [4] ~ Internet Diseconnection For Target")
try:
  number = int(input(Fore.CYAN + "\n\t\t\t        Your Number " + Fore.GREEN + ">>>" + Fore.BLUE + " "))
except:
  time.sleep(1)
  print(Fore.RED + "[-] Your Input Is Not Found !!!")
  sys.exit()
if number == 1:
  import mac_changer
  mac-changer.mac_changer()
if number == 2:
  import scanner_network
  scanner_network.scanner_network()
if number == 3:
  import arp_spoofer
  arp_spoofer.arp_spoofer()
if number == 4:
  import internet_diseconnection
  internet_diseconnection.internet_diseconnection()
else:
  time.sleep(1)
  print(Fore.RED + "[-] Your Numbrt Is Not Found !!!")
  sys.exit()
