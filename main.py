# def func(string, sp):
#     print(string.split())
#     print(list('ala'))
#     print('-'.join('ala'))
#     return print(' '.join(sp.join(word) for word in string.split()))
#
# func('ala ma kota', '-')

import unittest

def func1(words):
    return list(''.join(str(i) for i in words))


class TestPack(unittest.TestCase):
    def test1(self): return self.assertEqual(func1('Hello'), ['H', 'e', 'l', 'l', 'o'])
    def test2(self): return self.assertEqual(func1(['He','ll', 'o']), ['H', 'e', 'l', 'l', 'o'])
    def test3(self): return self.assertEqual(func1([1,2,3]), ['1', '2', '3'])

if __name__ == '__main__':
    unittest.main()
