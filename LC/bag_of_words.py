'''
from bag of words recipe in www.norvig.com jupyter nb

@date: Fri 7 Oct 2016
@author: claud29
'''
import re
from collections import Counter
PATHS = ['wikipedia_pt.txt']
TEXT_STRINGS =  []
ALFABETO = 'a b c d e f g h i j l m n o p q r s t u v w y x z á à â ã ç é ê í ï ó ô õ ú ü'.split()
LETRAS = 'abcdefghijlmnopqrstuvwyxzáàâãçéêíïóôõúü'

def get_texts(paths = PATHS, recipient = TEXT_STRINGS):
    '''
    returns list of texts found in files in paths
    '''
    for path in paths:
        fh = open(path, 'r')
        recipient.append( fh.read() )
        fh.close()
    return recipient

def tokenize(text, letras = ALFABETO):
    '''
    returns list of tokens in :param text

    :param text: a string
    '''
    return re.findall( '[abcdefghijlmnopqrstuvwyxzáàâãçéêíïóôõúü]+',
                       text.lower() ) 

def bag_of_words(words):
    '''
    returns dictionary

    :param words: list of strings
    '''
    return Counter(words)

def frequence(bag, n = 3):
	'''
	returns n most frequent words
	'''
	return bag.most_common(n)

def what_frequence(bag, word):
	'''
	returns number of times word appears in bag
	'''
	return word, bag[word]

txts = get_texts()
tokens = tokenize(txts[0])
bag = bag_of_words(tokens)
common = frequence(bag)
print what_frequence(bag, 'golpe')

