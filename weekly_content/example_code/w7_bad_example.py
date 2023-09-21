def fun1(X):
    im = 0
    Xm = X[im]
    
    for i in range(len(X)):
        if X[i] < Xm:
            im = i
            Xm = X[i]

    return im, Xm

L = [6, 3, 7, -3, 1, 5, 2]

def f2(X):

    def f3(i1, i2, X):
        tmp = X[i1]
        X[i1] = X[i2]
        X[i2] = tmp
        return X
    
    for i in range(len(X)):
        im, Xm = fun1(X[i:])
        X = f3(i, im + i, X)

    return X

def f3(i1, i2, X):
    tmp = X[i1]
    X[i1] = X[i2]
    X[i2] = tmp
    return X

print(L)
print(f2(L))
