import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	X = np.array(features)
	y = np.array(labels)
	w = np.array(weights)

	z = np.dot(X,w) + bias

	predictions = 1/(1+np.exp(-z))
	mse = np.mean((predictions - y)**2)

	return np.round(predictions,4).tolist(),round(mse,4)
