import sys, os, shutil, tempfile
from PIL import Image
import img2pdf

def has_alpha(file):
    """
    Check if an image has alpha, which would need to be removed
    """
    img = Image.open(file, 'r')
    has_alpha = img.mode == 'RGBA'
    return(has_alpha)

def remove_alpha(file, output):
    """
    Remove alpha from: https://stackoverflow.com/questions/9166400/convert-rgba-png-to-rgb-with-pil/9459208
    """
    png = Image.open(file)
    png.load() # required for png.split()

    background = Image.new("RGB", png.size, (255, 255, 255))
    background.paste(png, mask=png.split()[3]) # 3 is the alpha channel
    
    background.save(output, 'PNG')

    return(output)


def which(program):
    """Function to check for presence of executable/installed program
       Used for checking presense of OCR"""
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None