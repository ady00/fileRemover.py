import os
import time

current_time = time.time()

for f in os.listdir():
    creation_time = os.path.getctime(f)
    if (current_time - creation_time) // (24 * 3600) >= 30:
        os.unlink(f)
        print('{} removed'.format(f))
