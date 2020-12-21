import requests,threading,os
from colorama import init, Fore, Back, Style
init(convert=True)
found = 0
notfound = 0
def checkuser(name,line):
    global found
    global notfound
    line = line.strip()
    line = line.split(',') 
    site = line[0]
    status = line[1]
    site = site.replace("username",name)
    print(f"{Fore.BLUE} > Checking {site}")
    checked = requests.get(site).status_code
    #print(f"{site} Returned status code {str(checked)} - Needed to be {status}")
    if checked == int(status):
        print(f"{Fore.GREEN} > {name} found on {site}!")
        try:
            f = open(f"{name}.txt", "a")
            f.write(f"{site} \n")
            f.close()
        except:
            pass
        found =+ 1
    else:
        print(f"{Fore.RED} > {name} not be found on {site}!")
        notfound =+ 1
    os.system(f"title Username Searcher - {name} found on {found} Sites, Not found on {notfound} sites")
os.system("title Please Enter The Username")
print(f"{Fore.CYAN} > Username To Search For?")
name = input(" > ")
print(f"{Fore.BLUE} > Searching...")
with open("sites.txt", 'r') as f:
    for line in f.readlines():
        threading.Thread(target = checkuser, args = (name,line,)).start()
