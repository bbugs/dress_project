
import json
from utils_local import utils_local
import numpy as np


class DataStats(object):

    def __init__(self, item_type='dresses',
                 dataset_fname='dataset/dataset_joint_all.json',
                 img_path_root='../'):
        """
        Load data
        item_type can be dresses,
        """
        self.dataset = utils_local.load_data0(dataset_fname)
        self.item_type = item_type


    def get_num_items(self):
        # eg. dataset['dresses']
        return len(self.dataset[self.item_type])


    def get_files_split(self, split_name='train'):
        split_filepaths = []
        for item in self.dataset[self.item_type]:
            if item['split'] == split_name:
                split_filepaths.append()


class DataProvider(object):
    """

    """

    def __init__(self, dataset_fname='dataset/dataset_dress_all.json'):
        """
        """
        self.dataset = utils_local.load_data0(dataset_fname)
        return

    def get_img_paths(self, verbose=False):
        """
        """
        img_paths = []
        for item in self.dataset['items']:
            folder = item['folder']
            img_path = folder + item['img_filename']
            if verbose:
                print img_path
            img_paths.append(img_path)
        return img_paths

    def get_split_ids(self):



class CnnProvider(object):
    """

    """
    def __init__(self, dataset_fname='dataset/dataset_dress_title.json',
                 cnn_fname='../DATASETS/dress_attributes/cnn/cnn_dress_test.txt'):
        self.dataset = utils_local.load_data0(dataset_fname)
        self.cnn = np.loadtxt(cnn_fname)




if __name__ == '__main__':
    # d = DataStats()
    #
    # print "number of dresses is: ", d.get_num_dress()

    # d = DataProvider(dataset_fname='dataset/dataset_joint_title.json')
    #
    # d.get_img_paths(verbose=True)  # use this in the command line to write to file

    pass


