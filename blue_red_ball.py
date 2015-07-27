import re
import numpy as np

path = '/Users/chenziheziye/PycharmProjects/test/ssq.txt'
hist_array = ['00']*10

with open(path, 'rt') as f:
    for line in f:
        raw_val = re.split(r'[,\s\\]', line.rstrip())

        if len(raw_val) > 10:
            raw_val.pop()

        print raw_val
        nd_array = np.vstack((hist_array, raw_val))
        hist_array = nd_array

        #each line refers to a priority list for red and blue num

f.close()
