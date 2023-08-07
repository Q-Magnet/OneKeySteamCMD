import requests as r
import os
import sys
from time import sleep
    
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
    print('Retrieving file in ' + scmd_link1)
    Download(scmd_link1, 'SteamCMD.zip')
    os.system(f'cd {__file__} & unzip.exe SteamCMD.zip & md steamcmd & move steamcmd.exe {_path} & del steamcmd.zip')
    os.system('cls')
    
    
# Detect is SteamCMD Downloaded
print(_path)
if os.path.exists(_path+'\\SteamCMD.EXE'):
    print('SteamCMD is installed in ' + _path)
    sys.exit()
else:
    print('SteamCMD is not in ' + _path)
print('Getting SteamCMD' + _path)
GetSCMD()
os.system('cls')
print('SteamCMD Downloaded')
print('We are now going to update SteamCMD\nDo not terminate this update job\nStop Steam++ or Watt Toolkit first in order to download\n\nAfter the update is finished, you will be in the steamcmd prompt')
sleep(5)
input('Press Enter to Continue')
print(_path+'\\steamcmd.exe')
os.system(_path+'\\steamcmd.exe')
