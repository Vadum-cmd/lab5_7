"""
Module for class object ScaleZip.
"""
import sys
import os
import shutil
import zipfile
from pathlib import Path
from PIL import Image


class ScaleZip:
    def __init__(self, zipname, w_size, h_size):
        """
        Initialize object of class ScaleZip.
        """
        self.zipname = zipname
        self.w_size = w_size
        self.h_size = h_size
        self.temp_directory = Path("unzipped-{}".format(
                zipname[:-4]))

    def process_zip(self):
        """
        Main method which uses the rest.
        It extracts files from archive, works with them and puts them back.
        """
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        """
        Extracts files from archive.
        """
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        """
        After work with files this method adds them to archive.
        """
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))

    def process_files(self):
        '''
        Scale each image in the directory to input value.
        '''
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((self.w_size, self.h_size))
            scaled.save(str(filename))
