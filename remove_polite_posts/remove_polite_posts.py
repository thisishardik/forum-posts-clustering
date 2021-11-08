import numpy as np
import pandas as pd
from flashtext.keyword import KeywordProcessor
import string

def polite_post_index(forum_posts):
    polite_indexes = []
    
    stop_word_list = ["no problem", "thanks", "thx", "thank", "great",
                      "nice", "interesting", "awesome", "perfect", 
                      "amazing", "well done", "good job"]

    keyword_processor = KeywordProcessor()
    keyword_processor.add_keywords_from_list(stop_word_list)

    for i,post in enumerate(forum_posts):
        post = post.lower().translate(str.maketrans({a:None for a in string.punctuation}))
        
        if len(post) < 100:
            keywords_found = keyword_processor.extract_keywords(post.lower(), span_info=True)
            if keywords_found:
                polite_indexes.append(i)

    return(polite_indexes)