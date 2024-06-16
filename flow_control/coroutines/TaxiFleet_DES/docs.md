# A Descreet Event Simulation (DES)

A DES is a type of simulation where a system is modeled as a sequence of events. In a DES, the simulation clock
does not advance by fixed increments, but advances directly to the simulated time of the next modeled event.
For example, if we are simulating the operation of a taxi cab from a high-level perspective, one event is picking up a passenger, the next is dropping the passenger off. It doesn’t matter if a trip takes 5 or 50 minutes: when the drop off event happens, the clock is updated to the end time of the trip in a single operation. In a DES, we can simulate a year of cab trips in less than a second. This is in contrast to a continuous simulation where the clock advances continuously by a fixed—and usually small—increment.

Turn-based games are a examples of descreet event simulations: the state of the game only changes when a player makes a move, and while the player is deciding the next move, the simulation clock is frozen. Real-time games, on the other hand, are continuous simulations where the simulation clock is running all the time, the state of the game is updated many times per second, and slow players are at a real disadvantage.
