import json
import os
import zTextProcessing as zt
import nltk
import nltk.data

def load_data0(fname='../data0.json'):
    with open(fname, 'r') as f:
        data0 = json.load(f)

    return data0


def write_line2txt(line, file_object):
    for l in line:
        file_object.write(l, ",")
    pass

def get_stored_sentences(fname):
    """(str) -> set
    Get a set of sentences stored in fname
    It could be the excluded sentences or the included ones
    """
    if not os.path.isfile(fname):
        sfile = open(fname, "w")
        sfile.close()
        sentences = set()

    else:
        sfile = open(fname, "r")

        # for s in sfile.readlines():
        #     print s
        #     print s.strip()

        sentences = [sentence for sentence in sfile.readlines()]
        print "number of sentences in the list", len(sentences)
        #print sentences[-1]
        sentences = set(sentences)
        print "number of sentences in the set", len(sentences)
        sfile.close()

    return sentences


def get_sentences(all_text, verbose=0):
    """(list of strings) -> list of sentences (str)
    group into a list of sentences title, features and editorial
    editorial is broken into sentences.

    """
    # load punctuation
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    sents = []  # clean sentences
    for item in all_text:
        # print item
        # tokenize into sentences
        temp_sentences = sent_tokenizer.tokenize(item)
        for s in temp_sentences:
            #print s
            s1 = s.replace("<br />", "<br>")
            s1 = s1.replace("<br/>", "<br>")
            if s1:
                sents.append(s1)

    clean_sents = []
    for s in sents:
        s2 = s.split("<br>")
        for ss in s2:
            #print ss
            # s3 = ss.replace("<br />", "  ")
            # s3 = ss.replace("<br/>", "  ")
            s3 = zt.strip_tags(ss)  # strip html tags
            if not s3.isspace():
                s4 = s3.replace("\n\n", "\%")
                s4 = s4.replace("\n", "\%")
                clean_sents.append(s4)

    if verbose:
        for s in clean_sents:
            print '\n', s

    return clean_sents

if __name__ == '__main__':
    excluded_fname = '/Users/susanaparis/Documents/Belgium/IMAGES_plus_TEXT/projects/dress_project/Crowdflower/excluded_phrases.csv'
    sentences = get_stored_sentences(excluded_fname)
    print sentences