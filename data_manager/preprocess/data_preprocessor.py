import os
import pickle
from utils_local import utils_local


to_include = ['neckline', 'aline', 'vneck', 'sheath', 'ruched', 'scoopneck',
              'shortsleev', 'fulllength', 'strapless', 'capsleeve', 'sweetheart',
              'aplique', 'applique', 'empire', 'column', 'ruffle', 'pleated', 'straps', 'boatneck',
              'sleeveless', 'rouche', 'cashmere', 'longsleeve', 'squareneck', 'leather',
              'silk', 'halter', 'silver', 'satin', 'chiffon', 'pink', 'purple','mermaid',
              'floorlength', 'organza', 'beading', '34sleeve', '34lengthsleeve', 'lengthsleeve', 'sleevejacket', 'roundneck', 'longdress', 'shortdress', 'floral', 'taffeta', 'eveningdress', 'promdress', 'beachdress', 'cotton', 'polyester', 'white', 'black', 'linen', 'rayon', 'mesh', 'nylon','wool', 'asymmetric', 'grecian', 'turtleneck', 'pencil','drape', 'dropwaist', 'plussize', 'ruching', 'beaded', 'appliques', 'lace', 'cinche', 'oneshoulder', 'tulle', 'kneelength', 'hilow', 'offshoulder', 'scallop', 'tencel', 'crisscross', 'sweaterdress', 'vintage']




def is_in_set(comp_sent, keyword_list):
    result = False
    for s in keyword_list:
        if s in comp_sent:
            #print s, " in ", comp_sent
            result = True
            break
    return result




class SentenceRemover():
    """

    """

    def __init__(self, excluded_fname, included_fname):
        """
        data_fname='../data0.json'
        excluded_fname = 'excluded_phrases.pkl'
        included_fname = 'included_phrases.pkl'
        """
        self.excluded_fname = excluded_fname
        self.included_fname = included_fname
        self.excluded_sentences = self.get_stored_sentences(excluded_fname)
        self.included_sentences = self.get_stored_sentences(included_fname)
        # characters to replace
        self.to_replace = """/_,-.?!':"(){};+$%^&*<>@#+=[]"""
        pass



    def get_user_input(self, sentence, verbose=0, very_verbose=0):
        """
        given a human-readable sentence, indicate
        """

        comp_sent = self.mk_sent_comparable(sentence)
        # if very_verbose:
        #     print "original sentence: \n", sentence
        #     print "comparable sentence: \n", comp_sent
        #     raw_input("press any key to continue")




        if comp_sent in self.excluded_sentences:
            if verbose:
                print "EXCLUDED already:"
                print "sent", sentence
                raw_input("excluded. press any key to continue")
            return


        elif comp_sent in self.included_sentences:
            if verbose:
                print "included already", sentence
                raw_input("included press any key to continue")
            return

        elif is_in_set(comp_sent, to_include):
            self.included_sentences.add(comp_sent)
            #print "comp_sent included\n", comp_sent
            #raw_input("press any key to continue")
            return





        print "evaluate the following sentence\n"
        print sentence
        option = raw_input("Press 0 to exclude:\n ")

        if option == '0':
            # place it in the excluded set
            self.excluded_sentences.add(comp_sent)
            print "added to excluded set"
            # raw_input("any key to continue")
            return

        else:
            # put it on the csv file for crowdflower
            self.included_sentences.add(comp_sent)
            print "added to INcluded set"
            # raw_input("press any key to continue")
            return



    def mk_sent_comparable(self, sentence):
        """
        make the sentence in lower case
        remove all the characters in self.to_replace
        """
        # make lower
        new_sentence = sentence.lower()
        new_sentence = "".join(new_sentence.split())
        # remove digits
        new_sentence2 = ''.join([i for i in new_sentence if not (i.isdigit() or i in self.to_replace)])
        return new_sentence2


    def get_stored_sentences(self, fname):
        """(str) -> set
        Get a set of sentences stored in fname using pickle
        It could be the excluded sentences or the included ones
        """
        if not os.path.isfile(fname):
            print "file does not yet exist. Do you wish to create a new file. %s\n" % fname
            option = raw_input("Press y for yes or any other key for no")
            if option == 'y':
                sfile = open(fname, "wb")
                sfile.close()
            sentences = set()

        else:
            print "Reading %s" % fname
            sfile = open(fname, "rb")

            # for s in sfile.readlines():
            #     print s
            #     print s.strip()

            sentences = pickle.load(sfile)
            print "number of sentences in the list", len(sentences)
            #print sentences[-1]
            sentences = set(sentences)
            print "number of sentences in the set", len(sentences)
            sfile.close()

        return sentences

    def commit(self):
        """
        Save exluded_phrases and included_sentences in pickle format
        """
        sfile = open(self.excluded_fname, "wb")
        pickle.dump(self.excluded_sentences, sfile)
        sfile.close()

        sfile = open(self.included_fname, "wb")
        pickle.dump(self.included_sentences, sfile)
        sfile.close()

if __name__ == '__main__':
    excluded_fname = 'data_manager/preprocess/excluded_phrases.pkl'
    included_fname = 'data_manager/preprocess/included_phrases.pkl'

    d = SentenceRemover(excluded_fname, included_fname)

    s = 'squareneck'

    print is_in_set(s)







