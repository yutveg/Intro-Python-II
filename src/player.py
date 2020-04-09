# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room, inventory=None):
        self.name = name
        self.room = room
        self.inventory = [] if inventory is None else inventory
