import os
import numpy as np
import cv2
def load_images_of_folder_2_np(image_forder_1, image_folder_2):
    '''
    This code first stores images for comparison between images of the same name.
    step
    1. Exclude images that are not the same name.
    2. Load the images into bgr image by opencv.
    3. Tie up all the images and save them in numpy format.
    '''
    filenames_one = os.listdir(image_forder_1)
    filenames_two = os.listdir(image_folder_2)
    print("before the number of 1images: ", len(filenames_one))
    print("before the number of 2 images: ", len(filenames_two))
    #Find overlapping images.
    inter_filenames = list(set(filenames_one).intersection(filenames_two))
    print("after the number of inter images: ", len(inter_filenames))
    images_one_np =[]
    images_two_np =[]
    for index_name, name in enumerate(inter_filenames):
        full_file_name_one = image_forder_1 + inter_filenames[index_name]
        full_file_name_two = image_folder_2 + inter_filenames[index_name]
        temp1 = cv2.imread(full_file_name_one)
        image_one_cp = temp1.copy()
        temp2 = cv2.imread(full_file_name_two)
        image_two_cp = temp2.copy()
        images_one_np.append(image_one_cp)
        images_two_np.append(image_two_cp)
        if index_name%100 ==0:
            print("download : ", index_name)
    images_one_np = np.array(images_one_np)
    np.save('./saved_one', images_one_np)
    images_two_np = np.array(images_two_np)
    np.save('./saved_two', images_two_np)



