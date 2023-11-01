import os
import shutil
from pathlib import Path


img  = (".img", ".gif", ".jpeg", ".png", ".jpg")

def is_img(file):
    return os.path.splitext(file)[1] in img

os.chdir(r'\Users\Julia\Downloads\im')

for i in os.listdir():
    if is_img:
        shutil.move(r'\Users\Julia\Downloads',  r'\Users\Julia\Downloads\im\data')