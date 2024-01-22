from pprint import pprint


data = [
    "Системный блок: 1500 75890.56",
    "Монитор Samsung: 2000 34000",
    "Клавиатура: 200.44 545",
    "Монитор Samsung: 2000 34000",
]


class ShopItem:
    def __init__(self, name, weight, price) -> None:
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self) -> int:
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other) -> bool:
        return hash(self) == hash(other)

    
    def __repr__(self) -> str:
        return f"ShopItem({self.name}, {self.weight}, {self.price})"


shop_items = {}

for i in data:
    obj = ShopItem(i[:i.find(": ")], *i[i.find(": ")+1:].split())
    
    exist = shop_items.setdefault(obj, [obj, 0])
    shop_items[obj][1] += 1

    pprint(obj)
    
    
# def convert_data(data):
#     new_data2 = []
#     for i in data:
#         spam = []

#         name, other = i.split(": ")
#         spam.append(name)
#         for j in other.split():
#             if "." in j:
#                 spam.append(float(j))
#             else:
#                 spam.append(int(j))

#         new_data2.append(spam)
#         spam = []
#     return list(new_data2)


# def create_dict(data):
#     new_data2 = convert_data(data)

#     shop_items = {}

#     for i in new_data2:
#         item = ShopItem(i[0], i[1], i[2])
#         if item in shop_items:
#             shop_items[item] = [item, shop_items[item][1] + 1]
#         else:
#             shop_items[item] = [item, 1]

#     return dict(shop_items)


# shop_items = create_dict(data)



pprint(shop_items)
