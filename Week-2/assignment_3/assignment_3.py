

def main():
    print(avg({
        "products": [{"name": "Product 1", "price": 100},
                     {"name": "Product 2", "price": 700}, {"price": 300}]}))
    # print the average price of all products (round to 3 decimal)


def avg(data):
    total = 0
    count = 0
    for value in data["products"]:
        if "price" in value:
            total += value["price"]
            count +=1
            ave= round(total/count,3)
    return ave




if __name__ == '__main__':
    main()
