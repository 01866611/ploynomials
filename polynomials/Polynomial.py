# from email import policy
# from zlib import DEF_BUF_SIZE
from numbers import Number


class Polynomial:
    """定义poly 输入参数为各项的系数构成的tuple,  有加减乘除的定义."""

    def __init__(self, coefs):
        """."""
        self.coefficients = coefs

    def degree(self):
        """Degree."""
        return len(self.coefficients)-1

    def __str__(self):
        """Printing function."""
        coefs = self.coefficients
        terms = []
        # Degree 0 and 1 terms conventionally have different representation.
        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() > 0 and coefs[1]:
            terms.append(f"{'' if coefs[1] ==1 else coefs[1]}x")
        # Remaining terms look like cx^d, though factors of 1 are dropped.
        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]
        # Sum polynomial terms from high to low exponent.
        return " + ".join(reversed(terms)) or "0"

    def __eq__(self, other):
        """Check whether one polynomial equals to this poly."""
        return self.coefficients == other.coefficients

    def __add__(self, other):
        """Addition."""
        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree())+1
            coefs = tuple(a+b for a, b in
                          zip(self.coefficients, other.coefficients))
            coefs += self.coefficients[common:]+other.coefficients[common:]
            return Polynomial(coefs)
        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,) +
                              self.coefficients[1:])
        else:
            return NotImplemented

    def __radd__(self, other):
        """."""
        return self + other

# 注意区分polynomials\polynomials\Polynomial.py 还有 class Polynomial

# total_folder_name \poly_folder_name\module_name. 
# 还有 class Polynomial是在module里面的class

# ###我们调用的Polynomial.Polynomial。所以要从polynomials.polynomials.Polynomial调用

# 也就是from polynomial.Polynomial import Polynomial
# from poly_folder_name.module_name import class
