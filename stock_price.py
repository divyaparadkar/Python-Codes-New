stock_price = []
with open("stock_price.csv", "r") as f:
    for line in f:
        tokens = line.split(' ,')
        day = tokens[0]
        prices = float(tokens[1])
        stock_price.append([day.price])
