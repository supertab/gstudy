import numpy as np
step = 2e-7
end_time = 162
data  =  np.arange(0, end_time*step, step)
# data = [float(x) for x in data]
data_str = ''
for i in data:
    data_str = data_str + str(i) + '\n'

with open('step.txt', 'w') as f:
    f.write(data_str)
