import sys
import shutil
import os
from os.path import exists

def checkup():
    cwd = os.getcwd()
    arg = sys.argv[1]
    par = cwd+"/"+arg

#PLACEHOLDER
    dst = cwd+"/dst"

    print(par)

    if os.path.exists(par):
        print("All correct")
    #Placeholder
        shutil.copy(par, dst)
    else:
        print("Mistakes have been made")
    #Placeholder


