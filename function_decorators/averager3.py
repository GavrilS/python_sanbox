def make_averager_failure():
    count = 0
    total = 0

    def averager(new_value):
        count += 1  # this fails because it is trying to assign to the variable within the body of the func which makes it a local variable
        total += new_value # this fails because it is trying to assign to the variable within the body of the func which makes it a local variable
        return total/count

    return averager


def make_averager_correct():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total # this allows us to use count and total as free variables and assign new values to them
        count += 1
        total += new_value
        return total/count

    return averager



if __name__=='__main__':
    avg_error = make_averager_failure()
    try:
        print('avg_error(10): ')
        print(avg_error(10))
    except Exception as e:
        print(e)

    avg = make_averager_correct()
    print('avg(10): ', avg(10))
    print('avg(12): ', avg(12))
