import numpy as np
from math import sqrt,log
import matplotlib.pyplot as plt

def amsasimov(s,b):
        
        if b<=0 or s<=0:
            return 0
        try:
            return sqrt(2*((s+b)*log(1+float(s)/b)-s))
        except ValueError:
            print 1+float(s)/b
            print (2*((s+b)*log(1+float(s)/b)-s))
        #return s/sqrt(s+b)

def amsasimovError(s, ds,b, db, z):
    if z==0:
        return 0
    e = sqrt( (ds*log(float(s)/b + 1))**2 + (db*((log(float(s)/b +1))-s/b))**2 )/z
    return e

def purity(s,b):
    if (s+b) ==0:
        return 0
    return (s*1.0)/(s+b)
def purityError(s,ds, b, db):
    if (s+b) ==0:
        return 0
    e = sqrt((ds*b)**2 +(db*s)**2)/((s+b)**2)
    return e
'''     
def bkgRej( b, total):
    return 1.0 - float(b)/total
    
def sigEff(s, total):
    return s/total

def bkgRejError( b,db, total, dtotal):
    return (db*(1.0/total))**2+ (dtotal*(float(b)/(total**2)))**2
    
def sigEffError(s,ds, total, dtotal):
    return (ds*(1.0/total))**2+ (dtotal*(float(s)/(total**2)))**2
'''

def compare_train_test(y_pred_train, y_train, y_pred, y_test, high_low=(0,1), bins=30):
    plt.hist(y_pred_train[y_train == 1],
                 color='r', alpha=0.5, range=high_low, bins=bins,
                 histtype='stepfilled', normed=True,
                 label='S (train)') # alpha is transparancy
    plt.hist(y_pred_train[y_train == 0],
                 color='b', alpha=0.5, range=high_low, bins=bins,
                 histtype='stepfilled', normed=True,
                 label='B (train)')

    hist, bins = np.histogram(y_pred[y_test == 1],
                                  bins=bins, range=high_low, normed=True)
    scale = len(y_pred[y_test == 1]) / sum(hist)
    err = np.sqrt(hist * scale) / scale

    #width = (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.errorbar(center, hist, yerr=err, fmt='o', c='r', label='S (test)')

    hist, bins = np.histogram(y_pred[y_test == 0],
                                  bins=bins, range=high_low, normed=True)
    scale = len(y_pred[y_test == 0]) / sum(hist)
    err = np.sqrt(hist * scale) / scale

    #width = (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.errorbar(center, hist, yerr=err, fmt='o', c='b', label='B (test)')
    plt.xlabel("NN scores")
    plt.ylabel("Arbitrary units")
    plt.legend(loc='best')