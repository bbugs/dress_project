from data_manager.data_provider import DataProvider
import random
import numpy as np

class ColorDataProvider(object):
    """

    """

    def __init__(self, n_img_sample=None, verbose=False,
                 dataset_fname='../../DATASETS/dress_attributes/data/json/dataset_dress_all.json'):

        """
        n_img_sample:  number of random images to use.  If none, use all images
        """

        d = DataProvider(dataset_fname=dataset_fname)
        self.img_paths = d.get_img_paths()
        self.dsift_paths = []  # initialize dsift paths

        if n_img_sample:
            self.img_paths = random.sample(self.img_paths, n_img_sample)

        if verbose:
            print self.img_paths[0:20]

        self.rgb_paths = self.generate_color_paths()
        self.hsv_paths = self.generate_color_paths(color_space='hsv')

        return

    def generate_color_paths(self, color_space='rgb', verbose=False):
        if color_space not in ['rgb', 'hsv']:
            raise ValueError("color space must be rgb or hsv")

        new_floder = "vis_representation/color_descriptors/%s/" % color_space

        dst_paths = []
        for img_path in self.img_paths:
            dst_path = img_path.replace("data/images/",
                                        new_floder)
            dst_path = dst_path.replace(".jpg", ".%s" % color_space)
            dst_paths.append(dst_path)
            if verbose:
                print dst_path

        return dst_paths

def generate_one_color_path(img_path, color_space='rgb',
                            new_folder='vis_representation/color_descriptors/', verbose=False):
    if color_space not in ['rgb', 'hsv']:
        raise ValueError("color space must be rgb or hsv")

    new_floder = new_folder + "%s/" % color_space

    dst_path = img_path.replace("data/images/",
                                new_floder)
    dst_path = dst_path.replace(".jpg", ".%s" % color_space)

    if verbose:
        print dst_path

    return dst_path
