from InvertedIndexModel import InvertedIndexModel,IndexNode,PostingList,PostingNode
from Cleaner import Cleaner
import nltk

class InvertedIndexManager(object):
    def __init__(self):
        self.invert_index_model=InvertedIndexModel()
        self.cleaner=Cleaner()
        self.last_doc_id=0

    def __read_doc(self,doc_name=""):
        lines=list()
        with open(doc_name,'r') as doc:
            lines=doc.read().splitlines()
        return lines

    def __get_tokens(self,line=""):
        return nltk.word_tokenize(line)

    def __get_token_frequency(self,lines=[]):
        term_frequency=dict()

        for line in lines:
            token_list=self.__get_tokens(line=line)
            token_list=self.cleaner.get_clean(p_token_list=token_list)
            for token in token_list:
                if token not in term_frequency:
                    term_frequency[token]=0
                term_frequency[token]=term_frequency[token]+1
        return term_frequency


    def process_doc(self,doc_name=""):
        self.last_doc_id=self.last_doc_id+1

        lines=self.__read_doc(doc_name=doc_name)
        term_frequency=self.__get_token_frequency(lines=lines)

        for term in term_frequency:
            frequency=term_frequency[term]
            self.invert_index_model.add_posting(term=term,doc_id=self.last_doc_id,tf_score=frequency)
        self.invert_index_model.update_idf()    
    
    def process_query(self,query=""):
        term_list=self.__get_tokens(line=query)
        inverted_index=self.invert_index_model.get_inverted_index()
        docs=dict() 

        for term in term_list:
            if term not in inverted_index:
                continue

            index_node=inverted_index[term]
            idf_score=index_node.get_idf()
            posting_list=index_node.get_posting_list()

            for posting in posting_list.get_list():
                doc=posting.doc_id
                tf_score=posting.tf_socre
                if doc not in docs:
                    docs[doc]=0
                docs[doc]=docs[doc]+float(tf_score)*float(idf_score)
        return docs

    def print_index(self):
        print(self.invert_index_model.get_string())


manager=InvertedIndexManager()
manager.process_doc(doc_name='../../docs/doc1.txt')
manager.process_doc(doc_name='../../docs/doc2.txt')
manager.process_doc(doc_name='../../docs/doc3.txt')
manager.print_index()
print(manager.process_query(query="Prime Minister Sheikh Hasina today Bangladesh and India have 54 common Khandaker Mosharraf Hossain akash"))
