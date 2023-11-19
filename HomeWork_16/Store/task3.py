import json

class DataBase:
    file_path = 'data_base.json'

    @classmethod
    def work_with_db(cls, mode='r', data=None):
        if mode == 'r':
            with open(cls.file_path, 'r') as db:
                return json.load(db)
        elif mode in ('w', 'a'):
            with open(cls.file_path, 'w' if mode == 'w' else 'a') as db:
                json.dump(data, db, indent=2)


class Product:
    def __init__(self, product_type, name, price, amount=None):
        self.type = product_type
        self.name = name
        self.price = price
        self.amount = amount


class ProductStore:
    profit = 0
    percent = 30 / 100

    def add(self, product, amount):

        new_product = {

            "type": product.type,
            "name": product.name,
            "price": product.price + product.price * self.percent,
            "amount": amount
        }
        data = DataBase.work_with_db('r')
        data.append(new_product)
        DataBase.work_with_db('w', data)

    def set_discount(self, identifier, percent, identifier_type='name'):
        data = DataBase.work_with_db('r')

        for item in data:
            if item[identifier_type] == identifier:
                item["price"] -= item["price"] * percent / 100
        DataBase.work_with_db('w', data)

    def sell_product(self, product_name, amount):

        data = DataBase.work_with_db('r')

        for item in data:
            if item["name"] == product_name:
                if item["amount"] >= amount:
                    item["amount"] -= amount
                    self.profit += item["price"] * amount
                else:
                    print(f'You have only: {item["amount"]} pieces')
                    raise ValueError
        DataBase.work_with_db('w', data)

    def get_income(self):
        return self.profit

    def get_all_products(self):
        data = DataBase.work_with_db('r')
        for i in data:
            print(i)

    def get_product_info(self, product_name):
        data = DataBase.work_with_db('r')
        for item in data:
            if item["name"] == product_name:
                return item["name"], item["amount"]





p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

# s.add(p, 10)
#
# s.add(p2, 300)

# s.sell_product('Ramen', 10)
print(s.get_product_info('Ramen'))

assert s.get_product_info('Ramen') == ('Ramen', 290)