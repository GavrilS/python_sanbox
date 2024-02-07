=======
Tombola tests
=======

Every concrete subclass of Tombola should pass these tests.

Create and load iterable:

>>> balls = list(range(3))
>>> globe = ConcreteTombola(balls)
>>> globe.loaded()
True
>>> globe.inspect()
(0, 1, 2)

Pick and collect balls:

>>> picks = []
>>> picks.append(globe.pick())
>>> picks.append(globe.pick())
>>> picks.append(globe.pick())

Check states and result:

>>> globe.loaded()
False
>>> sorted(picks) == balls
True
