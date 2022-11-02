class Inventory:

    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.items = []
        self.left_capacity = 0

    def add_item(self, item: str):
        if self.left_capacity < self.__capacity:
            self.items.append(str(item))
            self.left_capacity += 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {Inventory.get_capacity(self) - self.left_capacity}"




inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
