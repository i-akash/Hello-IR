import numpy as np
import math

class TF_IDF:
    def __init__(self):
        pass

    def get_tf(self,p_vector=np.zeros(10,dtype=int)):
        total_terms=np.sum(p_vector)
        return p_vector/total_terms

    def get_idf(self,vector_space_model):
        doc_list=vector_space_model.doc_list
        number_of_doc=len(doc_list)
        unique_tokens=vector_space_model.unique_tokens
        number_of_tokens=len(unique_tokens)

        token_rareity=np.zeros(number_of_tokens,dtype=float)

        for token_index in range(number_of_tokens):
            number_of_doc_token_existed=0
            for doc in doc_list:
                vector=doc.vector 
                if vector[token_index]>0:
                    number_of_doc_token_existed=number_of_doc_token_existed+1

            token_rareity[token_index]=math.log(number_of_doc/number_of_doc_token_existed)
        return token_rareity
    

    def update_tf_idf_vector(self,vector_space_model):
        doc_list=vector_space_model.doc_list
        for doc in doc_list:
            p_vector=self.get_tf(p_vector=doc.vector)
            token_rareity=self.get_idf(vector_space_model)
            tf_df_vector=p_vector*token_rareity
            doc.set_tf_idf_vector(p_vector=tf_df_vector)