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

3. Assertions

You would use the assert keyword to verify the results of your tested units. There are different tests you can perform with assert, but the most used one is 'assertEqual(param1, param2)', which checks if the 2 paramethers are equal. The 'assertEqual' method is inherited from the 'TestCase' class.

4. Running unit tests

You have multiple ways of running unit tests with the unittest package:
1) Make the module executable by including a check if the name equals main and then running the tests from there
2) You can use the command line interface of unittest