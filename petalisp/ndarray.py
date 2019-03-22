import numpy
import cl4py

lisp = cl4py.Lisp(quicklisp=True)
cl = lisp.function('find-package')('CL')
ql = cl.find_package('QL')
petalisp = ql.quickload('PETALISP')

class ndarray (cl4py.data.UnknownLispObject):
    pass

def array(object, **args):
    A = numpy.array(object, **args)
    print(A)
    return ndarray(lisp, petalisp.coerce_to_lazy_array(A))
