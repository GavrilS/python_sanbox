# An example on simulations using simpy

- A movie theather simulation to determine how many workers in the theather we need to get average wait time for moviegoers to 10 minutes. This is based on the example from https://realpython.com/simpy-simulating-with-python/

# Process

- We need to determine what resource are needed to get the average wait time to no more than 10 minutes per moviegoer during busy hours. We will run different examples for different days when the busy hours have different continuity.
- Resources for the system are #the number of cashiars, #the number of ushers and #the number of food servers
- Controlling parameters for the simulation are the #amount of time the theather is busy on a given day and the #number of tickets that could be sold during this time. For example if on a Friday the busy hours are between 6 and 9 in the evening this will be 180 minutes to the system. In these three hours how many tickets can be sold at the most. If the theather has 10 auditoriums, each with 200 seats and if each auditorium shows a movie every three hours on average, that means the total number of tickets that can be sold for the Friday in our example are 2000 tickets in that time frame.
