'''
This script shows how to skip tests when necessary. The reasons to skip a test can be a number 
of things:
- Incomplete feature
- External service which is currently unavailable
- Conditional execution - check only if a condition is present
- Known failures which you are working on
- Performance considerations for long running, resource heavy tests
- Deprecated feature
- Others
'''
import unittest

SKIP_TEST_INITIAL = True
SKIP_TEST_SECONDARY = False

class SkipTestExample(unittest.TestCase):

    @unittest.skip('Skip test always')
    def test_always_skip(self):
        '''This never runs'''
        self.fail('Always fail this test when not skipped.')

    @unittest.skipIf(SKIP_TEST_INITIAL, 'Skip only when condition is True')
    def test_when_true(self):
        '''This will only run if SKIP_TEST_INITIAL is changed to False'''
        self.assertEqual(1, 1)

    @unittest.skipIf(SKIP_TEST_SECONDARY, 'Never skip this test, unless the condition is changed to True')
    def test_never_skip(self):
        '''This will always run unless SKIP_TEST_SECONDARY is changed to True'''
        self.assertNotEqual(10, 5)


if __name__=='__main__':
    unittest.main(verbosity=2)