from osm_changes_class_save.create_dir import full_path
from osm_changes_class_save.create_dir import list_file
from osm_changes_class_save.create_dir import list_file_unfiltered
from osm_changes_class_save.save_class import classsaver
import sys

def main(path,threshold):

    full= full_path(path)
    files = list_file_unfiltered(full)
    for file in files:
        print(file)
        classsaver(file,threshold)

if __name__ == "__main__":

    #path = 'output_swinden_config2'
    path = sys.argv[1]
    #path = f"{path}_filtered"
    threshold = sys.argv[2]
    threshold = int(threshold)

    main(path,threshold)



    

