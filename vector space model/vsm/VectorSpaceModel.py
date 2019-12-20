import numpy as np




class VectorSpaceModel:
    def __init__(self):
        self.unique_tokens=dict()
        self.doc_list=list()
        self.doc_count=0

    def is_in_unique_tokens(self,p_token=""):
        if p_token in self.unique_tokens:
            return True
        return False
    
    def add_token(self,p_token=""):
        self.unique_tokens[p_token]=len(self.unique_tokens)
        for doc in self.doc_list:
            doc.update_vector()

    def add_doc(self,document):
        self.doc_count=self.doc_count+1
        self.doc_list.append(document)
    
    def get_doc(self):
        return self.doc_list

    def get_unique_tokens(self):
        return self.unique_tokens.keys()

    def get_next_doc_id(self):
        return self.doc_count

    


        

    

