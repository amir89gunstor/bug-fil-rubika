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
print(Fore.RED+"    "+" Loading....")
sleep(2.0)
os.system("clear")
print("\n")
print(Fore.GREEN+"""
     Loading Conected Server ... 
  """)
sleep(2.0)
print("\n"*49)
Sdf = """
    update Cod ......
    
    
    
    
    Checking availability of current mirror: bad
    Testing the available mirrors:
    [*] https://dl.bintray.com/termux/termux-packages-24: bad
    [*] https://grimler.se/termux-packages-24: bad
    [*] https://main.termux-mirror.ml: bad
    [*] https://termux.mentality.rip/termux-packages-24: bad
‌‌
    Using fallback mirror: https://termux.org/packages
    Reading package lists... Done
    Building dependency tree
    Reading state information... Done
    Filtering User is already the newest version (2.2.5-2).
    0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
"""
for i in Sdf:
  sleep(0.02)
  print(i,end='',flush=True)
print()
print(Fore.RED+"    Crea cod Loafing ....")
sleep(2.1)
print()
def random_string_genera_variable_size(min_size, max_size, allowed_chars):
  return ''.join(random.choice(allowed_chars) for x in range(randint(min_size, max_size)))
chars = string.ascii_letters + string.punctuation
print(Fore.GREEN+"    "+"|"+"-"*50+"|")
print("     "+Fore.YELLOW+'COOD Filteri User id ★★★★★★★ >>> ', random_string_genera_variable_size(6, 12, chars))
print(Fore.GREEN+"    "+"|"+"-"*50+"|")
print()
sleep(1.0)
print(Fore.GREEN+"""
    CODID BY SHaH HuNTer 
     """)
input()
os.system("python Meno.py")
