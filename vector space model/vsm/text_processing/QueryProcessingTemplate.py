from cleaning.Cleaner import Cleaner
import numpy as np

class QueryProcessingTemplate:
    def __init__(self,vector_space_model):
        self.cleaner=Cleaner()
        self.vector_space_model=vector_space_model

    
    def process(self,query=""):
        token_frquency_table=self.get_tokens_frequency(query=query)
        vector=self.get_vector(p_tokens=token_frquency_table)
        return vector

    def get_tokenize(self,line=""):
        return line.split()

    def get_tokens_frequency(self,query=""):
        token_dict=dict()
        token_list=self.get_tokenize(query)
        token_list=self.cleaner.get_clean(p_token_list=token_list)

        for token in token_list:
            if self.vector_space_model.is_in_unique_tokens(p_token=token)==False:
                continue

            if token not in token_dict:    
                token_dict[token]=0
            token_dict[token]=token_dict[token]+1
        return token_dict
    
    def get_vector(self,p_tokens={}):
        vector_coef=[]
        unique_tokens=self.vector_space_model.get_unique_tokens()

        for token in unique_tokens:
            if token in p_tokens:
                vector_coef.append(p_tokens[token])
            else :
                vector_coef.append(0)

        vector=np.array(vector_coef)
        return vector 