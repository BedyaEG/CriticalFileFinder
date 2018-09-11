import requests
import time
import sys
import getpass
if sys.version > '3':
    pass
else:
    time.sleep(2)
    print("You Running At Python 2 \n [+] Run python3 Directory_Searhcer.py [+]")
    exit()
def chk_internet():
	try:
		url = 'https://start.parrotsec.org/'
		req = requests.get(url)
		http = req.content
		if b'IP' in http:
			pass
		else:
			print("No Internet Connection,Connect To Network Then Try Again Later")
			exit()
	except requests.exceptions.ConnectionError as e:
		print("You're Not Connected To Any Network\nConnect To Network Then Try Again")
		exit()
		
chk_internet()

Detect_user = getpass.getuser()
print("Hello "+Detect_user.upper())
from cores import banner
print("File Scanner Has Been Started Please Wait.. \n");time.sleep(2)

print("""


	Welcome To Critical File Finder Version : 1.0

    		Choose A Number From Below : 

    		[1]==> Tool Info And How it Works.

    		[2]==> Enter The File Critical Finder (Default).

    		[3]==> Enter The File Critical Finder (Custom).

    		[4]==> About The Tool.

    		[5]==> Exit.
""")

user_input = input("Choose A Choice >> ")
if user_input == "1":
	from cores import Tool_Info
elif user_input== "2":
	from cores import Attacker
elif user_input=="3":
	from cores import Attacker_Custom
elif user_input=="4":
	print("Copyright To BedyaEG \n Use At Your Own Risk")
elif user_input=="5":
	exit()




