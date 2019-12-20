import numpy as np

class Document:
    """Document properties"""

    def __init__(self,doc_id=0,doc_name=""):
        self.doc_id=doc_id
        self.doc_name=doc_name
        self.vector=np.zeros(10,dtype=int)
    
    def set_vector(self,vector=np.zeros(10,dtype=int)):
        """Setting  the vector"""
        self.vector=vector
    
    def update_vector(self):
        self.vector=np.append(self.vector,0)

    def get_vector(self):
        return self.vector
    
