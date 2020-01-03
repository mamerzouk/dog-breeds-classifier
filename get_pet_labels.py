#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: Mohamed Amine Merzouk
# DATE CREATED: 02-02-2020
# REVISED DATE: 02-02-2020
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# DONE 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function
#
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this

    # Creating the results dictionary
    results_dic = dict()
    # filenames is a list of the image_dir files names
    filenames = listdir(image_dir)
    # Removing the hidden file (that start with '.')
    filenames = list(filter(lambda x: x[0] != '.', filenames))
    # Looping over the filenames
    for filename in filenames:
        # Since the label can be composed of several words spearated by underscores, we do :
        # split contains the list of the words of the filename
        split = filename.split('_')
        # The first word is always in the dogs name so we add it directly (in lower case)
        label = split[0].lower()
        # Looping over the rest of the words
        for i in range(1, len(split)):
            # If the word doesn't start with a number, then it is part of the dog's name, we add it
            if split[i][0] not in  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                label += " " + split[i].lower()
            # If it starts with a number, then it's the number that comes after the name, we break
            else:
                break
        # Adding the label to the result_dic *as a list*
        results_dic[filename] = [label]

    return results_dic
