class Polynomial:
    def __init__(self,coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients)-1

    def __str__(self):
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

#注意区分polynomials\polynomials\Polynomial.py 还有 class Polynomial
# total_folder_name \poly_folder_name\module_name. 还有 class Polynomial是在module里面的class

####我们调用的Polynomial.Polynomial。所以要从polynomials.polynomials.Polynomial调用

#也就是from polynomial.Polynomial import Polynomial
#from poly_folder_name.module_name import class