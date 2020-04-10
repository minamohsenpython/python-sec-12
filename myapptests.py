import apputility as u
import unittest


class MyAppTest(unittest.TestCase):
    def test_verify1(self):
        result = u.verify("p1", "p2", "admin")
        self.assertFalse(result)

    def test_verify2(self):
        result = u.verify("p1", "p1", "sina")
        self.assertTrue(result)

    def test_fake(self):
        self.assertEqual(2+2, 4)

    def test_in(self):
        l = [i for i in range(10)]
        self.assertIn(5, l)

if __name__ == '__main__':
    unittest.main()