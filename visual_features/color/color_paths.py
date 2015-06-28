# save a file with destination color paths.
# one file for rgb and one for hsv

from data_manager.data_provider import DataProvider

fname = '../../DATASETS/dress_attributes/data/json/dataset_dress_all.json'
dp = DataProvider(dataset_fname=fname)

img_paths = dp.get_img_paths()

for img_path in img_paths:
    dst_path = img_path.replace("data/images/",
                                "vis_representation/color_descriptors/hsv/")
    dst_path = dst_path.replace(".jpg", ".hsv")

    print dst_path
