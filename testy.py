import unittest
import kalkulator as k

# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

class TestyKalkulator(unittest.TestCase):

    def test_dod(self):
        self.assertEqual(k.dodawanie(2,3),5)

    def test_mnoz(self):
        self.assertEqual(k.mnozenie(2,3),6)

    def test_dziel(self):
        self.assertEqual(k.dzielenie(4,2),2)
        with self.assertRaises(ZeroDivisionError):
            k.dzielenie(4,0)
    
    def test_odej(self):
        self.assertEqual(k.odejmowanie(4,2),2)



if __name__ == '__main__':
    unittest.main()