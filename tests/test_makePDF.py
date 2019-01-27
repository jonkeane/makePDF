import pytest
from unittest import TestCase
from PIL import Image

import sys, os, shutil, uuid
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../src/makePDF/") # move to the src directory

import main

class TestMakePDF(TestCase):
    def test_make_pdf_wrong_file(self):
        with pytest.raises(IOError) as e_info:
            main.make_pdf_from_images(["/not/here.png"], "foo.pdf")
            assert e_info == "Something went wrong, I can't access the file at /not/here.png"

    def test_make_pdf(self):
        main.make_pdf_from_images(
        ['tests/images/travis-pride.png',
        'tests/images/travis-pride-sans-alpha.png'],
        output = "out.pdf"
        )