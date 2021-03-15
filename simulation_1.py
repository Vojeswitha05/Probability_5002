import numpy as np
from scipy.stats import bernoulli

sample_size=100000

prob_A=5/26
prob_B=5/13
prob_AgivenB=2/5

#Simulations using Bernoulli r.v.
sample_A= bernoulli.rvs(size= sample_size, p = prob_A)
sample_B= bernoulli.rvs(size= sample_size, p = prob_B)
sample_AgivenB= bernoulli.rvs(size= sample_size, p = prob_AgivenB)

A_nonzero = np.nonzero(sample_A == 1)
B_nonzero = np.nonzero(sample_B == 1)
AgivenB_nonzero = np.nonzero(sample_AgivenB == 1)

n_A= np.size(A_nonzero)
n_B= np.size(B_nonzero)
n_AgivenB= np.size(AgivenB_nonzero)

calc_prob_A=n_A/sample_size
calc_prob_B=n_B/sample_size
calc_prob_AgivenB=n_AgivenB/sample_size

#calculating P(A intersection B):
calc_prob_AB= calc_prob_AgivenB*calc_prob_B
prob_AB = prob_AgivenB*prob_B

#calculating P(A union B)
calc_prob_AorB= calc_prob_A + calc_prob_B - calc_prob_AB
prob_AorB = prob_A+prob_B-prob_AB
print("P(A+B) Simulated value  = ", calc_prob_AorB, " while theoretical value = ", prob_AorB)
