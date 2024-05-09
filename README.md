# osm_changes_modified
Additional scripts added to osm_changes for filtering and designating classes

The added modules/scripts/folder along with their functions include:
1.	iterate.py (in case for a moving window idea for the bitemporal osm layers)
2.	noise_remover.py (for filtering out labelled segments using skimage.morphology.remove_small_objects)
3.	osm_changes_class_save module (separates out changed filtered images into change folder and unchanged unfiltered images into unchange folder)
4.	run folder (contains a .bat file to as an executable for running the whole process in figure below)

![image](https://github.com/admrshid/osm_changes_modified/assets/159965213/22753a52-0671-4b48-beed-0eb6fba83112)

## Iterate.py
Essentially opens the config file and rewrites them with different configs according to the list in test.bat file

## noise_remover.py
Removes labelled segments < minsize using skimage.morphology.remove_small_objects

## osm_changes_class_save
Saves .tiff images into a change and no_change folder where images will be considered change if the total no of white pixels > certain thershold

## run folder
Contains test.bat which can be modified which executes the processing chain shown in the figure shown previously

# Things to note when running test.bat
1. Modify it to make sure it changes to your working directory (path\to\osm_changes_modified)
2. Modify it to activate your wanted virtual environment (from the packages specified in osm_changes, the additional package would need include 'pip install scikit image')
