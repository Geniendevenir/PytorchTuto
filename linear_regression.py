import torch
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import os


def foward(x, w):
	return x * w

def loss(y, y_pred):
	return ((y - y_pred) **2).mean()

def update_gradient(w, learning_rate):
	w -= learning_rate * w.grad

def linear_regression():
	X = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8], dtype=torch.float32)
	Y = torch.tensor([2, 4, 6, 8, 10, 12, 14, 16], dtype=torch.float32)

	w = torch.tensor(0.0, dtype=torch.float32, requires_grad=True)

	X_test = 5.0

	learning_rate = 0.01
	n_epochs = 100	

	for epoch in range(n_epochs):
		y_pred = foward(X, w)

		l = loss(Y, y_pred)

		l.backward()

		with torch.no_grad():
			update_gradient(w, learning_rate)			

		w.grad.zero_()

	print(f'Prediction after Training for f({X_test}) = {foward(X_test, w)}')

if __name__ == "__main__":
    linear_regression()
