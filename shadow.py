import os
def myshutdown(s): # type: ignore
    if s == 'no':
        exit()
    else:
    os.system("shutdown /s /t 1")
s = input("Do you wish to shut down your computer? (yes / no): ")
myshutdown(s)

