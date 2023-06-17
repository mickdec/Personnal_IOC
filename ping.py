import os

f = open("README.md", "r")
ct = f.readlines()
f.close()
print("Your VPN is enabled ?")
input()
for ioc in ct:
    if "#" not in ioc:
        ioc = ioc.replace("<br>", "").replace("\n", "")
        print("Test on >> " + ioc)
        os.system("nmap -v -p- --open "+ioc +
                  " -oX nmap-result/"+ioc+".xml --unprivileged")
