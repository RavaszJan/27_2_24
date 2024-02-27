

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
        self.assertAlmostEqual(calc.sucet(1.1,2.2), 3.3, places=1)

    def test_sucin_integers(self):
        calc=Kalkulacka()
        self.assertEqual(calc.sucin(10,5),50)

    def test_quadratic_roots(self):
        calc=Kalkulacka()
        a=calc.quadratic_roots(1,-3,2)
        self.assertEqual(a[0],2.0)
        self.assertEqual(a[1],1.0)


if __name__ == "__main__":
    unittest.main()
