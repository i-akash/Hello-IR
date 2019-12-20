from VectorSpaceModel import VectorSpaceModel as vsm
from Document import Document
from text_processing.DocumentProcessingTemplate import DocumentProcessingTemplate as dpt 
from text_processing.QueryProcessingTemplate import QueryProcessingTemplate as qtp
import numpy as np

class VectorSpaceModelManager(object):
    def __init__(self):
        self.vector_space_model=vsm()
        self.document_processor=dpt(self.vector_space_model)
        self.query_processor=qtp(self.vector_space_model)


    def add_doc(self,filename=""):
        doc_id=self.vector_space_model.get_next_doc_id()
        document=Document(doc_id=doc_id,doc_name=filename)
        vector=self.document_processor.process(filname=filename)
        document.set_vector(vector=vector)
        self.vector_space_model.add_doc(document)
    
    def isearch(self,query):
        query_vector=self.query_processor.process(query=query)
        doc_list=self.vector_space_model.get_doc()

        for doc in doc_list:
            doc_vector=doc.get_vector()
            match_score=self.get_cosine_score(query_vector,doc_vector)
            print('Document: {0} has matching score: {1}'.format(doc.doc_name,match_score))


        

    def get_cosine_score(self,vector1,vector2):
        return np.dot(vector1,vector2)/np.sqrt(vector1.dot(vector1)*vector2.dot(vector2))

    

vsmm=VectorSpaceModelManager()


vsmm.add_doc(filename='../docs/doc3.txt')
vsmm.add_doc(filename='../docs/doc2.txt')
vsmm.add_doc(filename='../docs/doc1.txt')
vsmm.isearch(query="hasina")

