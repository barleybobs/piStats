from termcolor import colored

piHoleLogo = """ ____  _       _   _       _      
|  _ \(_)     | | | | ___ | | ___ 
| |_) | |_____| |_| |/ _ \| |/ _ \\
|  __/| |_____|  _  | (_) | |  __/
|_|   |_|     |_| |_|\___/|_|\___|"""

sambaLogo = """ ____                  _           
/ ___|  __ _ _ __ ___ | |__   __ _ 
\___ \ / _` | '_ ` _ \| '_ \ / _` |
___) | (_| | | | | | | |_) | (_| |
|____/ \__,_|_| |_| |_|_.__/ \__,_|
"""

def percent(percent, boxes, spaces, background_color, bar_color, end):
  percent_for_bar = round((int(percent)/10)*(boxes/10))
  print('\033[1m[\033[0m', end="")
  for x in range(boxes):
    if x == percent_for_bar or x > percent_for_bar:
      print(colored('■' + spaces, background_color), end="")
    else:
      print(colored('■' + spaces, bar_color), end="")
  print('\033[1m]' + ' ', end="")
  print(str(percent) + '%\033[0m', end=end)