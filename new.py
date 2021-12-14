from math import sqrt
import numpy as np 
import random

def find_sd(lst, lst_mean):
    total_a = sum([(abs(x-lst_mean))**2 for x in lst])
    divide_by_n = total_a/len(lst)
    sqr_a = divide_by_n ** 0.5
    return sqr_a

def find_normal_dist(lst, lst_mean, lst_sd):
    my_pi = 3.14159
    my_e = 2.71828
    sqrt_2pi = (2 * my_pi) **0.5
    part1 = 1/(lst_sd* sqrt_2pi)
    
    
    # y = [part1* (my_e **(-0.5*(((x - lst_mean)/lst_sd)**2))) for x in lst]
    y = [(my_e **(((-0.5*(x**2)))))/sqrt_2pi for x in lst]
    return y


##Second attempt
x2 = [random.uniform(0.0,100.0) for x in range(20) ]
rand_vals = [random.uniform(-1.0,1.0) for x in range(20) ]
rand_vals_mean = sum(rand_vals)/20
rand_vals_sd =  find_sd(rand_vals, rand_vals_mean)

rand_normal_distribute = find_normal_dist(rand_vals,rand_vals_mean,rand_vals_sd)
print("rand_normal_distribute: ",np.round(rand_normal_distribute,2))

y2 = [(50*i)+ 22 +j for i,j in zip(x2,rand_normal_distribute) ]
# print("y2: ", (np.round(y2, 2))
# print("x2: ", (np.round(x2, 2))
print("y2: ", y2)
print("x2: ", x2)