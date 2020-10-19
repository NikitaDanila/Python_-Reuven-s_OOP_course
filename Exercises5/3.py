class ShopingCart(object):
    def __init__(self):
        self.my_cart = []

    def add_to_cart(self, *args):
        self.my_cart += args

    def delete_from_cart(self, item):
        for one_item in range(len(self.my_cart)):
            if self.my_cart[one_item].name == str(item):
                if int(self.my_cart[one_item].quantity) > 1:
                    self.my_cart[one_item].quantity -= 1
                else:
                    del(self.my_cart[one_item])
                    break

    def total(self):
        total_price = 0
        total_price += sum(self.my_cart[one_item].price * self.my_cart[one_item].quantity
                           for one_item in range(len(self.my_cart)))
        return total_price

    def __len__(self):
        return sum([self.my_cart[one_item].quantity
                    for one_item in range(len(self.my_cart))])

    def __repr__(self):
        output = []
        for one_item in range(len(self.my_cart)):
            output.append(
                f"{self.my_cart[one_item].name:10} {self.my_cart[one_item].quantity:3} ${self.my_cart[one_item].price:3} ${self.my_cart[one_item].price * self.my_cart[one_item].quantity:4}")
        output.append('-------------------------')
        output.append(f"Total: {self.total():18}")

        return '\n'.join(output)


class Item(object):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class OnlineShopingCart(ShopingCart):

    def total_with_shipping(self):
        total_price = 0
        for one_item in range(len(self.my_cart)):
            total_price += self.my_cart[one_item].price * \
                self.my_cart[one_item].quantity

        return (total_price + 10) * 1.05


item1 = Item('book', 30, 1)
item2 = Item('toothbrush', 3, 4)

sc = ShopingCart()
sc.add_to_cart(item1, item2)

osc = OnlineShopingCart()
osc.add_to_cart(item1)


def list():
    for i in range(len(sc.my_cart)):
        print(
            f"name: {sc.my_cart[i].name}\nprice: {sc.my_cart[i].price}\nquantity: {sc.my_cart[i].quantity}\n\n")


# print(osc.my_cart[0].price)

# print(osc.total_with_shipping())
# print(len(sc))
print(sc)
