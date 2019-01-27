import pytest
from unittest import TestCase
from PIL import Image

import sys, os, shutil, uuid
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../src/makePDF/") # move to the src directory


import utils

class TestCLI(TestCase):
    def test_has_alpha(self):
        assert utils.has_alpha('tests/images/travis-pride.png')
        assert not utils.has_alpha('tests/images/travis-pride-sans-alpha.png')

    def test_remove_alpha(self):
        new_image = utils.remove_alpha('tests/images/travis-pride.png', 'tests/images/travis-pride-temp.png')
        img = Image.open(new_image, 'r')
        assert img.mode != 'RGBA'
        os.unlink(new_image)
