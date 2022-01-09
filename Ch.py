import random
from random import randint
import string
import uuid
import os
import time 
from time import sleep
from colorama import Fore
import sys
print("")
print(Fore.GREEN+"    "+" Loading....")
sleep(2.0)
os.system("clear")
print("\n")
print(Fore.GREEN+"""
     Loading Conected Server ... 
  """)
sleep(2.0)
print("\n"*49)
print("""
  Conected Servers :/
  """)
Dmo = """
  May 26 22:10:07.000 [notice] Parsing GEOIP IPv6 file /data/data/com.termux/files/usr/share//geoip6.                                                            May 26 22:10:07.000 [notice] Bootstrapped 0% (starting): Starting
  May 26 22:10:08.000 [notice] Starting with guard context "default"
  May 26 22:10:09.000 [warn] Problem bootstrapping. Stuck at 0% (starting): Starting. (Network is unreachable; NOROUTE; count 1; recommendation warn; host 4623A9EC53BFD83155929E56D6F7B55B5E718C24 at 163.172.157.213:443)
  May 26 22:10:10.000 [warn] Problem bootstrapping. Stuck at 0% (starting): Starting. (Network is unreachable; NOROUTE; count 2; recommendation warn; host AD86CD1A49573D52A7B6F4A35750F161AAD89C88 at 176.10.104.240:8443)
  May 26 22:10:12.000 [warn] Problem bootstrapping. Stuck at 0% (starting): Starting. (Network is unreachable; NOROUTE; count 3; recommendation warn; host 1CD17CB202063C51C7DAD3BACEF87ECE81C2350F at 50.7.74.171:9001)                             May 26 22:10:15.000 [warn] Problem bootstrapping. Stuck at 0% (starting): Starting. (Network is unreachable; NOROUTE; count 4; recommendation warn; host BD6A829255CB08E66FBE7D3748363586E46B3810 at 171.25.193.9:80)
  May 26 22:10:16.000 [warn] Problem bootstrapping. Stuck at 0% (starting): Starting. (Network is unreachable; NOROUTE; count 5; recommendation warn; host ED2338CAC2711B3E331392E1ED2831219B794024 at 192.87.28.28:9001)
  May 26 22:10:21.000 [warn] Problem bootstrapping. Stuck at 0% (starting): Starting. (Network is unreachable; NOROUTE; count 6; recommendation warn; host FFA72BD683BC2FCF988356E6BEC1E490F313FB07 at 193.11.164.243:9001)
  May 26 22:10:21.000 [warn] Problem bootstrapping. Stuck at 0% (starting): Starting. (Network is unreachable; NOROUTE; count 7; recommendation warn; host 24E2F139121D4394C54B5BCC368B3B411857C413 at 204.13.164.118:443)
  May 26 22:10:23.000 [notice] Interrupt: exiting cleanly.
  
"""
for i in Dmo:
  sleep(0.02)
  print(i,end='',flush=True)
print()
print(Fore.RED+"    CreaTor cod Loafing ....")
sleep(2.1)
def random_string_generator(str_size, allowed_chars):
  return ''.join(random.choice(allowed_chars) for x in range(str_size))
chars = string.ascii_letters + string.punctuation
size = 28
print(Fore.BLUE+"    "+"|"+"-"*50+"|")
print(Fore.RED+'   COOD Filteri CHANELL >> ',random_string_generator(size, chars))
print(Fore.BLUE+"    "+"|"+"-"*50+"|")
input()
os.system("python Meno.py")
