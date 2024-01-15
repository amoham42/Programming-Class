import mpmath
import time

mpmath.mp.dps = 1000  # set number of decimal places

start_time = time.time()

pi = mpmath.pi

end_time = time.time()
execution_time = end_time - start_time

print(f"Pi to 1000 digits:\n{pi}")
print(f"Time taken: {execution_time} seconds")
