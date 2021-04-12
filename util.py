# Add your import statements here
import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import seaborn as sns


# Add any utility functions here

def build_word_index(docs,doc_ids):
    corpora = [] # a list of words
    #word_map = {}
    for doc in docs:
        for sent in doc:
            for word in sent:
                corpora.append(word)
    corpora = set(corpora)  # unique words
    word_map = {word : idx for idx,word in enumerate(set(corpora),0)} # for assigning a unique label to each word

    return word_map
	
