# -*- encoding: utf-8 -*-

"""
>>> 1 + 1
2

>>> 1 + AccountingNone
1

>>> AccountingNone + 1
1

>>> AccountingNone + None
AccountingNone

>>> +AccountingNone
AccountingNone

>>> -AccountingNone
AccountingNone

>>> -(AccountingNone)
AccountingNone

>>> AccountingNone - 1
-1
>>> 1 - AccountingNone
1
>>> AccountingNone - None
AccountingNone

>>> AccountingNone / 2
AccountingNone

>>> 2 / AccountingNone
Traceback (most recent call last):
 ...
ZeroDivisionError

>>> AccountingNone // 2
AccountingNone

>>> 2 // AccountingNone
Traceback (most recent call last):
 ...
ZeroDivisionError

>>> AccountingNone * 2
AccountingNone

>>> 2 * AccountingNone
AccountingNone

"""

class AccountingNoneType(object):

    def __add__(self, other):
        """
        Overload of the + operator
        """
        if other is None:
            return AccountingNone
        return other
    
    __radd__ = __add__
    
    def __sub__(self, other):
        """
        Overload of the - operator
        """
        if other is None:
            return AccountingNone
        return -other

    def __rsub__(self, other):
        """
        Overload of the reverse - operator
        """
        if other is None:
            return AccountingNone
        return other

    def __iadd__(self, other):
        """
        Overload of the += operator
        """
        if other is None:
            return AccountingNone
        return other

    def __isub__(self, other):
        """
        Overload of the -= operator
        """
        if other is None:
            return AccountingNone
        return -other
    
    def __pos__(self):
        """
        Overload of the unary + operator
        """
        return self
    
    def __neg__(self):
        """
        Overload of unary - operatpr
        """
        return self
    
    def __repr__(self):
        """
        Overload of repr
        """
        return 'AccountingNone'

    def __floordiv__(self, other):
        """
        Overload of the // operator
        """
        return self

    def __rfloordiv__(self, other):
        """
        Overload of the reverse + operator
        """
        raise ZeroDivisionError

    def __truediv__(self, other):
        """
        Overload of the / operator
        """
        return self

    def __rtruediv__(self, other):
        """
        Overload of the reverse + operator
        """
        raise ZeroDivisionError

    def __mul__(self, other):
        """
        Overload of the * operator
        """
        return AccountingNone

    def __rmul__(self, other):
        """
        Overload of the reverse * operator
        """
        return AccountingNone

    def __str__(self):
        """
        Overload of str
        """
        return ''
    
    def __unicode__(self):
        """
        Overload of unicode
        """
        return ''


AccountingNone = AccountingNoneType()


if __name__ == '__main__':
    import doctest
    doctest.testmod()