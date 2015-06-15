"""
Create a dataset.json from the data0.json file, where now we remove dresses that are non-descriptive

This time we check whether the sentence has been excluded.  If the sentence has been excluded,
then we don't consider it for the dataset.

inputs:
save
filter_sent
title_in
editorial_in
features_in

excluded_fname = 'data_manager/preprocess/excluded_phrases.pkl'
included_fname = 'data_manager/preprocess/included_phrases.pkl'

dataset/data0.json
"""

import json
from utils_local import utils_local
import numpy as np
from numpy.random import RandomState
prng = RandomState(42)  # set the random state so that splits are the same

# decide whether to save the json file
save = False
if not save:
    print "json file will not be saved"

# decide whether to filter sentences based on previous human input
filter_sent = True  # set to False if processing only titles, set to True if processing all text: title+editorial+features
if not filter_sent:
    print "sentences will not be filtered"


from data_manager.preprocess.data_preprocessor import SentenceRemover, get_sentences

excluded_fname = 'data_manager/preprocess/excluded_phrases.pkl'
included_fname = 'data_manager/preprocess/included_phrases.pkl'
sr = SentenceRemover(excluded_fname, included_fname)

# indicate which parts to include in the dataset: title, editorial, features
title_in = True
editorial_in = True
features_in = True


def init_item_dict():
    dress = {}
    fields = ['imgid', 'asin', 'img_filename', 'item_type', 'item_subtype', 'folder', 'url', 'brand', 'text', 'split']
    for f in fields:
        # imgid is an int
        if f == 'imgid':
            dress[f] = 0
        # text is a list
        elif f == 'text':
            dress[f] = []
        # everything else is a string (asin, img_filename, item_type, folder, url, brand, split)
        else:
            dress[f] = ''
    return dress

data0_dress = utils_local.load_data0(fname='../../DATASETS/dress_attributes/data/json/data0.json')
#i = 239 #1224  #357



data = {}
data['items'] = []  # a list of dictionaries


N = len(data0_dress['dresses'])  # number of dresses


test_val_split = prng.choice(N, 5000, replace=False)  # randomly choose 2000 imgid for test and validations
test_split = prng.choice(test_val_split, 1000, replace=False)  # randomly choose 1000 for test. Rest is for validation






# # sample from a bernoulli distribution N times
# # toss a coin N times with prob. p of getting heads (1)
# N = len(data0['dresess'])  # number of dresses
# p = 0.8  # with probability p a dress is assigned to the train split
# split = np.random.binomial(1, p, N)  # bernoulli is a binomial with only 1 trial, thus 1.
#
# # Make sure that we have at least 80% for training
# while sum(split) < (p * N):
#     split = np.random.binomial(1, p, N)
#
# assert sum(split) > (p * N)

counter = 0
item_type = 'dress'
for dress in data0_dress['dresses']:
    #dress0 = data0['dresses'][i]

    features = dress['features']  # list of strings
    editorial = dress['editorial']  # string
    title = dress['title']  # string
    brand = dress['brand']
    asin = dress['asin']
    imgid = dress['imgid']
    folder = dress['folder']
    url = dress['url']

    if title_in and not editorial_in and not features_in:
        all_text = [title]

    elif title_in and not editorial_in and features_in:
        all_text = [title] + features

    elif title_in and editorial_in and not features_in:
        all_text = [title] + [editorial]

    elif title_in and editorial_in and features_in:
        all_text = [title] + features + [editorial]

    else:
        raise ValueError("Invalid setup!")



    # get list of sentences by breaking down the editorial into sentences and
    # adding the features and title

    processed_sents = get_sentences(all_text)

    # if you want to filter out sentences based on the excluded sentences
    if filter_sent:
        dress_sents = []
        for sent in processed_sents:
            # print sent
            # print type(sent)
            # check if sent is not empty
            if not sent:
                continue
            # remove sentences if they are just empty
            if sent.isspace():
                continue
            # remove sentences to exclude (previously marked as excluded sentences)
            new_sent = sr.mk_sent_comparable(sent)
            if new_sent in sr.excluded_sentences:
                continue
            dress_sents.append(sent)
    # if you don't want to filter sentences
    else:
        dress_sents = processed_sents

    if dress_sents:
        sents_string = "<\%>".join(dress_sents)
        #sents_string = "<\%>".join(dress_sents)

        new_dress = init_item_dict()
        new_dress['asin'] = asin
        new_dress['brand'] = brand
        new_dress['folder'] = 'dress_attributes/data/images/' + folder + '/'
        new_dress['img_filename'] = asin + '.jpg'
        new_dress['imgid'] = imgid
        new_dress['item_type'] = item_type
        new_dress['text'] = sents_string
        new_dress['url'] = url

        # remove digits from folder
        item_subtype = ''.join(i for i in folder if not i.isdigit())
        new_dress['item_subtype'] = item_subtype

        # assign a split
        if imgid not in test_val_split:
            new_dress['split'] = 'train'
        else:
            if imgid in test_split:
                new_dress['split'] = 'test'
            else:
                new_dress['split'] = 'val'

        data['items'].append(new_dress)  # add new dress to the list of dresses
    else:
        print "THIS ASIN HAS NO DRESS_SENTS"
        print asin, folder, dress_sents
        print '\n'

    #print clean_sents

if title_in and not editorial_in and not features_in:
    out_fname = 'dataset_dress' + '_title' + '.json'

elif title_in and not editorial_in and features_in:
    out_fname = 'dataset_dress' + '_title' + '_feat' + '.json'

elif title_in and editorial_in and not features_in:
    out_fname = 'dataset_dress' + '_title' + '_edit' + '.json'

elif title_in and editorial_in and features_in:
    out_fname = 'dataset_dress' + '_all' + '.json'

else:
    raise ValueError("Invalid setup!")

if save:
    out_fname = '../../DATASETS/dress_attributes/data/json/' + out_fname
    with open(out_fname, 'wb') as fp:
        json.dump(data, fp, indent=4, sort_keys=True)