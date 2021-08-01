from termcolor import colored # just for color
import requests # untuk send get request
import argparse
import threading

def banner(): # function for banner

    print(colored("""

        ░██████╗██████╗░░█████╗░  ███╗░░░███╗██╗░░░██╗
        ██╔════╝██╔══██╗██╔══██╗  ████╗░████║╚██╗░██╔╝
        ╚█████╗░██████╦╝██║░░╚═╝  ██╔████╔██║░╚████╔╝░
        ░╚═══██╗██╔══██╗██║░░██╗  ██║╚██╔╝██║░░╚██╔╝░░
        ██████╔╝██████╦╝╚█████╔╝  ██║░╚═╝░██║░░░██║░░░
        ╚═════╝░╚═════╝░░╚════╝░  ╚═╝░░░░░╚═╝░░░╚═╝░░░
        """, 'magenta'))


wordlist = open("wordlistSBC.txt","r") # buka wordlist

def find_admin(url): # function mencari
    for word in wordlist:
        word = word.strip()
        req = requests.get(url+"/"+word)
        if req.status_code == 200: # 200 means respond OK
            print(colored(req.url, 'green')) # return output

parser = argparse.ArgumentParser("""
cara guna : python3 admin.py -t [url]
contohnya : python3 admin.py -t http://testphp.vulnweb.com
""") # contoh yang x menjadi ;(

parser.add_argument("-t","--t") # -t untuk terget
args = parser.parse_args()
url = args.t

if url !=None:
    for x in range(60):
        i = threading.Thread(target=find_admin,args=(url,))
        i.start()

else:
    pass

banner()




