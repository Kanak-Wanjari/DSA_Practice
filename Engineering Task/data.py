import  numpy as np

np.random.seed(42)

X = np.random.rand(100, 1)
y = 2*X+1+0.1*np.random.randn(100, 1)

W = np.random.randn(1, 1)
b = np.zeros((1,))

def forward(X,W,b):
    return X @ W + b

def mse_loss(y_pred, y_true):
    return np.mean((y_pred - y_true)**2)

def backward(X,y,y_pred):
    n = len(X)
    dW = (2/n)*X.T @ (y_pred)
    db = (2/n)*np.sum(y_pred)
    return dW, db

lr = 0.1
epochs = 1000

for epoch in range(epochs):
    y_pred = forward(X,W,b)

    loss = mse_loss(y_pred,y)

    dW, db = backward(X, y, y_pred)

    W -= lr * dW
    b -= lr *db

    if epoch % 100 == 0:
        print(f"Epoch {epoch} | Loss:{loss:.4f}")

print("Learned W:", W)
print("Learned b:", b)