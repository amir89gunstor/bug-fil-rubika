import random
from random import randint
import string
import uuid
import os
import time 
from time import sleep
from colorama import Fore
import sys
###########
os.system("clear")
print(Fore.BLUE+"""
     ███
      ██
        █
    █
     █     █
          █   CODID BY \033[93mamir serkhio | MR serkhio\033[93m  
       CH.\33[1;0m https://rubika.ir/manam_miram\033[93m
soheil = """
     \033[41m[1]\33[1;0m COOD GROP
     \033[41m[2]\33[1;0m COOD USER
     \033[41m[3]\33[1;0m COOD CHANEEL
     \033[41m[4]\33[1;0m Exit 
"""
for i in soheil:
	sleep(0.05)
	print(i,end='',flush=True)
print()
################   Inputs
shah = int(input(Fore.CYAN+"     \033[41m[?]\33[1;0m"+"\33[1;0m Open You NuMber >>> \033[93m"+Fore.RED+""))
################################## Grop
if(str(shah) == "1"):
  os.system("python G.py")
###############################     User 
if(str(shah) == "2"):
  os.system("python U.py")
  #COD Filteri Chanel
if(str(shah) == "3"):
  os.system("python Ch.py")
##########
if(str(shah) == "4"):
  sys.exit()
