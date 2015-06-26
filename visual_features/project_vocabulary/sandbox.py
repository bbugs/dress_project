from visual_features.dsift.dsift_data_provider import get_dsift_paths_from_file
from local_descriptors import sift

paths = get_dsift_paths_from_file()

for p in paths[0:10]:
    print p

    # '../../DATASETS/dress_attributes/vis_representation/dsift_images/size90_steps40/BridesmaidDresses/B0009PDO0Y.dsift'


loc, desc = sift.read_features_from_file(p)

print loc, desc.shape