import unittest

class Stack:
    '''
    Create a basic stack implementation to test unittest fixtures.
    '''

    def __init__(self, items=None):
        '''
        If no items are passed to the stack when creating it, then the stack is an empty list,
        else it contains a list of the passed items.
        '''
        self.items = [items] if items is not None else []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __reversed__(self):
        return reversed(self.items)
    

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
    
    def tearDown(self):
        del self.stack

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.items, [1])

    def test_pop(self):
        self.stack.push(2)
        res = self.stack.pop()
        self.assertEqual(res, 2)

    def test_len(self):
        self.stack.push(3)
        self.assertEqual(len(self.stack), 1)

    def test_iter(self):
        items = [1, 2, 3]
        for item in items:
            self.stack.push(item)

        for stack_item, item in zip(self.stack, items):
            self.assertEqual(stack_item, item)
    
    def test_reversed(self):
        items = [1, 2, 3]
        for item in items:
            self.stack.push(item)
        
        reversed_items = reversed(self.stack)
        self.assertEqual(list(reversed_items), list(reversed(items)))
        

if __name__=='__main__':
    unittest.main(verbosity=2)