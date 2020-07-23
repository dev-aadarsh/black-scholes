import numpy
from scipy.stats import norm

def euro_call(S, K, T, r, y, sigma):
  a = (np.log(S / K) + (r - y) * T) / (sigma * np.sqrt(T))
  b = (sigma * np.sqrt(T)) / 2
  
  x_plus = a + b
  x_minus = a - b

  S_term = S * np.exp(-y * T) * norm.cdf(x_plus)
  K_term = K * np.exp(-r * T) * norm.cdf(x_minus)

  call_price = S_term - K_term
  return call_price

def euro_put(S, K, T, r, y, sigma):
  a = (np.log(S / K) + (r - y) * T) / (sigma * np.sqrt(T))
  b = (sigma * np.sqrt(T)) / 2
  
  x_plus = a + b
  x_minus = a - b

  S_term = S * np.exp(-y * T) * norm.cdf(-x_plus)
  K_term = K * np.exp(-r * T) * norm.cdf(-x_minus)

  put_price = K_term - S_term
  return put_price
