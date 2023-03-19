import cython

def test2(int n):
   cdef int i
   cdef double a=0.0, b=1.0
   for i in range(n):
      a, b = a + b, a
   print (a)


