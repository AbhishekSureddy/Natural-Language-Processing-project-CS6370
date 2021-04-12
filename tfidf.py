# works for docs only
import numpy as np
def TF_IDF(docs, doc_ids, word_map, normalize = True, is_queries= False):
    """
    Input Arguments:
    docs : list of list of lists 
    doc_ids: list, there are around 1400 documents in the corpus, so length of doc_ids is 1400
    word_map:
    is_queries : Bool, True if we are passing queries
    normalize: Bool, True means it will normalize the features in the tfidf representation of documents
    
    Output Argument:
    return :: tf_idf representation of documents (numpy array)
    """
    m = len(set(word_map))  # number of words
    n = len(doc_ids)       # number of docs
    
    tf = np.zeros((m,n)) # initialising
    # filling the tf vector part
    for i in range(n):
        for sent in docs[i]:
            for word in sent:
                try:
                    tf[word_map[word]][doc_ids[i]-1] += 1
                except:
                    #print(word)
                    pass
    
    idf = tf!=0
    idf = np.sum(idf, axis = 1)
    idf = np.log10(n/idf).reshape(-1,1)
    tf_idf = idf*tf
    if(is_queries):
        tf_idf = tf
    if (normalize):
        epsilon = 1e-4
        return tf_idf/ (np.linalg.norm(tf_idf, axis = 0)+epsilon)
    
    return tf_idf