import unittest
import kalkulatur


class TestKalk(unittest.TestCase):
    def test_plus(self):
        """Testing add func with different attrs."""
        self.assertEqual(kalkulatur.plus(10, 20), 30)
        self.assertEqual(kalkulatur.plus(-10, 5), -5)
        self.assertEqual(kalkulatur.plus(-10, -10), -20)

    def test_minus(self):
        """Testing subtract func with different attrs."""
        self.assertEqual(kalkulatur.minus(20, 10), 10)
        self.assertEqual(kalkulatur.minus(-10, 5), -15)
        self.assertEqual(kalkulatur.minus(-10, -10), 0)

    def test_umnozhit(self):
        """Testing multiply func with different attrs."""
        self.assertEqual(kalkulatur.umnozhit(5, 10), 50)
        self.assertEqual(kalkulatur.umnozhit(-10, 5), -50)
        self.assertEqual(kalkulatur.umnozhit(-10, -10), 100)

    def test_podelit_success(self):
        """Testing divide func with different attrs."""
        self.assertEqual(kalkulatur.podelit(10, 5), 2)
        self.assertEqual(kalkulatur.podelit(-10, 5), -2)
        self.assertEqual(kalkulatur.podelit(-10, -5), 2)
        self.assertEqual(kalkulatur.podelit(5, 2), 2.5)

    def test_podelit_error(self):
        """Testing divide func to raise Error."""
        with self.assertRaises(ZeroDivisionError):
            kalkulatur.podelit(10, 0)

    def test_podelit_celochisleno(self):
        self.assertEqual(kalkulatur.podelit_celolochisleno(10, 5), 2)
        self.assertEqual(kalkulatur.podelit_celolochisleno(-10, 5), -2)
        self.assertEqual(kalkulatur.podelit_celolochisleno(-10, -5), 2)
        self.assertEqual(kalkulatur.podelit_celolochisleno(11, 2), 5)
        self.assertEqual(kalkulatur.podelit_celolochisleno(-16, 5), -4)
        self.assertEqual(kalkulatur.podelit_celolochisleno(-11, -5), 2)

if __name__ == '__main__':
    unittest.main()
