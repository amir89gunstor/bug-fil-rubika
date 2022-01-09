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
sleep(1.0)
os.system("clear")
print("\n"*49)
loo = """
  Opening socket...
  Crea Codd .....
  Testing the available mirrors:
  [*] https://dl.bintray.com/termux/termux-packages-24: bad
  [*] https://grimler.se/termux-packages-24: bad
  [*] https://main.termux-mirror.ml: bad
  [*] https://termux.mentality.rip/termux-packages-24: bad
  Using fallback mirror: https://termux.org/packages
  Err:1 https://dl.bintray.com/grimler/game-packages-24 games InRelease
  Could not resolve host: dl.bintray.com
  Err:2 https://dl.bintray.com/grimler/science-packages-24 science InRelease
  Could not resolve host: dl.bintray.com                                                        Err:3 https://termux.org/packages stable InRelease
  Could not resolve host: termux.org
  Reading package lists... Done
  Building dependency tree
  Reading state information... Done
  All packages are up to date.
  W: Failed to fetch https://termux.org/packages/dists/stable/InRelease  Could not resolve host: termux.org
  W: Failed to fetch https://dl.bintray.com/grimler/game-packages-24/dists/games/InRelease  Could not resolve host: dl.bintray.com
  W: Failed to fetch https://dl.bintray.com/grimler/science-packages-24/dists/science/InRelease  Could not resolve host: dl.bintray.com
  W: Some index files failed to download. They have been ignored, or old ones used instead.
  Reading package lists... Done
  Building dependency tree
  Reading state information... Done
  Filterings is already the newest version (0.5.3.20190105-6).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
\033[93m Crea..: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.HTTPSConnection object at 0x76a5ddc670>: Failed to establish a new connection: [Errno 7] No address associated with hostname')': /simple/Filterings/ \33[1;0m
  """
for i in loo:
  sleep(0.02)
  print(i,end='',flush=True)
print()
sleep(0.9)
print(Fore.GREEN+"  "+"|"+"-"*40+"|")
print("   "+Fore.YELLOW+'COOD Filteri Grop (★★★)>> ',uuid.uuid1())
print("   "+Fore.YELLOW+'COOD Filteri Grop (★★★★★★★)>> ',uuid.uuid4())
print(Fore.GREEN+"  "+"|"+"-"*40+"|")
print()
input()
os.system("python Meno.py")
