#.\python-exercises\zigzag.py
'''
    ********
   ********
  ********
 ********
********
 ********
  ********
   ********
    ********
'''
import time,sys
margin_count = 4
margin = margin_count*' '
length = '*'*8
iterate = 1
try:
    while True:# iterate 9 times for height
        time.sleep(0.1)
        margin = margin_count*' '
        print(margin+length)
        if margin_count == 0 or margin_count == 4:
            iterate *= -1
        margin_count += iterate
except KeyboardInterrupt:
    sys.exit()

