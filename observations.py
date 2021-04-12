from evaluation import Evaluation
from util import *
def run(qrels, doc_IDs_ordered, queries, k, model_name = ' ', bin_size = 20):

    """
    Runs all the observations like distribution of the recall, precision, ndcg..

    Input Arguments:
    qrels : Relevant documents for each queries, we import from here -> "./cranfield/cran_qrels.json"
    doc_IDs_ordered : List of list, output is the list of the retrieved documents for each query
    queries : List, list of all the queries
    k : int, number of top retrieved to be considered. Usually ranges from 1 to 10.
    bin_size : int, number of bins for histogram plot
    """
    df = pd.DataFrame(qrels)
    evaluator = Evaluation()

    # Queries with precision = 1.0
    ones_precision = []

    # Queries with precision = 0.0
    zeros_precision = []

    # Queries with recall = 1.0
    ones_recall = []

    # Queries with recall = 1.0
    zeros_recall = []

    # Precision of each queries
    q_precision = []

    # Recall of each queries
    q_recall = []

    # Fscore of each queries
    q_fscore = []

    for i in range(len(doc_IDs_ordered)):
        true_doc_ids = list(map(int, df[df['query_num'] == str(i+1)]['id'].tolist()))
        precision = evaluator.queryPrecision(doc_IDs_ordered[i], i+1, true_doc_ids, k)
        q_precision.append(precision)
        recall = evaluator.queryRecall(doc_IDs_ordered[i], i+1, true_doc_ids, k)
        q_recall.append(recall)
        fscore = evaluator.queryFscore(doc_IDs_ordered[i], i+1, true_doc_ids, k)
        q_fscore.append(fscore)

        if precision == 1:
            ones_precision.append({'q_id':i+1, 'query': queries[i],
            'rel_docs':true_doc_ids, 'ret_docs':doc_IDs_ordered[i][:10]})
        if precision == 0:
            zeros_precision.append({'q_id':i+1, 'query': queries[i],
            'rel_docs':true_doc_ids, 'ret_docs':doc_IDs_ordered[i][:10]})
            
        if recall == 1:
            ones_recall.append({'q_id':i+1, 'query': queries[i],
            'rel_docs':true_doc_ids, 'ret_docs':doc_IDs_ordered[i][:10]})
        if recall == 0:
            zeros_recall.append({'q_id':i+1, 'query': queries[i],
            'rel_docs':true_doc_ids, 'ret_docs':doc_IDs_ordered[i][:10]})

    # ndcg for each query calculation
    q_ndcg = []
    for i in range(len(doc_IDs_ordered)):
        true_doc_ndcg = df[df['query_num'] == str(i+1)][['position', 'id']]
        ndcg = evaluator.queryNDCG(doc_IDs_ordered[i], i+1, true_doc_ndcg, k)
        q_ndcg.append(list(ndcg)[0])

    # Precision graph
    x_label = 'Precision @ k = ' + str(k)
    plt.figure(figsize = (10,5))
    plt.xlabel(x_label)
    plt.ylabel('Number of Queries')
    plt.title('Precision Distribution for ' + model_name)
    sns.distplot(q_precision, hist=True, kde=True,color = 'darkblue',
                hist_kws={'edgecolor':'black'},kde_kws={'linewidth': 4})
    plt.show()

    # Recall graph
    x_label = 'Recall @ k = ' + str(k)
    plt.figure(figsize = (10,5))
    plt.xlabel(x_label)
    plt.ylabel('Number of Queries')
    plt.title('Recall Distribution for ' + model_name)
    sns.distplot(q_recall, hist=True, kde=True,color = 'darkblue',
                hist_kws={'edgecolor':'black'},kde_kws={'linewidth': 4})
    plt.show()

    # Fscore graph
    x_label = 'Fscore @ k = ' + str(k)
    plt.figure(figsize = (10,5))
    plt.xlabel(x_label)
    plt.ylabel('Number of Queries')
    plt.title('Fscore Distribution for ' + model_name)
    sns.distplot(q_fscore, hist=True, kde=True,color = 'darkblue',
                hist_kws={'edgecolor':'black'},kde_kws={'linewidth': 4})
    plt.show()

    # nDCG graph
    x_label = 'nDCG @ k = ' + str(k)
    plt.figure(figsize = (10,5))
    plt.xlabel(x_label)
    plt.ylabel('Number of Queries')
    plt.title('nDCG Distribution for ' + model_name)
    sns.distplot(q_ndcg, hist=True, kde=True,color = 'darkblue',
                hist_kws={'edgecolor':'black'},kde_kws={'linewidth': 4})
    plt.show()

    return q_precision, q_recall, q_fscore, q_ndcg

