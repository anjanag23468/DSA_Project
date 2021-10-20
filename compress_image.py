# Imports
from operator import add
from functools import reduce
import numpy as np
from PIL import Image
import os
import warnings

warnings.filterwarnings("ignore")  # Hide warnings


def import_image(img_path):
    """
    Imports an image from the system
    """

    img = Image.open(img_path)
    img = img.convert('RGB')  # Converting the image colours to RGB format
    img = np.array(img)       # Storing the image in the form of a numpy array
    return img


def img_size(img_path):
    """
    Calculates and returns the image size in Kilo Bytes (KB)
    """

    stats = os.stat(img_path)  # Storing img_path in stats variable
    return round(stats.st_size / 1024, 2)


def img_save(img_file, file_name):
    """
    Save the compressed image
    """

    im = img_file.astype(np.uint8)
    im = Image.fromarray(im)
    im.save(file_name)


def split_image(img):
    """
    Splits the image into 4 quadrants
    """

    half_split = np.array_split(img, 2)                            # Spliting the image in half
    res = map(lambda x: np.array_split(x, 2, axis=1), half_split)  # Spliting the image into one fourth quadrant
    return reduce(add, res)


def concatenate_image(top_left, top_right, bottom_left, bottom_right):
    """
    Reconstructs the full image from the four split quadrants.
    """

    top = np.concatenate((top_left, top_right), axis=1)          # Merging top_left and top_right
    bottom = np.concatenate((bottom_left, bottom_right), axis=1) # Merging bottom_left and bottom_right
    return np.concatenate((top, bottom), axis=0)


def calculate_mean(img):
    """
    Calculate the mean color of 4 quadrants of the image.
    """ 
    return np.mean(img, axis=(0, 1))


def checkEqual(myList):
    """
    Checks if all the 4 quadrants of the image are equal
    """
    first = myList[0]
    return all((x == first).all() for x in myList)


# A quadtree is a special tree that defines each node as having four quadrants.
# We will create insert function that will be called recursively.Then we will traverse the tree at each level.
# We save this level as the mean color calculated for the current level for the whole image.
# save the resolution in order to recreate the image with the same resolution as passed before.
# We will check if all the pixels in the image are equal. We stop the traversing and 
# we’ll be able to reconstruct the image at the current level by reconstructing an image from the resolution with the mean colour.
class QuadTree:
    def insert(self, img, level=0):
        """
        Recursively traverses the tree at each level
        """

        self.level = level
        self.mean = calculate_mean(img).astype(int)
        self.resolution = (img.shape[0], img.shape[1])
        self.final = True

        if not checkEqual(img):
            split_img = split_image(img)

            # If we have different pixel colors in the image then we create four quadrant and insert the
            # respective quadrant to each quadrant by calling the insert method passing the current level + 1.
            self.final = False
            self.top_left = QuadTree().insert(split_img[0], level + 1)
            self.top_right = QuadTree().insert(split_img[1], level + 1)
            self.bottom_left = QuadTree().insert(split_img[2], level + 1)
            self.bottom_right = QuadTree().insert(split_img[3], level + 1)

        return self

    def get_image(self, level):
        """
        Returns concatenated image
        """
        if self.final or self.level == level:
            return np.tile(self.mean, (self.resolution[0], self.resolution[1], 1))

        return concatenate_image(
            self.top_left.get_image(level),
            self.top_right.get_image(level),
            self.bottom_left.get_image(level),
            self.bottom_right.get_image(level))

   

def compress_image(path, save_name, threshold):
    """
    Driver function. Compresses the image based on input threshold and saves the image in the same directory as this python file
    """

    image = import_image(path)

    print('Preparing image. Please wait, this may take a while...')
    quadtree = QuadTree()  # Quadtree object
    quadtree.insert(image)
    print('Done')

    print('Compressing...')
    img_compressed = quadtree.get_image(threshold)
    print('Done!')

    print('Saving...')
    img_save(img_compressed, save_name)
    print('Done!')

    return img_compressed
