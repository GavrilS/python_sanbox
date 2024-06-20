"""
A program to help determine what resource are needed to make average wait time for a moviegoer
to get tickets to no more than 10 minutes.

Available cinema resources which we can change:
    - number of cashiars - handles a sale in 1-2 minutes
    - number of ushers - handles a customer in 5 seconds
    - number of food servers - sells food in 1-6 minutes

Parameters to run the simulation:
    - busy hours total time in minutes
    - maximum number of tickets that can be sold per this time
"""
import simpy
import random


wait_times = []


class Cinema:

    def __init__(self, env, num_cashiers, num_ushers, num_food_servers):
        self.env = env
        self.cashier = simpy.Resource(env, num_cashiers)
        self.usher = simpy.Resource(env, num_ushers)
        self.food_server = simpy.Resource(env, num_food_servers)


    def purchase_ticket(self, moviegoer):
        yield self.env.timeout(random.randint(1, 3))

    
    def check_ticket(self, moviegoer):
        yield self.env.timeout(5 / 60)


    def purchase_food(self, moviegoer):
        yield self.env.timeout(random.randint(1, 6))


def go_to_movies(env, moviegoer, cinema):
    arrival_time = env.now

    with cinema.cashier.request() as request:
        yield request
        yield env.process(cinema.purchase_ticket(moviegoer))

    with cinema.usher.request() as request:
        yield request
        yield env.process(cinema.check_ticket(moviegoer))
    
    if random.choice([True, False]):
        with cinema.food_server.requst() as request:
            yield request
            yield env.process(cinema.purchase_food(moviegoer))

    wait_times.append(env.now - arrival_time)


def run_cinema(env, num_cashiers, num_ushers, num_food_sellers):
    cinema = Cinema(num_cashiers, num_ushers, num_food_sellers)

    for moviegoer in range(3):
        env.process(go_to_movies(env, moviegoer, cinema))

    while True:
        yield env.timeout(0.20)

        moviegoer += 1
        env.process(go_to_movies(env, moviegoer, cinema))
