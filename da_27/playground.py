def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(1, 2, 3, 5, 8, 11, 1))


def calc(n, **kwargs):
    print(kwargs["add"])
    # for key,val in kwargs.items():
    #     print(key)
    #     print(val)


calc(2, add=2, mul=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


my_car = Car(make="nisan", model="gtr")
print(my_car.model)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)