import numpy as np


x = np.random.uniform(0, 100, 20)



rand_var =  np.random.normal(-1, 1, 20)
y = (50*x) + 22 + rand_var
# new_y = y[:]
# new_y[9] = y[9]*2
print(np.round(y))
# print(np.round(new_y))


def estimate_coef(x, y):
    n = np.size(x)
    
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    
    SS_xy = np.sum(y*x) - n*mean_y*mean_x
    SS_xx = np.sum(x*x) - n*mean_x*mean_x
    
    b_1 = SS_xy / SS_xx
    b_0 = mean_y - b_1*mean_x
    
    return (np.round(b_0), np.round(b_1))

print(estimate_coef(x, y))
