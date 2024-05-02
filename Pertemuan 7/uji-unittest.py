import unittest

def tambah(a, b):
    return a + b

class TestPengujian(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(tambah(2, 3), 5)
        self.assertEqual(tambah(-1, 1), 0)
        self.assertEqual(tambah(0, 0), 0)

if __name__ == '__main__':
    unittest.main()