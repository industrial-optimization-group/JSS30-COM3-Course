# https://blog.dominodatalab.com/fitting-gaussian-process-models-python/
# I modified this code for my trinket to show a simple Kriging/Gaussian Process example to play with
import numpy as np
# (c) Michael Emmerich, Leiden University
def exponential_cov(x, y, params):
  return params[0] * np.exp( -0.8 * params[1] * np.subtract.outer(x, y)**2)
def euclid(x,y):
  np.subtract.outer(x, y)

def conditional(x_new, x, y, params):
  B = exponential_cov(x_new, x, params)
  C = exponential_cov(x, x, params)
  A = exponential_cov(x_new, x_new, params)
  mu = np.linalg.inv(C).dot(B.T).T.dot(y)
  sigma = A - B.dot(np.linalg.inv(C).dot(B.T))
  return(mu.squeeze(), sigma.squeeze())

def predict(x, data, kernel, params, sigma, t):
  k = [kernel(x, y, params) for y in data]
  Sinv = np.linalg.inv(sigma)
  y_pred = np.dot(k, Sinv).dot(t)
  sigma_new = kernel(x, x, params) - np.dot(k, Sinv).dot(k)
  return y_pred, sigma_new

def predict_lipschitz(x,data,constant,sigma,t):
  k = [kernel(x, y, params) for y in data]

import matplotlib.pylab as plt
###############################################
# Enter the evaluated data points here        #
###############################################
x=[0.,0.5,1,1.3]
y = [1.3,0.0,0.7,1.0]

# Here starts the Gaussian Process (GP) computation
θ = [1, 10]
σ_0 = exponential_cov(0, 0, θ)
σ_1 = exponential_cov(x, x, θ)
x_pred = np.linspace(-0.5, 1.5, 100)
y_up = np.linspace(-0.5, 1.5, 100)
y_low = np.linspace(-0.5, 1.5, 100)

predictions = [predict(i, x, exponential_cov, θ, σ_1, y) for i in x_pred]
y_pred, sigmas = np.transpose(predictions)
plt.errorbar(x_pred, y_pred, yerr=sigmas, capsize=0)
plt.plot(x, y, "ro")

# Add title and axis names
plt.title('Lipschitz & Gaussian Process Interpolation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

# Here starts the Lipschitzian bound computation (red and green lines).
# L is Lipschitz Constant: maximal change rate of function
L=4
for i in range(len(x_pred)):
  xnew = x_pred[i]
  d=[L*np.abs(z-xnew) for z in x]
  lowenv=max(np.subtract(y,d))
  upenv=min(np.add(y,d))
  y_pred[i] = (upenv+lowenv)/2
  y_up[i]=upenv;
  y_low[i]=lowenv;

plt.plot(x_pred, y_pred)
plt.plot(x_pred, y_low)
plt.plot(x_pred, y_up)
plt.show();

