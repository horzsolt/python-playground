import unittest
from contextlib import contextmanager

def even_numbers(n):
    for i in range(n):
        yield 2*i

@contextmanager
def my_context_manager():
    resource = open('README.md','r')
    try:
        yield resource
    finally:
        resource.close()

class Testing(unittest.TestCase):

    def test_gen(self):
        even_gen = even_numbers(3)

        for idx, num in enumerate(even_gen):
            self.assertEqual(num, 2*idx)

        for idx, num in enumerate(even_numbers(50)):
            self.assertEqual(num, 2*idx)

    def test_context_mgr(self):
        with my_context_manager() as res:
            self.assertEqual(res.name, 'README.md')

if __name__ == '__main__':
    unittest.main()