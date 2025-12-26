# Unit testing in Python

1. Overview

Unit tests are a way to test a single unit(methods/functions) of your code and make sure, that the code behaves as expected. They are good to have, because when you change your code at a future point, the tests help you verify that the end result has not changed.

In Python there is a package - <block>unittest</block>, which can help you test your code. The package has many features to make testing easier. Another useful tool in the Python standard library that can help you with tests is <block>doctest</block>. This is lightweight testing framework that provides quick and easy test automation. It can read the test cases from your project's documentation and your code's docstrings.

2. Unittest

The framework is directly available in the standard library, so you don't have to install anything. It uses an object-oriented approach and supports test creation, organization, preparation and automation:
    - Test case: an individual unit of test
    - Test suite: a collection of test cases
    - Test fixture: a group of actions to setup the environment for the tests and tear it down after the tests are done
    - Test runner: a component responsible for running the tests and outputing the results

One of the tools that helps you setting up your tests is the 'TestCase' class from the unittest package.

2.1. Subtests

The unittest frawemork provides the subtest functionality which allows you to run a test with multiple values.

2.2. TestSuite - you can group your tests with the TestSuite class and run them selectively. Usefull for:
    - complex projects - organize tests in logical groups
    - different testing levels - group tests according to their level
    - selective testing
    - environment specific testing - group tests based on environment or platform

3. Assertions

You would use the assert keyword to verify the results of your tested units. There are different tests you can perform with assert, but the most used one is 'assertEqual(param1, param2)', which checks if the 2 paramethers are equal. The 'assertEqual' method is inherited from the 'TestCase' class. There is a large number of available assert methods.

3.1. Comparing values:
.assertEqual(a, b)
.assertNotEqual(a, b)
.assertTrue(x)
.assertFalse(x)

3.2. Comparing objects by their identity:
.assertIs(a, b)
.assertIsNot(a, b)
.assertIsNone(x)
.assertIsNotNone(x)

3.3. Comparing collections:
.assertSequenceEqual(a, b)
.assertMultiLineEqual(a, b)
.assertListEqual(a, b)
.assertTupleEqual(a, b)
.assertDictEqual(a, b)
.assertSetEqual(a, b)

3.4. Membership tests:
.assertIn(a, b) -> a in b
.assertNotIn(a, b)

3.5. Check for object type:
.assertIsInstance(a, b)
.assertNotIsInstance(a, b)

3.6. Testing for exceptions:
.assertRaises(exc, fun, *args, **kwargs) -> fun(*args, **kwargs) raises exc
.assertRaisesRegex(exc, r, fun, *args, **kwargs) -> fun(*args, **kwargs) raises exc and the message matches regex r

3.7. Warnings and logs:
.assertWarns(warn, fun, *args, **kwargs) -> fun(*args, **kwargs) raises warn
.assertWarnsRegex(warn, r, fun, *args, **kwargs) -> fun(*args, **kwargs) raises warn and the message matches regex r
.assertLogs(logger, level)
.assertNoLogs(logger, level)

3.8. Using custom assert methods


4. Running unit tests

You have multiple ways of running unit tests with the unittest package:
4.1. Make the module executable by including a check if the name equals main and then running the tests from there

4.2. You can use the command line interface of unittest:
    - you can run entire test modules:
        python3 -m unittest test_age test_case test_skip_example
    
    - you can run the tests from a specific class:
        python3 -m unittest test_age.TestGetAgeCategory
    
    - you can run tests from individual test methods:
        python3 -m unittest test_age.TestGetAgeCategory.test_child

4.3. Autodiscovery of tests - you can run the discover command of the unittest CLI to run all classes derived from the TestCase class:
    python3 -m unittest discover -s '<start_directory>'


5. Test Fixtures

This is a preparation that is run before and after tests to prepare the environment for the tests. The preparation before the tests is known as setup, while the one after the tests is called teardown. Setup is the process of creating connections, bringing up test DBs, creating temporary resources and so on, while teardown is the opposite process of releaseing these temporary connections/resources.

With the unittest framework we can overwrite these methods in our test classes (which extend the TestClass class) to create setups and teardowns for our tests:
    .setUp() -> an instance method that unittest runs before running each test method in a test case class
    .tearDown() -> an instance method that unittest runs after each test method in a test case class
    @classmethod
    .setUpClass(cls) -> a class method that unittest calls before running the tests in a test case class
    @classmethod
    .tearDownClass(cls) -> a class method that unittest calls after running the tests in a test case class
    .setUpModule() -> runs before all test cases in the containing module
    .tearDownModule() -> runs after all test cases have run

