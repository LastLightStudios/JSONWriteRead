import json
import jsonpickle
from RoomManager import RoomManager, Room
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    room_manager = RoomManager()
    room_manager.generate_default_map()

    file1 = open(r"Maps\NewFile.txt", "w")
    frozen = jsonpickle.encode(room_manager, indent=4, keys=True)
    file1.write(frozen)
    #frozen = file1.read()
    file1.close()
    thawed = jsonpickle.decode(frozen)
    #assert room_manager.rooms["Left Room"] == thawed.rooms["Left Room"]
    print(thawed.rooms["Left Room"].name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
