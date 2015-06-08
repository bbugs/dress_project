"""
input:  ../berg_project/data0_berg.json
output: dataset/dataset_berg.json

"""

import json
from utils_local import utils_local
import numpy as np


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

def get_item_subtype(folder_name):
    """
    e.g., folder_name = 'bags_backpacks'
    item_subtype = 'backpacks'
    """
    s = folder_name.find('_')
    e = folder_name.find('/')
    item_subtype = folder_name[s+1:e]
    return item_subtype

def mk_new_item(item):
    asin = ''
    if 'asin' in item:
        asin = item['asin']

    brand = ''
    if 'brand' in item:
        brand = item['brand']

    folder = ''
    if 'folder' in item:
        folder = item['folder']

    img_filename = ''
    if 'img_filename' in item:
        img_filename = item['img_filename']

    imgid = 0
    if 'imgid' in item:
        imgid = item['imgid']

    text = ''
    if 'text' in item:
        text = item['text']
        #print "txt len", img_filename, len(text)

    url = ''
    if 'url' in item:
        url = item['url']

    new_item = init_item_dict()
    new_item['asin'] = asin
    new_item['brand'] = brand
    new_item['folder'] = folder + '/'
    new_item['img_filename'] = img_filename
    new_item['imgid'] = imgid
    new_item['item_type'] = item_type
    new_item['text'] = text
    new_item['url'] = url
    new_item['item_subtype'] = get_item_subtype(folder)
    #print new_item['item_subtype']

    # assign a split
    if imgid not in test_val_split:
        new_item['split'] = 'train'
    else:
        if imgid in test_split:
            new_item['split'] = 'test'
        else:
            new_item['split'] = 'val'
    return new_item

data0_berg = utils_local.load_data0(fname='../berg_project/data0_berg.json')
item_types = ['bags', 'ties', 'earrings', 'shoes']


data = {}
data['items'] = []


for item_type in item_types:
    N = len(data0_berg[item_type])
    print "item_type", item_type
    print "number of items in ", item_type, ": ", N

    N20 = int(0.2 * N)  # 20% of the data
    test_val_split = np.random.choice(N, N20, replace=False)  # randomly choose 2000 imgid for test and validations

    print "len test val split", len(test_val_split)
    # print test_val_split

    N10 = int(0.1 * N)  # 10% of the data
    test_split = np.random.choice(test_val_split, N10, replace=False)
    print "len test split", len(test_split)
    #print test_split

    for item in data0_berg[item_type]:

        new_item = mk_new_item(item)
        # add item to data
        data['items'].append(new_item)




out_fname = 'dataset_berg.json'
out_fname = 'dataset/' + out_fname
with open(out_fname, 'wb') as fp:
    json.dump(data, fp, indent=4, sort_keys=True)


