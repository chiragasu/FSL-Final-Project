import numpy as np;

beta = 0.9;
eps = 1e-8;
def rmsPropUpdateParams(vW, vb, dW, db):
    vW = beta * vW + (1 - beta) * dW * dW;
    vb = beta * vb + (1 - beta) * db * db;
    newUW = dW / (np.sqrt(vW) + eps);
    newUb = db / (np.sqrt(vb) + eps);
    return newUW, newUb, vW, vb;