import os 
from subprocess import call
from glob import glob
import platform

if platform.system() == "Linux":
    try:
        os.system("mkdir -p ~/.local/share/fonts")
    except:
        print("Folder Already Generated")

    all_files = glob(f'{os.getcwd()}/**/*', recursive=True)

    for f in all_files:
        os.system(f"cp {f} ~/.local/share/fonts/")

    os.system("fc-cache -f -v")
else:
    print("Sorry This only works on linux machines :(")