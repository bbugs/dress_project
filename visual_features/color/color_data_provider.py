from data_manager.data_provider import DataProvider
import random
import numpy as np

class ColorDataProvider(object):
    """

    """

    def __init__(self, n_img_sample=None, verbose=False,
                 dataset_fname='../../DATASETS/dress_attributes/data/json/dataset_dress_all_train_val.json'):

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

    def write_all_color_desc_to_file(self, out_fname, color_space='rgb'):
        """

        """
        if color_space == 'rgb':
            paths = self.rgb_paths
        elif color_space == 'hsv':
            paths = self.hsv_paths

        f = open(out_fname, 'w')

        for path in paths:
            # print path
            color = read_features_from_file(path)
            # print "color type", type(color)
            print "color shape", color.shape

            # in case
            if len(color.shape) < 2:
                color = np.zeros((1, 3))
                # raw_input("no color descriptor found")
            # assert color.shape[1] == 3  # color has 3 elements
            savetxt_compact(f, color)  # pass file handle to function
        f.close()





def read_features_from_file(filename, desc_dim=3):
    """
    Read feature descriptors and return in matrix form.
    desc_dim = 3.  Because color is expressed in rgb or hsv.
    """

    print filename
    features = np.loadtxt(filename)

    if features.shape[0] == 0:
        features = np.zeros((1, desc_dim))
        print "color descriptor not found", filename

    return features

def generate_one_color_path(img_path, color_space='rgb',
                            new_folder='vis_representation/color_descriptors/',
                            verbose=False):

    if color_space not in ['rgb', 'hsv']:
        raise ValueError("color space must be rgb or hsv")

    new_floder = new_folder + "%s/" % color_space

    dst_path = img_path.replace("data/images/", new_floder)
    dst_path = dst_path.replace(".jpg", ".%s" % color_space)

    if verbose:
        print dst_path

    return dst_path

def savetxt_compact(fh, x, fmt="%.6g", delimiter=','):
    """
    method may be used to save a numpy array compactly.
    I used for saving the cnn matrices
    http://stackoverflow.com/questions/24691755/how-to-format-in-numpy-savetxt-such-that-zeros-are-saved-only-as-0
    """

    for row in x:
        line = delimiter.join("0" if value == 0 else fmt % value for value in row)
        fh.write(line + '\n')



if __name__ == '__main__':
    split = 'test'
    color_space = 'rgb'
    dataset_fname = '../../DATASETS/dress_attributes/data/json/dataset_dress_all_%s.json' % split
    color_dp = ColorDataProvider(n_img_sample=None, dataset_fname=dataset_fname)
    color_dp.generate_color_paths(color_space=color_space)

    color_all_fname = '../../DATASETS/dress_attributes/vis_representation/color_descriptors/color_descriptors_%s.%s' % (split, color_space)
    color_dp.write_all_color_desc_to_file(out_fname=color_all_fname, color_space=color_space)

    #
    # images in black and white
    # "B00PW0C7YA.jpg"
    # B00MKZ4K5E.rgb
    # B00RDCYZS6.rgb


