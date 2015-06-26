
from vocabulary_projector import VocabularyProjector

from collections import Counter

dsift_paths_fname = '../../DATASETS/dress_attributes/data/paths/paths_dress_dsift_train_val.txt'
voc_fname = '../../DATASETS/dress_attributes/dsift_images/dress_dsift_nwords_20_vocab.pkl'
rpath = '../../DATASETS/'  # pre-pend this to the dsfit paths



def np2lda(words_in_doc):
    """(np array)
    Given numpy array that corresponds to a document
    """
    print Counter(words_in_doc)
    return




f = open(dsift_paths_fname, 'r')
dsift_paths = [rpath + l.replace("\n", "") for l in f.readlines()]
f.close()

vp = VocabularyProjector(voc_fname)

for dpath in dsift_paths[0:2]:
    img_desc = vp.get_descriptor(dpath)
    words = vp.project_on_img(img_desc)
    np2lda(words)
    #print words


