import math;

beta = 0.9;
def polyUpdateParams(mW, mb, dW, db, t):
    mW = beta * mW + (1 - beta) * dW;
    mb = beta * mb + (1 - beta) * db;
    # betaPower = math.pow(beta, t);
    # mW = mW/(1-betaPower);
    # mb = mb / (1 - betaPower);
    return mW, mb;
