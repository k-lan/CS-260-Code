"""
A fraction class to display and compute fractions
"""

class Fraction:
    def __init__(self, num, den) -> None:
        if isinstance(num, int) and isinstance(den, int):
            lowest = gcd(num, den)
            self.__num = num//lowest
            self.__den = den//lowest
        else:
            raise RuntimeError("You can only use int values (No decimals!)")

    def get_num(self):
        """
        :return: fractions numerator
        """
        return self.__num

    def get_den(self):
        """
        :return: fractions denominator
        """
        return self.__den

    def __str__(self):
        """
        Overwriting the string method
        :return: our fraction in a 'x/y' format
        """
        return f"{self.get_num()}/{self.get_den()}"

    def __repr__(self):
        """
        Overwriting repr method
        :return: dict version of our fraction.
        """
        return {'numerator':self.get_num(), 'denominator':self.get_den()}

    def __add__(self, other_fraction):
        """
        Add two fractions together
        :param other: A fraction to add to our original fraction
        :return: the added fraction.
        """
        new_num = self.get_num() * other_fraction.get_den() + self.get_den() * other_fraction.get_num()
        new_den = self.get_den() * other_fraction.get_den()
        #lowest = gcd(new_num, new_den)
        #return Fraction(new_num // lowest, new_den // lowest)
        return Fraction(new_num, new_den)

    def __iadd__(self, other_fraction):
        """
        Add two fractions together using +=
        :param other: A fraction to add to our original fraction
        :return: the added fraction.
        """
        self_num = self.get_num() * other_fraction.get_den()
        other_num = self.get_den() * other_fraction.get_num()
        new_num = self_num + other_num
        new_den = self.get_den() * other_fraction.get_den()
        return Fraction(new_num, new_den)

    '''
    def __radd__(self, other_fraction):
        """
        Add two fractions together when one fraction is of float rather than int
        :param other: A fraction to add to our original fraction
        :return: the added fraction.
        """
        if other_fraction == 0:
            return self
        elif isinstance(other_fraction, int):
            new_fraction = Fraction(other_fraction, 1)
            return self.__add__(new_fraction)
        else:
            return 'You can not add these data types.'
    '''

    def __eq__(self, other_fraction):
        """
        :param other_fraction: a fraction to compare the first one with ==
        :return: Boolean value if the fractions are the same or not.
        """
        first_num = self.get_num() * other_fraction.get_den()
        second_num = self.get_den() * other_fraction.get_num()
        return first_num == second_num

    def __mul__(self, other):
        """
        multiply both fractions
        :param other: fraction to multiply the first by
        :return: the multiplied fraction
        """
        new_num = (self.get_num() * other.get_den()) * (self.get_den() * other.get_num())
        new_den = (self.get_den() * other.get_den()) ** 2
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        """
        :param other: Fraction to divide by
        :return: the divided fraction
        """
        new_num = self.get_num() * other.get_den()
        new_den = self.get_den() * other.get_num()
        return Fraction(new_num, new_den)

    def __sub__(self, other_fraction):
        """
        Subtract two fractions from each other
        :param other: A fraction to add to our original fraction
        :return: the added fraction.
        """
        new_num = self.get_num() * other_fraction.get_den() - self.get_den() * other_fraction.get_num()
        new_den = self.get_den() * other_fraction.get_den()
        return Fraction(new_num, new_den)

    def __lt__(self, other):
        """
        :param other: fraction
        :return: fraction to compare the size, if other is a larger size it will return true
        """
        first_num = self.get_num() * other.get_den()
        second_num = self.get_den() * other.get_num()
        return first_num < second_num

    def __gt__(self, other):
        """
        :param other: fraction
        :return: fraction to compare the size, if other is a larger size it will return false
        """
        first_num = self.get_num() * other.get_den()
        second_num = self.get_den() * other.get_num()
        return first_num > second_num

    def __le__(self, other):
        """
        :param other: fraction
        :return: comparing fractions with <=
        """
        first_num = self.get_num() * other.get_den()
        second_num = self.get_den() * other.get_num()
        return first_num <= second_num

    def __ge__(self, other):
        """
        :param other: fraction
        :return: fraction to compare the size using >=
        """
        first_num = self.get_num() * other.get_den()
        second_num = self.get_den() * other.get_num()
        return first_num >= second_num

    def __ne__(self, other):
        """
        :param other: fraction
        :return: gives ability to compare fractions using !=
        """
        first_num = self.get_num() * other.get_den()
        second_num = self.get_den() * other.get_num()
        return first_num != second_num

def gcd(m, n):
    """
    :param m: the first integer to be compared
    :param n: the second integer that the first will be compared to
    :return: returns the greatest common divisor of the two
    """
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


def main():

    a_fraction = Fraction(3, 4)
    b_fraction = Fraction(1, 2)
    c_fraction = Fraction(6, 8)
    d_fraction = Fraction(1, -2)
    #print(f'3/4 plus 2 is {a_fraction + 2}')
    print(f'1/2 plus 3/4 is {b_fraction + a_fraction}')
    print(f'1/-2 += 3/4 is {d_fraction.__iadd__(a_fraction)}')
    print(f'1/-2 plus 1/2 is {d_fraction -b_fraction}')
    print(f'1/-2 * 3/4 is {d_fraction * a_fraction}')
    print(f"3/4 plus 1/2 is {a_fraction + b_fraction}")
    print(f'3/4 is equal to 1/2: {a_fraction == b_fraction}')
    print(f'3/4 is equal to 6/8: {a_fraction == c_fraction}')
    print(f'3/4 * 1/2 is {a_fraction * b_fraction}')
    print(f'1/2 / 3/4 is {b_fraction / a_fraction}')
    print(f"3/4 minus 1/2 is {a_fraction - b_fraction}")
    print(f'3/4 < 1/2: {a_fraction < b_fraction}')
    print(f'1/2 < 3/4: {b_fraction < a_fraction}')
    print(f'3/4 > 1/2: {a_fraction > b_fraction}')
    print(f'1/2 > 3/4: {b_fraction > a_fraction}')
    print(a_fraction.__repr__())
    print(gcd(6,9))


#main()