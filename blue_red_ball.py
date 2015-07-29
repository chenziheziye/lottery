import re
import numpy as np

path = '/Users/chenziheziye/PycharmProjects/test/ssq.txt'

#custom array type
type_key = map(str, range(1,11))
t = [(type_key[i], np.str_, 10) for i in range(1,3)] + [(type_key[i], int) for i in range(3,10)]
hist_array = ['00']*3 + [0]*7
red_cold_dict = dict.fromkeys(range(1,34), 0)
blue_cold_dict = dict.fromkeys(range(1,17), 0)

with open(path, 'rt') as f:
    for line in f:
        raw_val = re.split(r'[,\s\\]', line.rstrip())

        #keep fixed dim of the array for txtfile contain irregular data
        if len(raw_val) > 10:
            raw_val.pop()

        #transform str to int
        raw_val[3:11] = map(int, raw_val[3:11])

        for i in range(1,34):
            if i in raw_val[3:10]:
                red_cold_dict[i] = 0
            else:
                red_cold_dict[i] += 1

        #print raw_val
        nd_array = np.vstack((hist_array, raw_val))
        hist_array = nd_array

for line in hist_array[::-1]:
    print line

print red_cold_dict
print blue_cold_dict


f.close()

































