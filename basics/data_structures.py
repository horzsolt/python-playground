import unittest
import time

class Testing(unittest.TestCase):

    def test_set(self):
        # unordered, mutable, no duplicates

        my_set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
        self.assertEqual(len(my_set), 6)

        #no duplicates
        my_set = set([1,1,1,1])
        self.assertEqual(len(my_set), 1)

        # assignment not possible, add/remove supported
        my_set= set([1,2])
        with self.assertRaises(TypeError):
            my_set[0] = 3

        my_set.add(4)
        self.assertEqual(len(my_set), 3)

        my_set.remove(1)
        self.assertEqual(len(my_set), 2)

        #null allowed
        my_set = set([None, 1])
        self.assertEqual(len(my_set), 2)        

    def test_list(self):
        # ordered, mutable collection of (various) elements []

        my_list = [3,1,2,"hello", "world"]
        self.assertEqual(len(my_list), 5)
        print(my_list)

        #nulls and duplicates are allowed
        my_list = [None, None]
        self.assertEqual(len(my_list), 2)

        my_list[0] = 4
        self.assertEqual(my_list[0], 4)

        start = time.time()
        my_large_list = [x for x in range(30000000)]
        end = time.time()
        print(f'List generation time: {end - start}')

        start = time.time()
        my_large_list.remove(0)
        end = time.time()
        print(f'Removing the first item from a list: {end - start}')

        start = time.time()
        my_large_list.remove(len(my_large_list))
        end = time.time()
        print(f'Removing the last item from a list: {end - start}')

        start = time.time()
        my_large_list.append('oops')
        end = time.time()
        print(f'Append time: {end - start}')

        start = time.time()
        my_large_list.insert(0, '123')
        end = time.time()
        print(f'Insert[0] time: {end - start}')

        start = time.time()
        my_large_list.insert(len(my_large_list), '123')
        end = time.time()
        print(f'Insert[last] time: {end - start}')

        #comprehension examples
        print([i for i in range(0,2)])
        #permutations
        print([[i,j] for i in range(0,2) for j in range(0,2)])
        print([[i, j, k] for i in range (0, 2) for j in range (0, 2) for k in range (0, 2)])

        #slicing: start:end:step -> 0,len(list),1
        my_list = [1,2,3,4,5]
        #first three elements
        self.assertEqual(my_list[:3], [1,2,3])

        #last two
        self.assertEqual(my_list[-2:], [4,5])

        #every other
        self.assertEqual(my_list[::2], [1,3,5])

        #reverse
        self.assertEqual(my_list[::-1], [5,4,3,2,1])

        #second item
        self.assertEqual(my_list[1], 2)

        #zip
        list1 = [1,2,3]
        list2 = [4,5,6]

        sum_list = [x + y for x, y in zip(list1, list2)]
        print(sum_list)



    def test_tuple(self):
        # tuple is immutable, ordered ()

        #nulls and duplicates are allowed
        my_tuple = (None, None)
        self.assertEqual(len(my_tuple), 2)

        my_tuple = (1,2,3,"hello", "world")
        self.assertEqual(len(my_tuple), 5)
        with self.assertRaises(TypeError):
            my_tuple[0] = 4

    def test_dict(self):
        # dict is unordered key-value pairs
        my_dict = {"key1" : "value1", "key2" : "value2"}
        self.assertEqual(len(my_dict), 2)

        my_dict["key1"] = 123
        self.assertEqual(my_dict["key1"], 123)

        # creation using dictionary comprehension
        my_dict = {x: x**2 for x in [1,2,3,4,5]}
        self.assertEqual(len(my_dict), 5)
        self.assertEqual(my_dict[1], 1)
        self.assertEqual(my_dict[4], 16)

if __name__ == '__main__':
    unittest.main()