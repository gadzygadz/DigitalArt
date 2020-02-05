import os 
from subprocess import call
from glob import glob

try:
    os.system("mkdir -p ~/.local/share/fonts")
except:
    print("Folder Already Generated")

all_files = glob(f'{os.getcwd()}/**/*', recursive=True)
for f in all_files:
    os.system(f"cp {f} ~/.local/share/fonts/")

os.system("fc-cache -f -v")