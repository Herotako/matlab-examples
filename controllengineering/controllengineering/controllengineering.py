"""Main module."""
# coding: utf-8

import numpy as np

def Hurwitz(dimension_sequence: list) :
    coef = np.array(dimension_sequence, dtype='float64')
    """フルビッツの安定判別法"""

    N = len(coef)-1
    H = np.zeros((N,N))

    evens = coef[1::2]
    odds = coef[0::2]

    evens = np.pad(evens,[0,N-len(evens)],'constant',constant_values=0)
    odds = np.pad(odds,[0,N-len(odds)],'constant',constant_values=0)

    for i in range(0,N):
        if i%2==0:
            H[i,i//2:] = evens[:N-i//2]
        else:
            H[i,i//2:] = odds[:N-i//2]

    print('H=\n',H)

    for n in range(1,N+1):
        D =H[:n,:n]
        det = np.linalg.det(D)
        print('D=\n',D)
        print('det=',det)

    return 0