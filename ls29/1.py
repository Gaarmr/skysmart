class Shop:
    def __init__(self, *items):
        self.stock = list(items)

    def list_items(self):
        output = 'In stock:\n'
        for item in self.stock:
            if item.amount > 0:
                output += f'{item.name}: {item.price}, {item.amount}, {item.rarity}\n'
        return output



class Item:
    def __init__(self, name, price, amount=1, rarity='common'):
        self.name = name
        self.price = price
        self.amount = amount
        self.rarity = rarity

    def decrease_amount(self, value=1):
        if self.amount - value >= 0:
            self.amount -= value
        else:
            raise ValueError('Item amount can not be negative')

shop = Shop(
    Item("Eyes of door",300,5,"Legendary"), 
    Item("Flapppy",345,6,"Rare"), 
    Item("Srenshin",1450,7,"Epic"),
    Item("Brawl sraft",345,13,"Mythic"),
    Item("Miratel",12463,57,),
    Item("Dangaranpa",6564,87,"Rare"),
    Item("Your turn to disobey",2456,345,"Mythic"),
    Item("SRUGUS",6541,65,"LEGENDARY"),
    Item("impact",13456,9,"rare"),
    Item("Underway",1245,12,)
)
print(shop.list_items())