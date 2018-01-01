from urllib.request import urlopen
from urllib.error import HTTPError
import time
#import sys
#argv = sys.argv[1]
#open_wl = open(argv,'r')
path = input("Wordlist: ")
url = input("Enter url: ")

open_wl = open(path, 'r')
dirs = open_wl.read().split("\n")
open_wl.close()
#print(dirs)
outFile = open(url+"_output.txt", 'a')


now = time.strftime("%c")
print(time.strftime("%c"))
outFile.write(now + "\n" + "-----------------" + "\n")
outFile.close()

for i in range(0, len(dirs)):
    u = ("http://"+url+ "/" + dirs[i])
    #print("http://"+url+ "/" + dirs[i])

    try:
        response = urlopen(u)
        result = response.getcode()
        if result == 200:
            print("[*]" + " " + str(result) + " - [OK]" + " => " +u)
            outFile = open(url + "_output.txt", 'a')
            outFile.writelines("[*]" + " " + str(result) + " - [OK]" + " => " +u)
            outFile.writelines("\n")
            outFile.close()
        #print(result)
    except HTTPError as err:
        if err.code == 401:
            print("[x]" + " " + str(err.code) + " - [Unauthorized]" + " => " + u)
        elif err.code == 403:
            print("[x]" + " " + str(err.code) + " - [Forbidden]" + " => " + u)
        elif err.code == 404:
            print("[x]" + " " + str(err.code) + " - [Not Found]" + " => " + u)
        elif err.code == 503:
            print("[x]" + " " + str(err.code) + " - [Service Unavailable]" + " => " + u)
        else:
            print("N/A !")




