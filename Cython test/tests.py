
import test
import test2
import time


number = int(input('enter number: '))

start = time.time()
test.test(number)

end =  time.time()

py_time = end - start
print("Python time = {}".format(py_time))

start = time.time()
test2.test2(number)

end =  time.time()

cy_time = end - start
print("Cython time = {}".format(cy_time))
print("Speedup = {}".format(py_time / cy_time))