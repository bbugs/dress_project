
import nltk
import nltk.data
from utils_local import utils_local
import csv


import zTextProcessing as zt


data0 = utils_local.load_data0(fname='../data0.json')
#i = 239 #1224  #357

fname = 'data2crowdflower_test_done.csv'
f = open(fname, 'wb')
writer = csv.writer(f)


rdir = 'http://people.cs.kuleuven.be/~susana.zoghbi/dress_imgs/'
info = ("asin", "imgid", "folder", "img_dir", "brand", "sentences")

# for i in info:
#     f.write(i)
#     f.write(";")
#
# f.write('\n')

writer.writerow(info)

for dress in data0['dresses'][0:100]:
    #dress0 = data0['dresses'][i]

    features = dress['features']  # list of strings
    editorial = dress['editorial']  # string
    title = dress['title']  # string
    brand = dress['brand']
    asin = dress['asin']
    imgid = dress['imgid']
    folder = dress['folder']

    dir = rdir + folder + '/' + asin + '.jpg'

    all_text = [title] + features + [editorial] + ["done"]

    clean_sents = utils_local.get_sentences(all_text)
    # convert sentences to string separated by " \n"
    str_sents = "\%".join(clean_sents).encode('utf-8')
    #str_sents = "\%".join(clean_sents)
    #print str_sents


    info = (asin, imgid, folder, dir, brand, str_sents)
    #
    # for i in info:
    #     if type(i) == int:
    #         i = str(i)
    #
    #     f.write(i)
    #     f.write(";")
    writer.writerow(info)
    # f.write("\n")

f.close()