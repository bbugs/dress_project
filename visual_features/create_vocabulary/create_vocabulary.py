

"""
Here I create the vocabulary

input:  path to file that contains a list of paths for the training .dsift images or another desriptor like color.

output:  pickle file

"""

# Read which asins belong to the training set from create_db2 import text_search
from create_db2 import text_search
from PIL import Image
import numpy as np
import pickle
import vocabulary
import sift
from PIL import Image

db_name = '../data/databases/dress_text_db.db'
indx = text_search.Indexer(db_name)

# get the asins in the train set
searcher = text_search.Searcher(db_name)
train_asins = searcher.get_asins_split('train')

# Read the images corresponding to the training set
rpath = '../data/images/'
spath = '../data/databases/train_set_sift/'
nbr_images = len(train_asins)
train_sift_paths = []  # where to save the sift features
for asin in train_asins:
    # get the directory:
    folder = searcher.get_image_directory(asin)
    img_path = rpath + folder + '/' + asin + '.jpg'  # where to find original image

    # where to save the sift features
    sift_path = spath + asin + '.sift'
    train_sift_paths.append(sift_path)
    sift.process_image(img_path, sift_path)  # when you call sift.process_image, a tmp.pgm file gets created which temporarily creates a grayscale image to be processed by sift

print "Finished extracting Sift features"

# Create a vocabulary
nbr_words = 1000
voc = vocabulary.Vocabulary('dress_visual_vocabulary_%s' % nbr_words)
subsample_rate = 10
print "Training vocabulary"
voc.train(train_sift_paths, nbr_words, subsample_rate)  # featlist contains the path to the .sift files.

# saving vocabulary using pickle
print "Saving vocabulary"
with open('../data/databases/dress_visual_vocabulary.pkl', 'wb') as f:
    pickle.dump(voc, f)

print 'vocabulary is: ', voc.name, voc.nbr_words


