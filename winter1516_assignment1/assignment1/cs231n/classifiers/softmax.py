import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  
  num_train = X.shape[0]
  num_class = W.shape[1]
  
  sco = X.dot(W)
  s_sco = sco- np.amax(sco, axis = 1).reshape((-1,1))
  exp_s_sco = np.exp(s_sco)
  exp_s_sco_div = exp_s_sco / np.sum(exp_s_sco, axis = 1).reshape((-1,1))
  for i in range(num_train):
    loss -= np.log( exp_s_sco_div[i, y[i]])
    
  loss += reg * np.sum(W * W) / 2
  loss /= num_train

  
  for i in range(num_train):
    dW[:, y[i]] -= X[i].T
  
  essd_3d = exp_s_sco_div.reshape((num_train, 1, num_class))
  X_3d = X.reshape((X.shape[0], X.shape[1], 1))
  temp = X_3d * essd_3d
  dW += np.sum( temp, axis = 0)
  
  dW += reg * W
  dW /= num_train
  
  
  
  
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]
  num_class = W.shape[1]
  
  sco = X.dot(W)
  s_sco = sco- np.amax(sco, axis = 1).reshape((-1,1))
  exp_s_sco = np.exp(s_sco)
  exp_s_sco_div = exp_s_sco / np.sum(exp_s_sco, axis = 1).reshape((-1,1))
  for i in range(num_train):
    loss -= np.log( exp_s_sco_div[i, y[i]])
    
  loss += reg * np.sum(W * W) / 2
  loss /= num_train

  
  for i in range(num_train):
    dW[:, y[i]] -= X[i].T
  
  essd_3d = exp_s_sco_div.reshape((num_train, 1, num_class))
  X_3d = X.reshape((X.shape[0], X.shape[1], 1))
  temp = X_3d * essd_3d
  dW += np.sum( temp, axis = 0)
  
  dW += reg * W
  dW /= num_train
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

