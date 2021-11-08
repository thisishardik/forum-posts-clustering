import os

os.system("pip install git+https://github.com/LIAAD/yake")

import pandas as pd
from nltk.tokenize import RegexpTokenizer
import yake

def keywords_yake(sample_posts):
    simple_kwextractor = yake.KeywordExtractor()
    sentences = [] 
    
    for post in sample_posts:
        post_keywords = simple_kwextractor.extract_keywords(post)

        sentence_output = ""
        for word, number in post_keywords:
            sentence_output += word + " "

        sentences.append(sentence_output)
        
    return(sentences)

def tokenizing_after_YAKE(sentences):
    tokenizer = RegexpTokenizer(r'\w+')
    tokenized_data = [w.lower() for w in sentences]
    tokenized_data = [tokenizer.tokenize(i) for i in tokenized_data]
    
    return(tokenized_data)