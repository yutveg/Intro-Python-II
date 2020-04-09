# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, contents=None):
        self.name = name
        self.description = description
        self.contents = [] if contents is None else contents
