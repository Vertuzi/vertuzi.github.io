# showing goal of the game and move commands
def show_instructions():
    print("Dragon Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the dragon.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


def show_status():
    print("You are in the {}".format(current_room))
    print('Inventory: ', inventory)

    current_dict = rooms[current_room]
    item = 'none'
    if 'item' in current_dict:
        item = current_dict['item']
        print('You see a', item)


rooms = {
    'Front Entrance': {'East': 'Living Room'},
    'Living Room': {'North': 'Bedroom', 'South': 'Library', 'East': 'Kitchen', 'item': 'Armor'},
    'Library': {'North': 'Living Room', 'East': 'Bookshelf', 'item': 'Shield'},
    'Bookshelf': {'West': 'Library', 'item': 'Spellbook'},
    'Bedroom': {'South': 'Living Room', 'East': 'Closet', 'item': 'Boots'},
    'Closet': {'West': 'Bedroom', 'item': 'Helmet'},
    'Kitchen': {'West': 'Living Room', 'East': 'Cellar', 'item': 'Knife'},
    'Cellar': {'West': 'Kitchen', 'item': 'Dragon!'}

}


starting_room = 'Front Entrance'     # set starting room to front entrance for a starting point
inventory = []      # set inventory as blank to start
current_room = starting_room

show_instructions()

while True:
    show_status()
    if current_room == 'Cellar':
        if len(inventory) == 6:     # check number of items in inventory to determine if player won or lost
            print("Congratulations! You have collected all items and defeated the dragon!")
        else:
            print("NOM NOM...Game Over!")

        print('Thanks for playing! Hope you enjoyed it!')
        break
    list = input("Enter your move: ").split()
    print()
    list = [x.capitalize() for x in list]
    if len(list) == 1:
        if list[0] == "Exit":
            current_room = 'exit'
            print('Thanks for playing! Hope you enjoyed it!')
            break
        else:
            print('Invalid Input!')
            continue
    elif len(list) >= 2:
        action = list[0].lower()

        if action == 'go':
            if len(list) > 2:
                print('Invalid Input!')
                continue
            direction = list[1]
            possible_rooms = rooms[current_room]
            if direction in possible_rooms:
                current_room = possible_rooms[direction]
            else:
                print(f'Invalid Input!')
        elif action == "get":   # user input to get item
            if 'item' in rooms[current_room]:
                item_name = ''
                i = 1
                for val in list[1:]:
                    if i != 1:
                        item_name += f' {val}'
                        print(item_name, 'retrieved!')
                        print()
                    else:
                        item_name += val
                    i += 1
                if rooms[current_room]["item"] == item_name:
                    inventory.append(item_name)
                    rooms[current_room].pop("item")
                    if len(inventory) == 6:
                        print("You have collected all 6 items! Go find and defeat the dragon!")
                else:
                    print("Invalid Input!")
            else:
                print("Invalid Input!")
        else:
            print('Cannot get that item!')


