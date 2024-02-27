
# 27.2.24 Testing
<<<<<<< HEAD

import  unittest
from main import Kalkulacka

class TestAddFunction(unittest.TestCase):
    def test_add_integers(self):
        calc=Kalkulacka()
        self.assertEqual(calc.sucet(1,2),3)

    def test_add_negative(self):
        calc=Kalkulacka()
        self.assertAlmostEqual(calc.sucet(-1,-1),-2)

    def test_add_floats(self):
        calc=Kalkulacka()
        self.assertAlmostEqual(calc.sucet(1.1,2.2,3.3, places=1))

    if __name__ == "__main__":
        unittest.main()
=======
# import math
import math

class Kalkulacka():

    def sucet(self,a,b):
        v=a+b
        return(v)

    def sucin(self,a,b):
        v=a*b
        return(v)

    def podiel(self,a,b):
        v=a/b
        return(v)


    def odvesna(self,c,b):
        a=math.sqrt((c**2)-(b**2))
        return(a)



    def quadratic_roots(self,a, b, c):
    # Calculate the discriminant
        discriminant = b ** 2 - 4 * a * c

    # Check if a is zero to avoid division by zero
        if a == 0:
            return "The coefficient 'a' cannot be zero in a quadratic equation."

    # Case 1: Two distinct real roots
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return (root1, root2)

kalkulacka=Kalkulacka()
print(f" sucet:{kalkulacka.sucet(2,5)}")
print(f" sucin:{kalkulacka.sucin(2,5)} ")
print(f"podiel:{kalkulacka.podiel(6,2)}")
print(f"Odvesna: {kalkulacka.odvesna(6,4)}")
print(f" Korene:{kalkulacka.quadratic_roots(1,-3,2)}")













#
# import  unittest
# from main import Kalkulacka
#
# class TestAddFunction(unittest.TestCase):
#     def test_add_integers(self):
#         calc=Kalkulacka()
#         self.assertEqual(calc.sucet(1,2),3)
#
#     def test_add_negative(self):
#         calc=Kalkulacka()
#         self.assertAlmostEqual(calc.sucet(-1,-1),-2)
#
#     def test_add_floats(self):
#         calc=Kalkulacka()
#         self.assertAlmostEqual(calc.sucet(1.1,2.2,3.3, places=1))
#
#     if __name__ == "__main__":
#         unittest.main()
>>>>>>> 3de6191 (test2)

