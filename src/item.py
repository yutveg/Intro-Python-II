class Item:
    def __init__(self, name, description, effect=None):
        self.name = name
        self.description = description
        self.effect = effect

    def on_take(self):
        print(f"You have picked up {self.name.upper()}")
        if(self.effect is None):
            pass
        else:
            print(f"{self.effect}")
