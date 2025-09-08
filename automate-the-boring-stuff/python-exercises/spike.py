#.\python-exercises\spike.py 
'''
-
----
---------
----------------
-------------------------
------------------------------------
-------------------------------------------------
----------------------------------------------------------------
-------------------------------------------------
------------------------------------
-------------------------
----------------
---------
----
'''
import time,sys
spike_count = 1
spike = '-' * spike_count
multiply = 3
try:
    while True:
        time.sleep(0.1)
        spike = '-' * spike_count
        print(spike)
        if spike_count >= 20 or spike_count <= 0:
            multiply *= -1
            spike_count += 1
        spike_count += multiply
except KeyboardInterrupt: sys.exit()