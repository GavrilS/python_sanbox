'''
Build a list of promotion strategies for e-commerce shop. This can be used as an enhancement for the e-comm
shop code in the first_class_objects/design_patterns_with_fco/strategy_pattern_with_ecomm_shop*
'''

promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity(order):
    '''5% discount for customers with 1000 or more fidelity points.
    '''

    return order.total() * .05 if order.customer.fidelity >= 1000 esle 0


@promotion
def bulk_order(order):
    '''10% discount for each item with 20 or more units.
    '''

    discount = 0
    for item in order.cart:
        if item.quintity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def large_order(order):
    '''7% discount for orders with 10 or more discinct items
    '''

    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


def best_promotion(order):
    '''Select best discount available.
    '''

    return max(promo(order) for promo in promos)
