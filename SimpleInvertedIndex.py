

class InvertedIndex:
    def __init__(self):
        self.docs=list()
        self.hash_table=dict()
        self.__inverted_list=list()

    def __read_doc(self,doc_file='docs.txt'):
        document=list()
        with open(doc_file,'r') as file:
            document=file.read().splitlines()
            
        return document

    def __get_tokens(self,document=[""]):
        token_list=list()

        for lineNo in range(len(document)):
            line=document[lineNo]
            tokens=line.split()
            for token in tokens:
                token_list.append((token,lineNo))
        return token_list
    
    
    def make_inverted_index(self,doc_file='docs.txt'):
        document=self.__read_doc(doc_file=doc_file)
        token_list=self.__get_tokens(document=document)
        
        for token,lineNo in token_list:
            if token not in self.hash_table:
                self.hash_table[token]=len(self.hash_table)
                self.__inverted_list.append([])
            tokenNo=self.hash_table[token]
            self.__inverted_list[tokenNo].append(lineNo)
        return self.__inverted_list
                

        



inverted_index=InvertedIndex()
inverted_list=inverted_index.make_inverted_index()
print(inverted_list[inverted_index.hash_table['Apple']])