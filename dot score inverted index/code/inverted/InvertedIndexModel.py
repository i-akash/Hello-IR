from math import log10

class InvertedIndexModel(object):
    def __init__(self):
        self.inverted_index=dict()
        self.total_doc_number=0
    
    def __add_term(self,term=""):
        index_node=IndexNode(term=term)
        self.inverted_index[term]=index_node

    def add_posting(self,term="",doc_id="",tf_score=0):
        if term not in self.inverted_index:
            self.__add_term(term=term)
        index_node=self.inverted_index[term]
        self.total_doc_number=doc_id
        index_node.add_posting(doc_id=doc_id,tf_socre=tf_score)

    def update_idf(self):
        for index,index_node in self.inverted_index.items():
            index_node.update_idf(total_doc_number=self.total_doc_number,term_doc=index_node.posting_list.get_length())

    def get_inverted_index(self):
        return self.inverted_index

    def get_string(self):
        model=""
        for term in self.inverted_index.values():
            model=model+term.get_string()
        return model
        

class IndexNode(object):
    def __init__(self,term=""):
        self.term=term
        self.idf_score=0
        self.posting_list=PostingList()

    def update_idf(self,total_doc_number=0,term_doc=0):
        self.idf_score=log10((total_doc_number)/term_doc)

    def add_posting(self,doc_id="",tf_socre=0):
        self.posting_list.add_posting(doc_id=doc_id,tf_socre=tf_socre)
        
    def get_posting_list(self):
        return self.posting_list
    
    def get_idf(self):
        return self.idf_score

    def get_string(self):
        return 'term: {}, idf score: {}\n {}'.format(self.term,self.idf_score,self.posting_list.get_string())
        
    # def __hash__(self):
    #     return hash(self.term)
    
    # def __eq__(self,other):
    #     if isinstance(self,other.__class__):
    #         return self.term==other.term
    #     else :
    #         return "NotImplemented"



class PostingList(object):
    def __init__(self):
        self.posting_list=list()
        
    def add_posting(self,doc_id="",tf_socre=0):
        posting_node=PostingNode(doc_id=doc_id,tf_socre=tf_socre)
        self.posting_list.append(posting_node)
        
    def get_length(self):
        return len(self.posting_list)
    
    def get_list(self):
        return self.posting_list

    def get_string(self):
        strings_list=""
        for posting in self.posting_list:
            strings_list=strings_list+posting.get_string()
        return strings_list



class PostingNode(object):
    def __init__(self,doc_id="",tf_socre=0):
        self.doc_id=doc_id
        self.tf_socre=tf_socre

    def get_string(self):
        return 'doc id: {}, tf score: {}\n'.format(self.doc_id,self.tf_socre)
