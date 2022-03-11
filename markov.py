import re as regex
import nltk
import numpy as np

from nltk import word_tokenize as _token
nltk.download('punkt')

class Markov:
    def __init__(self):
        self.dictionary = nltk.defaultdict(list)

    def _tokenizer (self, content):
        content = content.decode('ascii', errors='ignore')
        reduce_case = content.lower()
        reduce_split = regex.split(r'[.!?]', reduce_case)
        
        for i in range(len(reduce_split)):
            reduce_comma = reduce_split[i].replace(',', '')
            token = _token(reduce_comma)
            restring = ' '.join(token)
            reduce_split[i] = restring

        return reduce_split

    def get_word_list(self):
        return list(self.dictionary.keys())

    def create_mat (self, content):
        tokenized_array = self._tokenizer(content)
        
        for sentence in tokenized_array:
            sen_split = sentence.split(' ')
            associations = []
            for word in sen_split:
               if (regex.match('[A-Za-z]*', word)).group() == '': continue
               else: associations.append(word)

            if len(associations) == 1: continue
            for i in range(len(associations)):
                word = associations[i]
                for j in range(len(associations)):
                    match = associations[j]
                    if word == match: continue
                    # print(f'[{word}, {match}]')
                    self.dictionary[word].append(match)

        dict_keys = list(self.dictionary.keys())
        dict_keys.sort()
        print(f'\nTotal unique dict: {len(dict_keys)}')
        
        network_matrix = np.zeros((len(dict_keys), len(dict_keys)))
        for i in range(len(dict_keys)):
            suggested_matches = nltk.Counter(
                self.dictionary[dict_keys[i]]).most_common()
            # print(len(suggested_matches))
            
            for match in suggested_matches:
                if match[0] in dict_keys:
                    j = dict_keys.index(match[0])
                    # print(f'Word: "{dict_keys[i]}" Match: "{match[0]}" Count: {match[1]}')
                    network_matrix[i][j] = match[1]


        return network_matrix
        
        # for i in range(len(dict_keys)):
        #     for j in range(len(dict_keys)):
                # if network_matrix[i][j] > 0:
                    # print(f'TEST: the word "{dict_keys[i]}" occurs {network_matrix[i][j]} times with the word "{dict_keys[j]}"')