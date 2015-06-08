"""

Create initial json file

INPUT: /Users/susanaparis/Documents/Belgium/IMAGES_plus_TEXT/DATASETS/dress_attributes/data/images

Note: we use the images directory and not the xml directory because images have been cleaned for duplicates
and they are guaranteed to have the image, whereas the xml does not know which images are not present

OUTPUT:  data0.json

Notes:
xml files live in
/Users/susanaparis/Documents/Belgium/IMAGES_plus_TEXT/DATASETS/dress_attributes/data/xml

images live in
/Users/susanaparis/Documents/Belgium/IMAGES_plus_TEXT/DATASETS/dress_attributes/data/images



"""
import os
import json
from amazon_xml_item import AmazonXMLItem


def init_dress_dict():
    dress = {}
    fields = ['imgid', 'asin', 'folder', 'url', 'title', 'brand', 'color', 'features', 'editorial', 'other']
    for f in fields:
        if f == 'imgid':
            dress[f] = 0
        elif f == 'features':
            dress[f] = []
        elif f == 'other':
            dress[f] = {}
        else:
            dress[f] = ''
    return dress

# get xml files for each directory
# check directories for files
r_xml_path = '/Users/susanaparis/Documents/Belgium/IMAGES_plus_TEXT/DATASETS/dress_attributes/data/xml/'
folders = [f for f in os.listdir(r_xml_path) if not f.startswith(".")]

r_img_path = '/Users/susanaparis/Documents/Belgium/IMAGES_plus_TEXT/DATASETS/dress_attributes/data/images/'


data = {}
data['dresses'] = []  # a list of dictionaries
data['asin2imgid2folder'] = {}
data['folder2asin2imgid'] = {}



imgid = 0
for folder in folders:
    # TODO: consider having a separate file (csv or txt) with all the
    # images to process, instead of reading this directory
    img_path = r_img_path + folder
    asins = [f for f in os.listdir(img_path) if not f.startswith(".")] # take the asins from the image folder

    xml_path = r_xml_path + folder
    for asin in asins:
        # initialize dress dictionary
        dress = init_dress_dict()
        xml_file_name = xml_path + '/' + asin.replace(".jpg", "") + '.xml'
        axml = AmazonXMLItem(xml_file_name)

        # populate dress dictionary with info from the xml
        dress['imgid'] = imgid
        dress['asin'] = axml.get_asin()
        dress['folder'] = folder
        dress['title'] = axml.get_title()
        dress['url'] = axml.get_img_url()
        dress['brand'] = axml.get_brand()
        dress['features'] = axml.get_all_features()
        dress['editorial'] = axml.get_editorial()
        dress['other'] = axml.get_attributes()
        imgid += 1
        data['dresses'].append(dress)
        asin = asin.replace(".jpg", "")
        assert asin == dress['asin']
        data['asin2imgid2folder'][asin] = (imgid, folder)
        if folder not in data['folder2asin2imgid']:
            data['folder2asin2imgid'][folder] = []
        data['folder2asin2imgid'][folder].append((asin, imgid))


# with open('data1.json', 'wb') as fp:
#     json.dump(data, fp)

with open('data1.json', 'wb') as fp:
    json.dump(data, fp, indent=4, sort_keys=True)
