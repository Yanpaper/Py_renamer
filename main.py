import os
import numpy
import datetime # get modified or created time 
from PIL import Image # get Exif information
from PIL.ExifTags import TAGS



def main():
    rename_file = Renamer()
    #rename_file.get_filelist_just_dir(r"D:\Install_Programs\Motile_m141_초기설치")
    img_exif = rename_file.get_modified_time(r"D:\Pictures\2020-07-18-11-01-51-068.jpg")
    print (img_exif)

class Renamer():
    def __init__(self):
        self.dirname = ""

    def get_filelist_just_dir(self, dirname, extension=None):
       self.file_list = []
       self.dirname = dirname
       filenames = os.listdir(dirname)
       for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if extension == None:
                self.file_list.append(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == extension: 
                    self.file_list.append(full_filename)

    #def get_filelist_include_subpath(self, dirname, extension=""):
    #    self.file_list =[]
    #    for (path, dir, files) in os.walk(dirname):
    #        for filename in files:
    #            ext = os.path.splitext(filename)[-1]
    #            if ext == extension:
    #                self.file_list.append([path, filename])

    def change_filename_by_range(self):
        return

    def get_modified_time(self, full_filename):
        try:
            file_datetime = str(datetime.datetime.fromtimestamp(os.path.getmtime(full_filename)))
            edited_format = (file_datetime.replace(" ", "_")).replace(":", "-")
            return edited_format
        except:
            return "Fail : get modified time"

    def get_created_time(self, full_filename):
        try:
            file_datetime = str(datetime.datetime.fromtimestamp(os.path.getctime(full_filename)))
            edited_format = (file_datetime.replace(" ", "_")).replace(":", "-")
            return edited_format
        except:
            return "Fail : get created time"

##############################################################################
class Photo_Info():
    
    def __init__(self, full_filename):
        self.img_tags = {}
        img = Image.open(full_filename)
        img_info = img._getexif()
        for tag, value in img_info.items():
            decoded = TAGS.get(tag, tag)
            self.img_tags[decoded] = value
        img.close()

    def get_img_datetime(self):
        # YYYY-mm-dd_HH-MM-SS
        try:
            return (self.img_tags['DateTime'].replace(":", "-")).replace(" ", "_")
        except: 
            return "No exif info : DateTime"

    def get_img_camera_model(self):    
        try:    
            return self.img_tags['Model']
        except: 
            return "No exif info : Model"
    
    def get_img_size(self):
        try:
            return (self.img_tags['ImageWidth'], self.img_tags['ImageLength']) 
        except: 
            return "No exif info : ImageWidth, ImageLength"
##############################################################################

if __name__ == "__main__":
    main()