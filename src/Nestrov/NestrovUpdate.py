



beta =0.9;

def NestrovUpdateParams(vW, vb, dW, db):
    vW = beta * vW + (1 - beta) * dW;
    vb = beta * vb + (1 - beta) * db;
    return vW, vb;