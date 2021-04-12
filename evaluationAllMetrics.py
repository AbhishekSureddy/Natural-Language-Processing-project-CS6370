from util import *


from evaluation import Evaluation
import matplotlib.pyplot as plt
evaluator = Evaluation()
def Evaluation_metrics(doc_IDs_ordered, query_ids, qrels, n_comp, op_folder = './',save_results = 2, verbose = 1, title_name = " "):
    """
    doc_IDs_ordered: List, the order of the retrieved docs by our model

    query_ids: List, values from 1 to 225. [1,2,3,..., 225]

    qrels: List, relevant documents for each query(/cranfield/cran_qrels.json)

    n_comp: integer, this argument used by the LSA model. Number of components considered.

    op_folder: Output Folder path, this is the folder path to save the results

    save_results : 0    ===> Output only the results table, not the plots
                 : 1    ===> Plots + Table Results
    title_name: str, title name of the plot(applicable when save_results = 1)

    """
    precisions, recalls, fscores, MAPs, nDCGs = [], [], [], [], []
    for k in range(1,11):
        precision = evaluator.meanPrecision(
            doc_IDs_ordered, query_ids, qrels, k)
        precisions.append(precision)
        recall = evaluator.meanRecall(
            doc_IDs_ordered, query_ids, qrels, k)
        recalls.append(recall)
        fscore = evaluator.meanFscore(
            doc_IDs_ordered, query_ids, qrels, k)
        fscores.append(fscore)

        MAP = evaluator.meanAveragePrecision(
            doc_IDs_ordered, query_ids, qrels, k)
        MAPs.append(MAP)
        nDCG = evaluator.meanNDCG(
            doc_IDs_ordered, query_ids, qrels, k)
        nDCGs.append(nDCG)
        if (verbose):
            print("Precision, Recall and F-score @ " +  
                str(k) + " : " + str(precision) + ", " + str(recall) + 
                ", " + str(fscore))
            print("MAP, nDCG @ " +  
                str(k) + " : " + str(MAP) + ", " + str(nDCG))
        # if (save_results > 0):
        # # saving the results
        #     with open(op_folder+'Results/LSA_'+str(n_comp)+'.txt', 'a') as f:
        #         f.write(str(k) + " , " + str(precision) + ", " + str(recall) + 
        #                 ", " + str(fscore)+", "+str(MAP) + ", " + str(nDCG)+'\n')
        #     with open(op_folder+'Results/metrics_'+str(k)+'.txt', 'a') as f:
        #         f.write(str(n_comp) + " , " + str(precision) + ", " + str(recall) + 
        #                 ", " + str(fscore)+", "+str(MAP) + ", " + str(nDCG)+'\n')
            
    # Plot the metrics and save plot 
    if (save_results == 1):
        plt.figure(figsize=(10,5))
        plt.plot(range(1, 11), precisions, label="Precision")
        plt.plot(range(1, 11), recalls, label="Recall")
        plt.plot(range(1, 11), fscores, label="F-Score")
        plt.plot(range(1, 11), MAPs, label="MAP")
        plt.plot(range(1, 11), nDCGs, label="nDCG")
        plt.legend()
        plt.title(title_name)
        plt.xlabel("k")
        #plt.savefig(op_folder + "Plots/LSA_"+str(n_comp)+".png")
    return
 