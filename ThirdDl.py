import numpy as np

a = np.random.randn(4,3)
print(a.shape)
print(a)
b = np.sum(a,axis = 1,keepdims = True)
print(b.shape)

def sigmoid(z):
    s = 1./(1+np.exp(-z))
    return s
print(sigmoid(1))

def propagation(w,b,X,Y):
    m = X.shape[1]

    a = sigmoid(np.dot(w,X)+b)
    cost = -(1./m)*np.sum(Y*np.log(a)+(1-Y)*np.log(1-a))

    dz = a - Y
    dw = (1./m)*np.dot(X,dz.T)
    db = (1./m)*np.sum(dz)
    grads = {
        "dw":dw,
        "db":db
    }
    return grads
# dz2 = a2 - Y
# dw2 = (1./m)*np.dot(dz2,a1.T)
# db2 = (1./m)*np.sum(dz2,axis = 1,keepdims = True)
# dz1 = np.dot(w2.T,dz2)*(1 - np.power(a1,2))