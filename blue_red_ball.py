import os
import re
import numpy as np

path = '/Users/chenziheziye/PycharmProjects/test/ssq.txt'

hist_array = []
num_time_array = []
red_cold_dict = dict.fromkeys(range(1,34), 0)
blue_cold_dict = dict.fromkeys(range(1,17), 0)

with open(path, 'rt') as f:

    hl = []
    nl = []
    for line in f:
        raw_val = re.split(r'[,\s\\]', line.rstrip())

        #keep fixed dim of the array for txtfile contain irregular data
        if len(raw_val) > 10:
            raw_val.pop()

        #transform str to int
        raw_val[3:11] = map(int, raw_val[3:11])

        hl.append(raw_val[3:11])
        nl.append(raw_val[0:3])
f.close()

hist_array = np.array(hl)
num_time_array = np.array(nl)
hist_array.shape = (len(hl), 7)
num_time_array.shape = (len(hl), 3)


for line in hist_array[::-1, 0:6]:

    for i in red_cold_dict:
        red_cold_dict[i] += 1
    for tag in line:
        red_cold_dict[tag] = 0

for tag in hist_array[::-1, -1]:

    for i in blue_cold_dict:
        blue_cold_dict[i] += 1
    blue_cold_dict[tag] = 0


print red_cold_dict
print blue_cold_dict




































