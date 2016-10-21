'''
@date: Fri 7 Oct 2016
@author: claud29

starting from peter norvig's jupyter nb how to do things with words

'''
import random
from bag_of_words import get_text, tokenize

def write_random_sentence(bag, n = 10):
	'''
	random n word sentence with words in bag
	
	'''
	return ' '.join(random.choice(bag) for _ in range(n))
