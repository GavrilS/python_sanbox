from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price


    def total(self):
        return self.price * self.quantity



class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion


    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        
        return self.total() - discount

    
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

    

class Promotion(ABC): # The strategy: an abstract base class

    @abstractmethod
    def discount(self, order):
        """Return discount as a positive amount"""


class FidelityPromo(Promotion):
    """5% discount for customer with 1000 or more fidelity points"""

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """10% discount for each LineItem with 20 or more units"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1

        return discount




if __name__=='__main__':
    joe = Customer('John Doe', 0)
    sue = Customer('Sue Doe', 1200)
    bil = Customer('Bil Willis', 2800)
    cart = [
        LineItem('banana', 4, .5),
        LineItem('apple', 3, 1),
        LineItem('watermellon', 2, 3.8)
    ]
    banana_cart = [
        LineItem('banana', 30, .5),
        LineItem('apple', 10, 1)
    ]

    joe_order = Order(joe, cart, FidelityPromo())
    sue_order = Order(sue, banana_cart, FidelityPromo())
    bil_banana = Order(bil, banana_cart, FidelityPromo())
    bil_banana_bulk = Order(bil, banana_cart, BulkItemPromo())
    print('**********ORDERS START**********')
    print('joe_order: ', joe_order)
    print('sue_order: ', sue_order)
    print('bil_banana: ', bil_banana)
    print('bil_banana_bulk: ', bil_banana_bulk)
    print('**********ORDERS END**********')
