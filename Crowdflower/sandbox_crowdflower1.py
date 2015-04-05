
import nltk
import nltk.data
import utils_local
import csv


import zTextProcessing as zt

# load punctuation
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


def get_sentences(all_text, verbose=0):
    """(list of strings) -> list of sentences (str)

    """
    sents = []  # clean sentences
    for item in all_text:
        # print item
        # tokenize into sentences
        temp_sentences = sent_tokenizer.tokenize(item)
        for s in temp_sentences:
            #print s
            sents.append(s)

    clean_sents = []
    for s in sents:
        s2 = s.split("<br>")
        for ss in s2:
            #print ss
            # s3 = ss.replace("<br />", "  ")
            # s3 = ss.replace("<br/>", "  ")
            s3 = zt.strip_tags(ss)
            #s4 = s3.replace("\n\n", "<sbr>")
            #s4 = s4.replace("\n", "<sbr>")
            clean_sents.append(s3)

    if verbose:
        for s in clean_sents:
            print s, '\n\n'

    return clean_sents



data0 = utils_local.load_data0()
#i = 239 #1224  #357

fname = 'data2crowdflower_test1.csv'
f = open(fname, 'wb')
#writer = csv.writer(f)


rdir = 'http://people.cs.kuleuven.be/~susana.zoghbi/dress_imgs/'
info = ("asin", "imgid", "folder", "img_dir", "sentences")

for i in info:
    f.write(i)
    f.write(";")

f.write('\n')

#writer.writerow(info)

for dress in data0['dresses'][0:100]:
    #dress0 = data0['dresses'][i]

    features = dress['features']  # list of strings
    editorial = dress['editorial']  # string
    title = dress['title']  # string

    asin = dress['asin']
    imgid = dress['imgid']
    folder = dress['folder']

    dir = rdir + folder + '/' + asin + '.jpg'

    all_text = [title] + features + [editorial]

    clean_sents = get_sentences(all_text)
    # convert sentences to string separated by " \n"
    #str_sents = "\n".join(clean_sents).encode('utf-8')
    str_sents = "\n".join(clean_sents)
    print str_sents


    info = (asin, imgid, folder, dir, str_sents)
    #
    for i in info:
        if type(i) == int:
            i = str(i)

        f.write(i)
        f.write(";")
    # writer.writerow(info)
    f.write("\n")

f.close()