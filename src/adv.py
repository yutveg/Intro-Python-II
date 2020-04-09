from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'staff_of_plague': Item("Staff Of Plague", "A rotting, twisting wood shaped into a staff.", "Your hands tingle upon grasping the staff."),
    'coin_bag': Item("Coin Bag", "A leather pouch full of coins."),
    'glove': Item("Glove", "A basic peasant glove."),
    'book': Item("Book", "A mysterious book with no cover.", "An energy enters the room.")
}

# Adding items to rooms

room['foyer'].contents = [item['coin_bag']]
room['treasure'].contents = [item['coin_bag']]
room['outside'].contents = [item['glove']]
room['overlook'].contents = [item['staff_of_plague'], item['book']]

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

thomas = Player("Thomas", room['outside'])

#
# Main
#


def move_rooms(direction):
    switcher = {
        "w": "n_to",
        "s": "s_to",
        "d": "e_to",
        "a": "w_to"
    }
    return switcher.get(direction, "Invalid Input")


def move_player(movement):
    try:
        newRoom = getattr(thomas.room, movement)
        return newRoom
    except AttributeError:
        print("*******************\nNo room in that direction. Please try again.\n*******************")
        return None


def handle_item_interaction(action):
    if(action[0] == 'take'):
        thomas.room.contents.remove(item[action[1]])
        thomas.inventory.append(item[action[1]])
        item[action[1]].on_take()
        print(f"{item[action[1]].name} has been added to your inventory.")
    if(action[0] == 'drop'):
        thomas.inventory.remove(item[action[1]])
        thomas.room.contents.append(item[action[1]])
        print(f"{item[action[1]].name} has been removed from your inventory.")
    return


def open_inventory():
    print("********* INVENTORY: *********")
    if(len(thomas.inventory) == 0):
        print("*crickets*")
    else:
        for item in thomas.inventory:
            print(f"{item.name}: {item.description}")

    print("******************************")
    input("Press enter to close inventory: ")


def handle_player_action(action):
    command_type = action.split(' ')
    if(len(command_type) == 2):  # user inputted a command
        handle_item_interaction(command_type)
    if(len(command_type) == 1):  # user inputted a movement
        if action == 'q':
            print("Thanks for playing.")
            exit()
        if action == 'i':
            open_inventory()
        else:
            direction = move_rooms(action)
            newRoom = move_player(direction)
            if(newRoom is None):
                pass
            else:
                try:
                    thomas.room = newRoom
                except Exception as e:
                    print(e)


def main():
    while True:
        print(f"{thomas.name} is in room: {thomas.room.name}")
        if(thomas.room.contents is not None):
            if(len(thomas.room.contents) >= 1):
                print(f"The room contains: ")
                for item in thomas.room.contents:
                    print(item.name)

        command = input("Move with WASD or enter command: ")
        handle_player_action(command)


main()

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
