import time
timplul_actual=time.time()
print(timplul_actual)

time.sleep(4)

noul_timp=time.time()

delta=noul_timp-timplul_actual
print(delta)