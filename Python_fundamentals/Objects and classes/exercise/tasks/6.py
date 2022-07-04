class Inventory:
    __capacity = 0

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add_item(self, items):
        if len(self.items) < self.capacity:
            self.items.append(items)
        return "not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        self.capacity -= self.capacity
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
