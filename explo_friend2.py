from math import sqrt
import numpy as np 
import random

def find_sd(lst, lst_mean):
    total_a = sum([(abs(x-lst_mean))**2 for x in lst])
    divide_by_n = total_a/len(lst)
    sqr_a = divide_by_n ** 0.5
    print("sqr a : "+str(sqr_a))
    print("using numpy: "+str(np.std(lst)))
    return sqr_a
def find_normal_dist(lst, lst_mean, lst_sd):
    my_pi = 3.14159
    my_e = 2.71828
    sqrt_2pi = (2 * my_pi) **0.5
    # two_sigma_sqrd = (lst_sd**2)
    part1 = 1/(lst_sd* sqrt_2pi)
    
    
    # y = [part1* (my_e **(-0.5*(((x - lst_mean)/lst_sd)**2))) for x in lst]
    y = [(my_e **(((-0.5*(x**2)))))/sqrt_2pi for x in lst]
    ##The above formular was adobted from resources below
    #https://www.numerade.com/ask/question/exercise-14-use-matplotlib-in-python-to-create-plots-showing-how-fy-y-muu-verges-to-the-normal-distribution-as-increases-your-plots-should-contain-an-outline-of-the-normal-distribution-like--10295/
    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html

    print("y generated : "+ str(y))
    # print("y from numpy: "+str(np.random.normal(lst_mean,lst_sd,20)))
    return y


##Second attempt
x2 = [random.uniform(0.0,100.0) for x in range(20) ]
rand_vals = [random.uniform(-1.0,1.0) for x in range(20) ]
rand_vals_mean = sum(rand_vals)/20
rand_vals_sd =  find_sd(rand_vals, rand_vals_mean)

rand_normal_distribute = find_normal_dist(rand_vals,rand_vals_mean,rand_vals_sd)

y2 = [(50*i)+ 22 +j for i,j in zip(x2,rand_normal_distribute) ]

# print("x of length "+ str(len(x))+" = "+str(x))
# print("++++++++++++++++++++++++++++++++++")
# print("x2  = "+str(x2))
# print("rand_vals = "+str(rand_vals))
##COmparison of values 
print("y : for x2"+ str(y2))

print("y : for x"+ str(y))
