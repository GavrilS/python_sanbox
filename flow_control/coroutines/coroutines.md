# Coroutines:

A coroutine is a genarator where the 'yield' keyword is part of the expression on the right. In a coroutine
yield doesn't necessarily produce a value, but can get a value from the client with the send() method.

# States - a coroutine can be one of the following states:

- GEN_CREATED - waiting to start execution
- GEN_RUNNING - currently being executed by the interpreter
- GEN_SUSPENDED - currently suspended at a 'yield' expression
- GEN_CLOSED - execution has completed

The send() method can only be used when a coroutine reaches the 'yield' keyword, so the first call to a coroutine after it is created should always be next() or send(None) to activate the coroutine and make it
reach the 'yield' expression. If we use send(some_value) before a coroutine reaches the 'yield' expr. it will
raise an error.
