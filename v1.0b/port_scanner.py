'''
* Developed by terabyte_data@ChilusoftCorp
* Port scanner program for TCP and UDP using the native Socket module
* written in python
'''
import subprocess,sys,socket
from datetime import datetime
from sys import platform
import time
#clean up the mess on the screen, code differs with platform

if platform == "linux" or platform == "linux2" or platform == "darwin":
    # linux
    subprocess.call("clear",shell=True)

elif platform == "win32":
    # Windows...
    subprocess.call('cls',shell=True)



#data from the user

serverUrl = raw_input("Enter the server address to scan : ")
serverIP = socket.gethostbyname(serverUrl)


#display some data

print "*" * 40
print "initiating port scanner engine"
time.sleep(1)
print "Please wait while scanning ", serverUrl, " at ", serverIP
t1 = datetime.now()

#port range to scan

try:
    for port in range(1,1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((serverIP,port))
        if result == 0:
            print "Port {}:   Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    print "Exiting in 3 seconds"
    time.sleep(3)
    sys.exit()

except socket.gaierror:
    print "hostnme could not be resolved.. "
    print "Exiting in 3 seconds"
    time.sleep(3)
    sys.exit()

except socket.error:
    print "Couldnt connect to server {} at port {}".format(serverUrl,port)
    print "Exiting in 3 seconds"
    sys.exit()

t2 = datetime.now()

t = t2-t1
    
print "Scanning completed : timeout",t    




