import unittest

from roman_numerals import RomanNumerals

class TestRomanNumerals(unittest.TestCase):

    def test_I(self):
        expected = 1
        actual = RomanNumerals('I').get_int()
        self.assertEqual(expected, actual)

    def test_II(self):
        expected = 2
        actual = RomanNumerals('II').get_int()
        self.assertEqual(expected, actual)

    def test_IV(self):
        expected = 4
        actual = RomanNumerals('IV').get_int()
        self.assertEqual(expected, actual)

    def test_V(self):
        expected = 5
        actual = RomanNumerals('V').get_int()
        self.assertEqual(expected, actual)

    def test_VI(self):
        expected = 6
        actual = RomanNumerals('VI').get_int()
        self.assertEqual(expected, actual)

    def test_VIII(self):
        expected = 8
        actual = RomanNumerals('VIII').get_int()
        self.assertEqual(expected, actual)

    def test_IX(self):
        expected = 9
        actual = RomanNumerals('IX').get_int()
        self.assertEqual(expected, actual)

    def test_X(self):
        expected = 10
        actual = RomanNumerals('X').get_int()
        self.assertEqual(expected, actual)

    def test_XX(self):
        expected = 20
        actual = RomanNumerals('XX').get_int()
        self.assertEqual(expected, actual)

    def test_XL(self):
        expected = 40
        actual = RomanNumerals('XL').get_int()
        self.assertEqual(expected, actual)

    def test_L(self):
        expected = 50
        actual = RomanNumerals('L').get_int()
        self.assertEqual(expected, actual)

    def test_LX(self):
        expected = 60
        actual = RomanNumerals('LX').get_int()
        self.assertEqual(expected, actual)

    def test_LXXX(self):
        expected = 80
        actual = RomanNumerals('LXXX').get_int()
        self.assertEqual(expected, actual)

    def test_XC(self):
        expected = 90
        actual = RomanNumerals('XC').get_int()
        self.assertEqual(expected, actual)

    def test_C(self):
        expected = 100
        actual = RomanNumerals('C').get_int()
        self.assertEqual(expected, actual)

    def test_CC(self):
        expected = 200
        actual = RomanNumerals('CC').get_int()
        self.assertEqual(expected, actual)

    def test_CD(self):
        expected = 400
        actual = RomanNumerals('CD').get_int()
        self.assertEqual(expected, actual)

    def test_D(self):
        expected = 500
        actual = RomanNumerals('D').get_int()
        self.assertEqual(expected, actual)

    def test_DC(self):
        expected = 600
        actual = RomanNumerals('DC').get_int()
        self.assertEqual(expected, actual)

    def test_DCCC(self):
        expected = 800
        actual = RomanNumerals('DCCC').get_int()
        self.assertEqual(expected, actual)

    def test_CM(self):
        expected = 900
        actual = RomanNumerals('CM').get_int()
        self.assertEqual(expected, actual)

    def test_M(self):
        expected = 1000
        actual = RomanNumerals('M').get_int()
        self.assertEqual(expected, actual)

    def test_MM(self):
        expected = 2000
        actual = RomanNumerals('MM').get_int()
        self.assertEqual(expected, actual)

    def test_MMMCMXCIX(self):
        expected = 3999
        actual = RomanNumerals('MMMCMXCIX').get_int()
        self.assertEqual(expected, actual)

    def test_IIII(self):
        expr = RomanNumerals('IIII')._valid()
        self.assertFalse(expr)

    def test_XXXX(self):
        expr = RomanNumerals('XXXX')._valid()
        self.assertFalse(expr)

    def test_CCCC(self):
        expr = RomanNumerals('CCCC')._valid()
        self.assertFalse(expr)

    def test_MMMM(self):
        expr = RomanNumerals('MMMM')._valid()
        self.assertFalse(expr)

    def test_VV(self):
        expr = RomanNumerals('VV')._valid()
        self.assertFalse(expr)

    def test_LL(self):
        expr = RomanNumerals('VV')._valid()
        self.assertFalse(expr)

    def test_DD(self):
        expr = RomanNumerals('VV')._valid()
        self.assertFalse(expr)

    def test_IL(self):
        expr = RomanNumerals('IL')._valid()
        self.assertFalse(expr)

    def test_XD(self):
        expr = RomanNumerals('XD')._valid()
        self.assertFalse(expr)

    def test_VX(self):
        expr = RomanNumerals('VX')._valid()
        self.assertFalse(expr)

    def test_LC(self):
        expr = RomanNumerals('LC')._valid()
        self.assertFalse(expr)

    def test_DM(self):
        expr = RomanNumerals('DM')._valid()
        self.assertFalse(expr)

    def test_IIV(self):
        expr = RomanNumerals('IIV')._valid()
        self.assertFalse(expr)

    def test_XXC(self):
        expr = RomanNumerals('XXC')._valid()
        self.assertFalse(expr)

    def test_CCM(self):
        expr = RomanNumerals('CCM')._valid()
        self.assertFalse(expr)

    def test_MMMCMXCVIII(self):
        expr = RomanNumerals('MMMCMXCVIII')._valid()
        self.assertTrue(expr)

