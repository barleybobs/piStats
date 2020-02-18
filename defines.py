import socket
import os

def isOpen(ip,port,timeout):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.settimeout(timeout)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False

def connectionType():
  if 'wired' in str(os.popen("ip route get 8.8.8.8 | grep -Po 'dev \K\w+' | grep -qFf - /proc/net/wireless &&echo wireless || echo wired").read()):
    return True
  else:
    return False

def listDrives():
  drives = []
  for i in range(len(os.popen('df -k /').read().split('\n'))-2):
    drives.append(os.popen('df -k /').read().split('\n')[i+1].split(' ')[0])
  for i in range(len(drives)):
    if len(drives) != 1:
      return (drives[i] + ', ' if i != len(drives)-2 else drives[i]) if i != len(drives)-1 else ' and ' + drives[i] + '\n'
    else: 
      return drives[0]