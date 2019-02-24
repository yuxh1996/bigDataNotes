import sys
import time

for line in sys.stdin:
    time.sleep(1000)
    ss = line.strip().split(' ')
    for word in ss:
        print '\t'.join([word.strip(), '1'])
