stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}




total_price1 = {key1: prices[key1] * stock[key1] for key1 in stock}

print(total_price1)