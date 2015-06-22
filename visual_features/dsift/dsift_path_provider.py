"""
dsift features have already been computed with dsift_main.py

This is a small script to generate the paths to the dsift files

Here we generate the paths of the training set

fout_name = 'paths_dress_dsift_train_val.txt
fout_name = 'paths_dress_dsift_test.txt



"""

# import os
# print os.getcwd()


# load train paths
img_paths_fname = '../..//DATASETS/dress_attributes/data/paths/paths_dress_test.txt'
f = open(img_paths_fname, 'r')
img_paths = f.readlines()
f.close()

# generate dsfit paths
dsift_paths = []
for path in img_paths:
    dsift_path = path.replace('data/images', 'dsift_images/size40_steps20')
    dsift_path = dsift_path.replace('.jpg\n', '.dsift')
    dsift_paths.append(dsift_path)
    #print path
    print dsift_path



# from data_manager.data_provider import DataProvider
#
# class dSiftProvider(object):
#     """
#
#     """
#
#     def __init__(self,
#                  dataset_fname='../../DATASETS/dress_attributes/data/json/dataset_dress_all_train_val.json '):
#
#         d = DataProvider(dataset_fname=dataset_fname)
#         img_paths = d.get_img_paths()
#
#         print img_paths[0:20]
#         pass
#
#
# if __name__ == '__main__':
#     dataset_fname = '../DATASETS/dress_attributes/data/json/dataset_dress_all_train_val.json '
#     ds = dSiftProvider(dataset_fname=dataset_fname)




#print len(dsift_paths)








