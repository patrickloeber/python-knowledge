# pip install tqdm
from tqdm import tqdm, trange
import time

# iterable based
for i in tqdm([1, 2, 3, 4, 5]):
    time.sleep(0.2)

print('done')

#  special optimised instance of tqdm(range(i))
for i in trange(10):
    time.sleep(0.1)

print('done')

# manual: use a with statement
# we can provide the optional 'total' parameter
with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.1)
        pbar.update(10)

print('done')

# manual: assign to a variable
# dont forget to call close() at the end
pbar = tqdm(total=100)
for i in range(10):
    time.sleep(0.1)
    pbar.update(10)
pbar.close()

print('done')