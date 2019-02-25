




# correlation analysis for categorical variables 
# link : https://stackoverflow.com/questions/46498455/categorical-features-correlation/46498792#46498792

import pandas as pd
import numpy as np
import scipy.stats as ss
import seaborn as sns

tips = sns.load_dataset("tips")

tips["total_bill_cut"] = pd.cut(tips["total_bill"],
                                np.arange(0, 55, 5),
                                include_lowest=True,
                                right=False)

def cramers_v(confusion_matrix):
    """ calculate Cramers V statistic for categorial-categorial association.
        uses correction from Bergsma and Wicher,
        Journal of the Korean Statistical Society 42 (2013): 323-328
    """
    chi2 = ss.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min((kcorr-1), (rcorr-1)))

confusion_matrix = pd.crosstab(tips["day"], tips["time"]).as_matrix()
cramers_v(confusion_matrix)
# Out[10]: 0.93866193407222209

confusion_matrix = pd.crosstab(tips["total_bill_cut"], tips["time"]).as_matrix()
cramers_v(confusion_matrix)
# Out[24]: 0.16498707494988371
