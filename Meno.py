import randomfrom random import randintimport stringimport uuidimport osimport time from time import sleepfrom colorama import Foreimport sys###########os.system("clear")print(Fore.BLUE+""" █████████ █▄█████▄█ CODID BY \033[93mSHah HunTer | MR HUNTER\033[93m █◇◇◇♡◇◇ CH.\33[1;0m https://rubika.ir/SHah_Officall\033[93m █ WE: http://crea-hunter.blogfa.com\33[1;0m █◇◇♡◇◇◇█████████ ██ ██""")soheil = """ \033[41m[1]\33[1;0m COOD GROP \033[41m[2]\33[1;0m COOD USER \033[41m[3]\33[1;0m COOD CHANEEL \033[41m[4]\33[1;0m Exit """for i in soheil:	sleep(0.05)	print(i,end='',flush=True)print()################ Inputsshah = int(input(Fore.CYAN+" \033[41m[?]\33[1;0m"+"\33[1;0m Open You NuMber >>> \033[93m"+Fore.RED+""))################################## Gropif(str(shah) == "1"): os.system("python G.py")############################### User if(str(shah) == "2"): os.system("python U.py") #COD Filteri Chanelif(str(shah) == "3"): os.system("python Ch.py")##########if(str(shah) == "4"): sys.exit()