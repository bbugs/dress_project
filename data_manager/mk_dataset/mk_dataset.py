"""
Create a dataset from the data0.json file, where now we remove dresses that contain
zero descriptive sentnces.

This time we check whether the sentence has been excluded.  If the sentence has been excluded,
then we don't consider it for the dataset.
"""

import json
from utils_local import utils_local

from data_manager.preprocess.data_preprocessor import SentenceRemover
excluded_fname = 'data_manager/preprocess/excluded_phrases.pkl'
included_fname = 'data_manager/preprocess/included_phrases.pkl'
sr = SentenceRemover(excluded_fname, included_fname)

def init_dress_dict():
    dress = {}
    fields = ['imgid', 'asin', 'folder', 'url', 'brand', 'text']
    for f in fields:
        if f == 'imgid':
            dress[f] = 0
        elif f == 'text':
            dress[f] = []
        else:
            dress[f] = ''
    return dress



data0 = utils_local.load_data0(fname='dataset/data0.json')
#i = 239 #1224  #357


data = {}
data['dresses'] = []  # a list of dictionaries

for dress in data0['dresses']:
    #dress0 = data0['dresses'][i]

    features = dress['features']  # list of strings
    editorial = dress['editorial']  # string
    title = dress['title']  # string
    brand = dress['brand']
    asin = dress['asin']
    imgid = dress['imgid']
    folder = dress['folder']
    url = dress['url']

    all_text = [title] + features + [editorial]



    # get list of sentences by breaking down the editorial into sentences and
    # adding the features and title
    processed_sents = utils_local.get_sentences(all_text)


    dress_sents = []
    for sent in processed_sents:
        # print sent
        # print type(sent)
        if not sent:
            continue
        # remove sentences if they are just empty
        if sent.isspace():
            continue
        # remove sentences to exclude
        new_sent = sr.mk_sent_comparable(sent)
        if new_sent in sr.excluded_sentences:
            continue
        dress_sents.append(sent)

    if dress_sents:
        sents_string = "<\%>".join(dress_sents)

        new_dress = init_dress_dict()
        new_dress['brand'] = brand
        new_dress['asin'] = asin
        new_dress['imgid'] = imgid
        new_dress['folder'] = folder
        new_dress['url'] = url
        new_dress['text'] = sents_string

        data['dresses'].append(new_dress)

    #print clean_sents



with open('dataset/dataset.json', 'wb') as fp:
    json.dump(data, fp, indent=4, sort_keys=True)