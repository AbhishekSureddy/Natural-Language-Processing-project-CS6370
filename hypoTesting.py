import numpy as np
from scipy.special import stdtr

def hypothesis_test(q1, q2):

    """
    Two Sample t-test
    Inputs:
    q1 : List, sample 1 values
    q2 : List, sample 2 values

    Output:
    tf : float, t-value of hypothesis testing
    pf : float, p-value
    """
    a = np.array(q1)
    b = np.array(q2)
    abar = a.mean()
    avar = a.var(ddof=1)
    na = a.size
    adof = na - 1

    bbar = b.mean()
    bvar = b.var(ddof=1)
    nb = b.size
    bdof = nb - 1

    # Use the formulas directly.
    tf = (abar - bbar) / np.sqrt(avar/na + bvar/nb)
    dof = (avar/na + bvar/nb)**2 / (avar**2/(na**2*adof) + bvar**2/(nb**2*bdof))
    pf = 2*stdtr(dof, -np.abs(tf))

    print("formula: t = %g  p = %g" % (tf, pf))
    # return tf, pf