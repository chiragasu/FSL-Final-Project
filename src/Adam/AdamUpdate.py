import numpy as np;

beta1 = 0.9;
beta2 = 0.999;
eps = 1e-8;


def adamUpdateParams(vW, vb, mW, mb, dW, db, t):
    mW = beta1 * mW + (1 - beta1) * dW;
    mb = beta1 * mb + (1 - beta1) * db;
    vW = beta2 * vW + (1 - beta2) * dW * dW;
    vb = beta2 * vb + (1 - beta2) * db * db;

    # mW_hat = mW / (1. - beta1 ** (t));
    # mb_hat = mb / (1. - beta1 ** (t));
    # vW_hat = vW / (1. - beta2 ** (t));
    # vb_hat = vb / (1. - beta2 ** (t));
    #
    # newUW = mW_hat / (np.sqrt(vW_hat) + eps);
    # newUb = mb_hat / (np.sqrt(vb_hat) + eps);

    newUW = mW / (np.sqrt(vW) + eps);
    newUb = mb / (np.sqrt(vb) + eps);
    return newUW, newUb, mW, mb, vW, vb;
