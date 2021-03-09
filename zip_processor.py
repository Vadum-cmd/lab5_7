"""
Module for class object ZipProcessor.
"""
import os
import shutil
import zipfile


class ZipProcessor:
    def __init__(self, zipname):
        """
        Initialize object of class ZipProcessor.
        """
        self.zipname = zipname
        self.temp_directory = "unzipped-{}".format(zipname[:-4])


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