def run_comp(q_precision_1, q_precision_2, q_recall_1, q_recall_2, q_fscore_1, q_fscore_2, q_ndcg_1, q_ndcg_2, k, model1_name = ' ', model2_name = ' '):

    # Precision graph for the Model1 and Model2
    
    x_label = 'Precision @ k = ' + str(k)
    plt.figure(figsize = (10,5))
    plt.xlabel(x_label)
    plt.ylabel('Number of Queries')
    plt.title('Precision Distribution for ' + model1_name + ' Vs ' + model2_name)
    sns.distplot(q_precision_1, hist=True, kde=True,color = 'red',
                hist_kws={'edgecolor':'red'},kde_kws={'linewidth': 4}, label = model1_name)
    sns.distplot(q_precision_2, hist=True, kde=True,color = 'darkblue',
                hist_kws={'edgecolor':'black'},kde_kws={'linewidth': 4}, label = model2_name)
    plt.legend()
    plt.show()

    # Recall graph for the Model1 and Model2
    
    x_label = 'Recall @ k = ' + str(k)
    plt.figure(figsize = (10,5))
    plt.xlabel(x_label)
    plt.ylabel('Number of Queries')
    plt.title('Recall Distribution for ' + model1_name + ' Vs ' + model2_name)
    sns.distplot(q_recall_1, hist=True, kde=True,color = 'red',
                hist_kws={'edgecolor':'red'},kde_kws={'linewidth': 4}, label = model1_name)
    sns.distplot(q_recall_2, hist=True, kde=True,color = 'darkblue',
                hist_kws={'edgecolor':'black'},kde_kws={'linewidth': 4}, label = model2_name)
    plt.legend()
    plt.show()

    # Fscore graph for the Model1 and Model2
    
    x_label = 'Fscore @ k = ' + str(k)
    plt.figure(figsize = (10,5))
    plt.xlabel(x_label)
    plt.ylabel('Number of Queries')
    sns.distplot(q_fscore_1, hist=True, kde=True,color = 'red',
                hist_kws={'edgecolor':'red'},kde_kws={'linewidth': 4}, label = model1_name)
    sns.distplot(q_fscore_2, hist=True, kde=True,color = 'darkblue',
                hist_kws={'edgecolor':'black'},kde_kws={'linewidth': 4}, label = model2_name)
    plt.title('Fscore Distribution for ' + model1_name + ' Vs ' + model2_name)
    plt.legend()
    plt.show()

    # Precision graph for the Model1 and Model2
    
    x_label = 'nDCG @ k = ' + str(k)
    plt.figure(figsize = (10,5))
    plt.xlabel(x_label)
    plt.ylabel('Number of Queries')
    sns.distplot(q_ndcg_1, hist=True, kde=True,color = 'red',
                hist_kws={'edgecolor':'red'},kde_kws={'linewidth': 4}, label = model1_name)
    sns.distplot(q_ndcg_2, hist=True, kde=True,color = 'darkblue',
                hist_kws={'edgecolor':'black'},kde_kws={'linewidth': 4}, label = model2_name)
    plt.title('nDCG Distribution for ' + model1_name + ' Vs ' + model2_name)
    plt.legend()
    plt.show()

    return

    




