

class InvertedIndexModel(object):
    def __init__(self):
        self.inverted_index=dict()
    
    def add_term(self,term=""):
        index_node=IndexNode(term=term)
        posting_list=PostingList()
        if index_node not in self.inverted_index:
            self.inverted_index[index_node]=posting_list


    def add_posting(self,term="",doc_id="",tf=0,total_doc=0):
        index_node=IndexNode(term=term)

        if index_node in self.inverted_index:
            posting_list=self.inverted_index[index_node]
            posting_list.add_posting(doc_id=doc_id,tf=tf,total_doc=total_doc)


class IndexNode(object):
    def __init__(self,term=""):
        self.term=term
    
    def __hash__(self):
        return hash(self.term)
    
    def __eq__(self,other):
        if isinstance(self,other.__class__):
            return self.term==other.term
        else :
            return "NotImplemented"
    

class PostingList(object):
    def __init__(self):
        self.posting_list=list()
        self.idf=0
    
    def add_posting(self,doc_id="",tf=0,total_doc=0):
        posting_node=PostingNode(doc_id=doc_id,tf=tf)
        self.posting_list.append(posting_node)
        self.update_idf(total_doc=total_doc,term_doc=len(self.posting_list))


    def update_idf(self,total_doc=0,term_doc=0):
        self.idf=log10((total_doc)/term_doc)


class PostingNode(object):
    def __init__(self,doc_id="",tf=0):
        self.doc_id=doc_id
        self.tf=tf

