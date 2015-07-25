import re

path = '/Users/chenziheziye/Documents/Study_inbox/study_in_BJ/s.txt'
with open(path, 'rt') as f:
	for line in f:
		raw_val = re.split(r'[,\s\\]', line)
		print raw_val
		
f.close()
