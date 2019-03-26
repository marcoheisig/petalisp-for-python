import numpy
import cl4py

lisp = cl4py.Lisp(quicklisp=True)
cl = lisp.function('find-package')('CL')
ql = cl.find_package('QL')
ql.quickload('PETALISP')
petalisp = cl.find_package('PETALISP')

class ndarray (cl4py.data.LispWrapper):
    @property
    def shape(self):
        expr = ('cl:mapcar', ('cl:function', 'petalisp:set-size'), ('petalisp:ranges', ('petalisp:shape', self)))
        return tuple(self.lisp.eval( expr ))

    @property
    def dtype(self):
        expr = ('cl4py:dtype-code', ('cl4py:dtype-from-type', ('petalisp:element-type', self)))
        return numpy.dtype(self.lisp.eval( expr ))

    @property
    def ndim(self):
        return petalisp.rank(self)

    def __getitem__(self, key):
        print(key)
        return

    # Comparison Operators

    def __lt__(self, other):
        return alpha(cl.lt, self, other)

    def __le__(self, other):
        return alpha(cl.le, self, other)

    def __eq__(self, other):
        return alpha(cl.sim, self, other)

    def __ne__(self, other):
        return alpha(cl.ne, self, other)

    def __ge__(self, other):
        return alpha(cl.ge, self, other)

    def __gt__(self, other):
        return alpha(cl.gt, self, other)

    def __is__(self, other):
        return alpha(cl.eq, self, other)

    # Numeric Operators

    def __add__(self, other):
        return alpha(cl.add, self, other)

    def __radd__(self, other):
        return alpha(cl.add, other, self)

    def __sub__(self, other):
        return alpha(cl.sub, self, other)

    def __rsub__(self, other):
        return alpha(cl.sub, other, self)

    def __mul__(self, other):
        return alpha(cl.mul, self, other)

    def __rmul__(self, other):
        return alpha(cl.mul, other, self)

    def __matmul__(self, other):
        raise RuntimeError('Not yet implemented.')

    def __rmatmul__(self, other):
        raise RuntimeError('Not yet implemented.')

    def __truediv__(self, other):
        return alpha(cl.div, self, other)

    def __rtruediv__(self, other):
        return alpha(cl.div, other, self)

    def __floordiv__(self, other):
        return alpha(cl.floor, self, other)

    def __rfloordiv__(self, other):
        return alpha(cl.floor, other, self)

    def __mod__(self, other):
        return alpha(cl.mod, self, other)

    def __rmod__(self, other):
        return alpha(cl.mod, other, self)

    def __divmod__(self,other):
        return alpha(2, cl.floor, self, other)

    def __rdivmod__(self,other):
        return alpha(2, cl.floor, other, self)

    def __pow__(self, other):
        return alpha(cl.expt, self, other)

    def __rpow__(self, other):
        return alpha(cl.expt, other, self)

    def __lshift__(self,other):
        return alpha(cl.ash, self, other)

    def __rlshift__(self,other):
        return alpha(cl.ash, other, self)

    def __rshift__(self, other):
        return alpha(cl.ash, self, -other)

    def __rrshift__(self, other):
        return alpha(cl.ash, other, -self)

    def __and__(self, other):
        return alpha(cl.logand, self, other)

    def __rand__(self, other):
        return alpha(cl.logand, other, self)

    def __xor__(self, other):
        return alpha(cl.logxor, self, other)

    def __rxor__(self, other):
        return alpha(cl.logxor, other, self)

    def __or__(self, other):
        return alpha(cl.logior, self, other)

    def __ror__(self, other):
        return alpha(cl.logior, other, self)

    def __neg__(self):
        return alpha(cl.sub, self)

    def __pos__(self):
        return self

    def __abs__(self):
        return alpha(cl.abs, self)

    def __invert__(self):
        return alpha(cl.lognot, self)

    def __concat__(self, other):
        return alpha(cl.concatenate, cl.type_of(self), self, other)

    def __contains__(self, other):
        return alpha(cl.find, self, other, cl4py.Keyword('TEST'), cl.equal)


def the_ndarray(obj):
    obj.__class__ = ndarray
    return obj

def array(object, **args):
    A = numpy.array(object, **args)
    return the_ndarray(petalisp.coerce_to_lazy_array(A))

def compute(*arrays):
    # TODO, only the first result is currently returned.
    return petalisp.compute(*arrays)

def schedule(*arrays):
    petalisp.schedule(*arrays)
    return

def alpha(operator, *arrays):
    return the_ndarray(petalisp.a(operator, *arrays))

def beta(operator, *arrays):
    return the_ndarray(petalisp.b(operator, *arrays))
