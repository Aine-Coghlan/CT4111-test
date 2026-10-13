def shopping_total(prices, discount_percent):
    total = sum(prices)
    return total + total * discount_percent / 100
