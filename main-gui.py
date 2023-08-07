import requests as r
import os
import sys
from time import sleep
from tkinter import messagebox as msgbox
    
_path = os.path.dirname(__file__) + '\\steamcmd'
scmd_link1 = "https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip"
dl = []


def Download(LNK, Filename='Test.zip'):
    try:
        global dl
        dl = r.get(LNK)
        with open(Filename, 'wb') as f:
            f.write(dl.content)
        return dl
    except:
        return False
def GetSCMD():
    Download(scmd_link1, 'SteamCMD.zip')
    os.system(f'cd {__file__} & unzip.exe SteamCMD.zip & md steamcmd & move steamcmd.exe {_path} & del steamcmd.zip')
    os.system('cls')
    
    
# Detect is SteamCMD Downloaded
if os.path.exists(_path+'\\SteamCMD.EXE'):
    msgbox.showerror('OneKeySteamCMD', 'SteamCMD is installed in ' + _path)
    sys.exit()
else:
    if msgbox.askquestion('OneKeySteamCMD', 'SteamCMD is not in ' + _path + '\nGetting SteamCMD') == 'no':
        sys.exit()
GetSCMD()
os.system('cls')
msgbox.showinfo('OneKeySteamCMD', 'SteamCMD is in ' + _path + '\nWe are now going to update SteamCMD\nDo not terminate this update job\nStop Steam++ or Watt Toolkit first in order to download\n\nAfter the update is finished, you will be in the steamcmd prompt')
os.system(_path+'\\steamcmd.exe')
