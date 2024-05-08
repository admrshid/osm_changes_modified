""" Rearranges images into folders according to class """
from osm_changes_class_save.detector import detect_white_pixel
import os
import rasterio as r
import sys


def classsaver(path,threshold):

    filename = os.path.basename(path)
    out_dir = ['change_wantage_unfiltered','no_change_wantage_unfiltered']

    # create new folder for each class
    change_path = os.path.join(os.getcwd(),out_dir[0])
    no_change_path = os.path.join(os.getcwd(),out_dir[1])
    os.makedirs(change_path, exist_ok=True)
    os.makedirs(no_change_path, exist_ok=True)

    with r.open(path, 'r') as file:
        imarray = file.read()
        meta = file.meta
            
        # Detect whether class is change or no_change
        classes = detect_white_pixel(imarray, tolerance=threshold) 

        if classes == None:
            sys.exit(1)
        elif classes == 'change':
            out = os.path.join(change_path,filename)
            with r.open(out, 'w', **meta) as dst:
                dst.write(imarray)
        else:
            out = os.path.join(no_change_path,filename)
            with r.open(out, 'w', **meta) as dst:
                dst.write(imarray)
        

        


        

 
