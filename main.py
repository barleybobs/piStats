from termcolor import colored
from graphics import *
from defines import *
from pathlib import Path
from hurry.filesize import *
import datetime, time, os, socket
import psutil
import json
import urllib.request as urllib2 

global piHoleLogo
global sambaLogo

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = str(s.getsockname()[0])

slide_change_time = 5

version = '1'#parsed_json['version']

drives = []

port = 445
timeout = 0.5
samaba_folder = Path('/share')

while True:
  f = urllib2.urlopen('http://' + str(ip) + '/admin/api.php')
  json_string = f.read()
  parsed_json = json.loads(json_string)

  if parsed_json['status'] == 'enabled':
    status = True
  else:
    status = False

  number_of_clients = parsed_json['unique_clients']
  dns_queries_today = parsed_json['dns_queries_today']

  domains_being_blocked = parsed_json['domains_being_blocked']
  ads_blocked_today = parsed_json['ads_blocked_today']
  ads_percentage_today = parsed_json['ads_percentage_today']
  
  print(piHoleLogo, end=" ")
  print('v' + str(version))
  #Pi-Hole title
  print('\n\033[1mPI-HOLE\033[0m')
  #Pi-Hole status
  print(' Status: ' + (colored('Enabled', 'green') if status else
                      (colored('Disabled', 'red'))))
  #Pi-Hole stats title
  print('\033[1mSTATS \033[0m')
  #Amount of servers on block list
  print(' Blocking: ' + str(format(domains_being_blocked, ',')))
  #Percent of dns queries blocked out of total dns queries
  print(' Pi-Holed: ', end="")
  percent(ads_percentage_today, 40, u'\u200b', 'green', 'red', '\n')
  #Amount of dns queries blocked out of total dns queries
  print(' Pi-Holed: ' + str(format(ads_blocked_today, ',')) + ' out of ' +
        str(format(dns_queries_today, ',')) + ' queries')
  #Network title
  print('\033[1mNETWORK\033[0m')
  #Machine hostname and Ip
  print(' Hostname: ' + socket.gethostname() + '\033[1m | \033[0m' + 'IP: ' + ip)
  #Connection type
  print(' Conection Type: ' + 'Wired' if connectionType() == True else ' Conection Type: ' + 'Wireless')
  #Pi-Hole connected clients
  print(' Connected Clients: ' + str(number_of_clients))
  #System title
  print('\033[1mSYSTEM\033[0m')
  #Machine uptime
  print(' Uptime:   ' +
        str(datetime.timedelta(seconds=round(time.time() - psutil.boot_time()))))
  #CPU usage
  print(' CPU:      ' + str(psutil.cpu_percent(interval=1)) + '%')
  #Memory usage
  print(' Memory:   ', end="")
  percent(psutil.virtual_memory().percent, 10, u'\u200b', 'green', 'red', '')
  #Machine drives     
  print(' Drives:   ' + listDrives())

  time.sleep(slide_change_time)
  os.system('cls' if os.name=='nt' else 'clear')

  print(sambaLogo, end=" ")
  #SMB title
  print('\n\033[1mSMB\033[0m')
  #SMB status
  print(' Status: ' + (colored('Enabled', 'green') if isOpen(ip, port, timeout) else (colored('Disabled', 'red'))))
  #SMB storage used
  print(' Storage Used: ' + size(sum(f.stat().st_size for f in samaba_folder.glob('**/*') if f.is_file()),system=alternative))
  #SMB folder location
  print(' Folder: ' + str(Path.cwd() / samaba_folder))
  #Network title
  print('\033[1mNETWORK\033[0m')
  #Machine hostname and Ip
  print(' Hostname: ' + socket.gethostname() + '\033[1m | \033[0m' + 'IP: ' + ip)
  #Connection type
  print(' Conection Type: ' + 'Wired' if connectionType() == True else ' Conection Type: ' + 'Wireless')
  #Sytem title
  print('\033[1mSYSTEM\033[0m')
  #Machine Uptime
  print(' Uptime:   ' +
        str(datetime.timedelta(seconds=round(time.time() - psutil.boot_time()))))
  #CPU usage
  print(' CPU:      ' + str(psutil.cpu_percent(interval=1)) + '%')
  #Memory usage
  print(' Memory:   ', end="")
  percent(psutil.virtual_memory().percent, 10, u'\u200b', 'green', 'red', '')
  #Machine drives
  print(' Drives:   ' + listDrives())

  time.sleep(slide_change_time)
  os.system('cls' if os.name=='nt' else 'clear')


#root_directory = Path('./test')
#print(size(sum(f.stat().st_size for f in root_directory.glob('**/*') if #f.is_file()),system=alternative))

#print(' Used RAM: ' + str(round(psutil.virtual_memory().used/1073741824, 2)) + 'gb/' + str(round(psutil.virtual_memory().total/1073741824, 2)) + 'gb')

#print(sambaLogo, end=" ")
