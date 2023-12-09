registry = set()

def register(active=True): # this is a decorator factory accepting a keyword argument and returns the actial decorator
    def decorate(func): # this is the actual decorator and accepts a function as an argument, returning it in the end
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func
    return decorate


@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry -> ', registry)
    f1()
    f2()
    f3()


if __name__=='__main__':
    main()
