"""
Join both datasets: bergs and dresses
Choose item types: bags, earrings, ties, shoes, dresses
Choose item_subtypes: default: choose all

inputs:
dataset/dataset_berg.json
dataset/dataset_title.json

outputs:
dataset/dataset_title_feat.json
datase/dataset_title_edit_feat.json



"""



# Load both datasets
from utils_local import utils_local
import json
data_berg = utils_local.load_data0(fname='dataset/dataset_berg.json')


data_dress = utils_local.load_data0(fname='dataset/dataset_dress_all.json')

# join them into one
data = {}
data['items'] = []
data['items'].extend(data_berg['items'])
data['items'].extend(data_dress['items'])



# save the new dictionary
out_fname = 'dataset/dataset_joint_all.json'
# out_fname = 'dataset/dataset_joint_all.json'


with open(out_fname, 'wb') as fp:
    json.dump(data, fp, indent=4, sort_keys=True)