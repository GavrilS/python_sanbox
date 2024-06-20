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
import statistics


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
        with cinema.food_server.request() as request:
            yield request
            yield env.process(cinema.purchase_food(moviegoer))

    wait_times.append(env.now - arrival_time)


def run_cinema(env, num_cashiers, num_ushers, num_food_sellers, num_available_seats):
    cinema = Cinema(env, num_cashiers, num_ushers, num_food_sellers)

    for moviegoer in range(3):
        env.process(go_to_movies(env, moviegoer, cinema))

    while True:
        yield env.timeout(0.20)

        moviegoer += 1
        env.process(go_to_movies(env, moviegoer, cinema))
        if moviegoer == num_available_seats: 
            return


def calculate_wait_time():
    average_wait = statistics.mean(wait_times)
    minutes, frac_minutes = divmod(average_wait, 1)
    seconds = frac_minutes * 60
    return round(minutes), round(seconds)


def get_user_input():
    num_cashiers = input('Number of cashiers for the simumlation: ')
    num_ushers = input('Number of ushers for the simulation: ')
    num_food_sellers = input('Number of food sellers for the simulation: ')
    num_busy_hours = input('The time in minutes that we are testing: ')
    num_available_tickets = input('The available number of tickets for the specified time: ')
    params = [num_cashiers, num_ushers, num_food_sellers, num_busy_hours, num_available_tickets]
    if all(str(i).isdigit() for i in params):
        params = [int(x) for x in params]
    else:
        print('Could not parse input. The simulation will use default values:',
              "\n1 cashier, 1 usher, 1 food seller, 180 minutes, 2000 seats available")
        params = [1, 1, 1, 180, 2000]
    return params


def main():
    random.seed(42)
    num_cashiers, num_ushers, num_food_sellers, busy_hours, num_available_tickets = get_user_input()

    env = simpy.Environment()
    env.process(run_cinema(env, num_cashiers, num_ushers, num_food_sellers, num_available_tickets))
    env.run(until=busy_hours)

    mins, secs = calculate_wait_time()
    print(
        "Running simulation...",
        f"\nThe average wait time is {mins} minutes and {secs} seconds.",
    )


if __name__=='__main__':
    main()
