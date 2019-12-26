from InvertedIndexModel import InvertedIndexModel
from Cleaner import Cleaner
import nltk

class InvertedIndexManager(object):
    def __init__(self):
        self.invert_index_model=InvertedIndexModel()
        self.cleaner=Cleaner()
        self.last_doc_id=0

    def read_doc(self,doc_name=""):
        lines=list()
        with open(doc_name,'r') as doc:
            lines=doc.read().splitlines()
        return lines

    def get_tokens(self,line=""):
        return nltk.word_tokenize(line)

    def get_token_frequency(self,lines=[]):
        term_frequency=dict()

        for line in lines:
            token_list=self.get_tokens(line=line)
            token_list=self.cleaner.get_clean(p_token_list=token_list)
            for token in token_list:
                if token not in term_frequency:
                    term_frequency[token]=0
                term_frequency[token]=term_frequency[token]+1
        return term_frequency


    def process_doc(self,doc_name=""):
        self.last_doc_id=self.last_doc_id+1

        lines=self.read_doc()
        term_frequency=self.get_token_frequency(lines=lines)

        for term in term_frequency:
            frequency=term_frequency[term]
            self.invert_index_model.add_posting(term=term,doc_id=self.last_doc_id,tf_score=frequency)
            

