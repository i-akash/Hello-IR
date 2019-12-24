from VectorSpaceModel import VectorSpaceModel as vsm
from Document import Document
from text_processing.DocumentProcessingTemplate import DocumentProcessingTemplate as dpt 
from text_processing.QueryProcessingTemplate import QueryProcessingTemplate as qtp
from score.TF_IDF import TF_IDF
import numpy as np

class VectorSpaceModelManager(object):
    def __init__(self):
        self.vector_space_model=vsm()
        self.document_processor=dpt(self.vector_space_model)
        self.query_processor=qtp(self.vector_space_model)
        self.tf_idf=TF_IDF()


    def add_doc(self,filename=""):
        doc_id=self.vector_space_model.get_next_doc_id()
        document=Document(doc_id=doc_id,doc_name=filename)
        vector=self.document_processor.process(filname=filename)
        document.set_vector(vector=vector)
        self.vector_space_model.add_doc(document)
    
    def update_tf_df(self):
        self.tf_idf.update_tf_idf_vector(self.vector_space_model)
       
    def isearch_tfidf(self,query):
        query_vector=self.query_processor.process(query=query)
        query_tf_vector=self.tf_idf.get_tf(p_vector=query_vector)
    
        doc_list=self.vector_space_model.get_doc()

        for doc in doc_list:
            doc_vector=doc.get_tf_idf_vector()

            match_score=self.get_cosine_score(query_tf_vector,doc_vector)
            print('Document: {0} has matching score: {1}'.format(doc.doc_name,match_score))


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
vsmm.add_doc(filename='../docs/doc1.txt')
vsmm.add_doc(filename='../docs/doc2.txt')
vsmm.add_doc(filename='../docs/doc3.txt')

vsmm.update_tf_df()

print("-------------with tf idf--------------")
vsmm.isearch_tfidf(query="Prime Minister Sheikh Hasina agreements two rivers men to be prepared")
print("-------------without tf idf--------------")
vsmm.isearch(query="Prime Minister Sheikh Hasina agreements two rivers men to be prepared")
