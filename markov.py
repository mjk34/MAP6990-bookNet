import re as regex
import nltk

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

    def _find_unique(self, tokenized):
        unique_words = []
        for sentence in tokenized:
            sen_split = sentence.split(' ')
            for word in sen_split:
                if word not in unique_words:
                    unique_words.append(word)
    
        unique_clean = []
        for i in range(len(unique_words)):
            if (regex.match('[A-Za-z]*', unique_words[i])).group() == '': continue
            unique_clean.append(unique_words[i])
        
        return unique_clean

    def create_map (self, content):
        tokenized_array = self._tokenizer(content)
        unique_array = self._find_unique(tokenized_array)
        unique_array.sort()

        dict_array = []
        print(f'\nTotal unique words: {len(unique_array)}')
        for sentence in tokenized_array:
            sen_split = sentence.split(' ')
            associations = []
            for word in sen_split:
                if word in unique_array: associations.append(word)
            
            for i in range(len(associations)):
                if i == len(associations)-1: continue

                word = associations[i]
                # for j in range(i+1, len(associations)):
                #     match = associations[j]
                #     if word == match: continue
                #     # print(f'[{word}, {match}]')
                #     self.dictionary[word].append(match)
                for j in range(len(associations)):
                    match = associations[j]
                    if word == match: continue
                    # print(f'[{word}, {match}]')
                    self.dictionary[word].append(match)
                    
        for i in range(10):
            suggested_matches = nltk.Counter(
                self.dictionary[unique_array[i]]).most_common()
            match_size = len(suggested_matches)
            print(f'\nWord: {unique_array[i]}', end=' ')
            print(f'Matches: {match_size}')
            print('Top 5: ', end='')
            print(suggested_matches[:5])