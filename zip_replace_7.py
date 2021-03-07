"""
Module for class object ZipReplace.
"""
import sys
import os
import shutil
import zipfile


class ZipReplace:
    def __init__(self, zipname, filename, search_string, replace_string):
        """
        Initialize object of class ZipReplace.
        """
        self.zipname = zipname
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = "unzipped-{}".format(
                filename)


    def _full_filename(self, filename):
        """
        Returns full name of file.
        """
        return os.path.join(self.temp_directory, filename)


    def unzip_files(self):
        """
        Extracts files from archive.
        """
        os.mkdir(self.temp_directory)
        zip = zipfile.ZipFile(self.zipname)
        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()


    def zip_files(self):
        """
        After work with files this method adds them to archive.
        """
        file = zipfile.ZipFile(self.zipname, 'w')
        for filename in os.listdir(self.temp_directory):
            file.write(self._full_filename(filename), filename)
        shutil.rmtree(self.temp_directory)


    def zip_find_replace(self):
        """
        Main method which uses the rest.
        It extracts files from archive, replaces some info in certain file and puts them back.
        """
        self.unzip_files()
        self.find_replace()
        self.zip_files()


    def find_replace(self):
        """
        Replaces selected info in certain file with given data.
        """
        for filename in os.listdir(self.temp_directory):
            with open(self._full_filename(filename)) as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)

            with open(self._full_filename(filename), "w") as file:
                file.write(contents)
