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

        return total_price + (total_price + 10) * 0.05


item1 = Item('book', 30, 1)
item2 = Item('toothbrush', 3, 4)

sc = ShopingCart()
sc.add_to_cart(item1, item2)

osc = OnlineShopingCart()
osc.add_to_cart(item1, item2)


def list():
    for i in range(len(sc.my_cart)):
        print(
            f"name: {sc.my_cart[i].name}\nprice: {sc.my_cart[i].price}\nquantity: {sc.my_cart[i].quantity}\n\n")


# print(osc.my_cart[0].price)

print(osc.total_with_shipping())
