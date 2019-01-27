import sys, os, shutil, tempfile, shlex, subprocess
from PIL import Image
import img2pdf

import utils

# define our clear function 
def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 

def make_pdf_from_images(images, output, letter = True):
    """
    Take images and make one pdf
    """
    temp_files = []
    
    # test if images are either Images or files 
    for i, s in enumerate(images):
        image = images[i]

        if not os.path.isfile(image):
            # the image doesn't exist, exit.
            m = "Something went wrong, I can't access the file at {}".format(i)
            raise IOError(m)
    
        if (utils.has_alpha(image)):
            _, path = tempfile.mkstemp()
            temp_files.append(path)
            images[i] = utils.remove_alpha(image, path)
            
    # test if output already exists?
    letter_inpt = (img2pdf.mm_to_pt(215.9),img2pdf.mm_to_pt(279.4))
    layout_fun = img2pdf.get_layout_fun(letter_inpt)
    
    try:
        with open(output,"wb") as f:
            if letter:
                f.write(img2pdf.convert(images, layout_fun=layout_fun))
            else:
                f.write(img2pdf.convert(images))
    except:
        # remove all temp files
        [os.unlink(x) for x in temp_files]
        raise
        
def make(default_filename = "images.pdf"):
    """
    Take images and make one pdf
    """
    clear()

    file_string = raw_input("Please drag and drop your image files here. Press return when you are done.\n")
    files = shlex.split(file_string)
    
    clear()
    
    output = raw_input("Where should the PDF be saved? Press return when you are done.\n")
    
    if os.path.isdir(output):
        # If there's just a folder, then add the default filename
        output = os.path.join(output, default_filename)    
    elif os.path.isdir(output[:-1]):
        # If there's just a folder, then add the default filename
        output = os.path.join(output[:-1], default_filename)

    # TODO: ask to make 8.5/11 (default:yes)?
    # TODO: ask to OCR (default:yes)?
    
    make_pdf_from_images(files, output)
    
    ocr_my_pdf = utils.which("ocrmypdf")
    if ocr_my_pdf is not None:
        print("Starting OCR, this could take some time.")
        _, temp_path = tempfile.mkstemp()
        proc_code = subprocess.call([ocr_my_pdf, output, temp_path])
        
        # if successful, move the temp file over the output
        if proc_code == 0:
            os.rename(temp_path, output)
        else:
            # otherwise, remove the temp file.
            os.unlink(temp_path)
            m = "Something went wrong with the OCR process, but the PDF is created."
            raise IOError(m)
        
