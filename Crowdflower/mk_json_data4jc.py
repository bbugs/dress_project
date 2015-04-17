
from utils_local import utils_local

import json
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



data0 = utils_local.load_data0(fname='../data0.json')
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
    clean_sents = utils_local.get_sentences(all_text)

    sents_string = "<\%>".join(clean_sents)

    new_dress = init_dress_dict()
    new_dress['brand'] = brand
    new_dress['asin'] = asin
    new_dress['imgid'] = imgid
    new_dress['folder'] = folder
    new_dress['url'] = url
    new_dress['text'] = sents_string

    data['dresses'].append(new_dress)

    #print clean_sents



with open('data4jc_dirty.json', 'wb') as fp:
    json.dump(data, fp, indent=4, sort_keys=True)