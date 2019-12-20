from nltk.stem import PorterStemmer

class Cleaner:
    def __init__(self):
        self.porterStemmer=PorterStemmer()

    def get_stemize(self,p_token=""):
        l_token=self.porterStemmer.stem(p_token)
        return l_token

    def is_stop_word(self,p_token=""):
        return False


    def get_clean(self,p_token_list=[]):
        l_token_list=list()
        for token in p_token_list:
            if self.is_stop_word(p_token=token):
                continue
            token=self.get_stemize(p_token=token)
            l_token_list.append(token)
        
        return l_token_list


