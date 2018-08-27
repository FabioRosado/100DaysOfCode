import json

HEADER = """
$$$$$$$$\                           $$\                                                      
\__$$  __|                          $$ |                                                     
   $$ | $$$$$$\  $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\                             
   $$ |$$  __$$\ \____$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\                            
   $$ |$$ |  \__|$$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|                           
   $$ |$$ |     $$  __$$ |$$ |      $$  _$$<  $$   ____|$$ |                                 
   $$ |$$ |     \$$$$$$$ |\$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |                                 
   \__|\__|      \_______| \_______|\__|  \__| \_______|\__|                                 
                                                                    
"""

house = []

values = []


def create_room():
    """Creates a new room. """
    print('\n ***************** CREATE ROOM *************** \n')
    room = input("Which room would you like to add to the house? ")
    house.append(str(room))
    print(f"The Room: {room} was added to your house. You can now add items to it. \n")


def add_item():
    print('\n ****************** ADD ITEMS **************** \n')
    items = {}
    room = input("Which room should we add this item? ").lower()
    if room not in house:
        question = input("Sorry, the house doesn't seem to have that room. Create one? \n"
                         "[y]es/[n]o ").lower()
        if question == 'y':
            create_room()
        else:
            print("Unable to add item. Sorry")
            commands()
    print(f"Adding item for the room: {room}: \n Press X to quit.")
    while True:
        item = input("Add the name of the item: ").lower()
        if item == 'x':
            commands()
            break
        value = int(input("Enter the value of the item: "))
        print("\n")
        items[item] = value

    values.append((room, items))


def list_all():
    print('\n **************** LIST ALL ITEMS ************** \n')
    for room in values:
        print(f"Room: {room[0]}")
        for item, value in room[1].items():
            print(f"    {value}" + f"             £ {value}")
        print(f"Subtotal: £{sum(room[1].values())} \n")


def see_rooms():
    print('\n ************* ROOMS IN THE HOUSE ************ \n')
    print("These are all the rooms available in the house:")
    for room in house:
        print(f"    {room}")


def save():
    _json = json.dumps(values)
    with open('data.json', 'w') as file:
        file.write(_json)
    print("House saved.")


def open_previous():
    with open('data.json') as file:
        saved = json.load(file)
        for room, items in saved:
            house.append(room)
            values.append((room, items))
    print("House loaded.")


def commands():
    print("What action would you like to take?")
    print("     [A]dd an item to a room")
    print("     [C]reate a new room")
    print("     [L]ist all items in the house by room")
    print("     [R]ooms in the house")
    print("     [S]ave house and contents")
    print("     [O]pen previous saved file")
    print("     E[X]it application")
    print("     [?] Help")


def run_app():
    print(HEADER)
    commands()
    while True:
        action = input("> ").lower()

        if action == 'a':
            add_item()
        elif action == 'c':
            create_room()
        elif action == 'l':
            list_all()
        elif action == 'r':
            see_rooms()
        elif action == 's':
            save()
        elif action == 'o':
            open_previous()
        elif action == 'x':
            break
        elif action == '?':
            commands()
        else:
            print("Sorry I couldn't understand that command. Press ? for help.")


if __name__ == "__main__":
    run_app()
