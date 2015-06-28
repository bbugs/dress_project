from data_manager.data_provider import DataProvider
from color_descriptor import color_extractor
from visual_features.color import color_data_provider as color_dp
import os
import time

fname = '../../DATASETS/dress_attributes/data/json/dataset_dress_all.json'
dp = DataProvider(dataset_fname=fname)
img_paths = dp.get_img_paths()

# img_paths = ['../../DATASETS/dress_attributes/vis_representation/color_descriptors/rgb/BridesmaidDresses2/B00UYR8JP2.jpg']

n = 25  # number of pixels to sample to get color
# color_space = 'hsv'

colos_spaces = ['rgb', 'hsv']

for color_space in colos_spaces:

    for img_path in img_paths:
        print img_path
        ce = color_extractor.ColorExtractor(img_path)
        ce.mk_center_path(patch_size=100, patch_show=False)
        ce.mk_random_indices(n=n)

        sample_rgb = ce.get_sample_rgb()
        sample_hsv = ce.get_sample_hsv()

        dst_path = color_dp.generate_one_color_path(img_path, color_space=color_space)
        e = dst_path.rfind('/')

        folder = dst_path[0:e]
        if not os.path.isdir(folder):
            os.mkdir(folder)

        ce.write_to_file(dst_path, color_space=color_space)
        # time.sleep(1)



