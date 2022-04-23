'''
    A general module with all necessary classes implemented.
'''


class Room:
    '''
        Room class.
    '''

    def __init__(self, name: str) -> None:
        self.name = name
        self.description = None
        self.item = None
        self.character = None
        self.linked_rooms = {}

    def set_character(self, new_character):
        '''
            A setter for a character.
        '''
        self.character = new_character

    def get_character(self):
        '''
            A getter for a character.
        '''
        return self.character

    def set_description(self, description):
        '''
            A setter for a description.
        '''
        self.description = description

    def get_description(self):
        '''
            A getter for a character.
        '''
        return self.description

    def set_name(self, name):
        '''
            A setter for a name.
        '''
        self.name = name

    def get_name(self):
        '''
            A getter for a name.
        '''
        return self.name

    def set_item(self, item_name):
        '''
            A setter for an item.
        '''
        self.item = item_name

    def get_item(self):
        '''
            A getter for an item.
        '''
        return self.item

    def link_room(self, other_room: object, side: str):
        '''
        Links a room to one of four possible ways to come.
        '''
        self.linked_rooms[side] = other_room

    def move(self, direction):
        '''
            Returns a room that is situated up to direction.
        '''
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("Не можна туди.")
            return self

    def get_details(self):
        '''
            Prints info about current room.
        '''
        print(self.name)
        dashes = "-" * len(self.name)
        print(dashes)
        print(self.description)
        for direction, room in self.linked_rooms.items():
            print("Щоб пройти до вулиці " + room.get_name() + ", треба йти на " + direction)
        print()


class Item:
    '''
        An item class.
    '''

    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, description):
        '''
            A setter for a description.
        '''
        self.description = description

    def get_description(self):
        '''
            A getter for a description.
        '''
        return self.description

    def set_name(self, name):
        '''
            A setter for a name.
        '''
        self.name = name

    def get_name(self):
        '''
            A setter for a name.
        '''
        return self.name

    def describe(self):
        '''
            Prints the info about item.
        '''
        print(self.description)


class Character:
    '''
        A character class.
    '''

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None

    def describe(self):
        '''
            Prints info about character.
        '''
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        '''
            A setter for a conversation.
        '''
        self.conversation = conversation

    def talk(self):
        '''
            Returns a phrase of a character if he/she/it wants to talk.
        '''
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to speak.")


class Enemy(Character):
    '''
        An Enemy class.
    '''
    enemies_defeated = 0

    def __init__(self, name, description):
        super().__init__(name, description)
        self.weakness = None
        self.is_defeated = False

    def fight(self, combat_item):
        '''
            If combat_item is a weak spot - returns True, and
            increases the enemies_defeated by 1. Otherwise returns False.
        '''
        if combat_item == self.weakness:
            print("Ти відкараскався від " + self.name + " завдяки предмету " + combat_item)
            Enemy.enemies_defeated += 1
            self.is_defeated = True
            return True
        print(self.name + " накинувся на тебе! Ти програв.")
        return False

    def get_enemies_defeated(self):
        '''
            Returns the count of enemies defeated.
        '''
        return Enemy.enemies_defeated

    def set_weakness(self, item_weakness):
        '''
            Sets a weak spot item for the enemy.
        '''
        self.weakness = item_weakness

    def get_weakness(self):
        '''
            Returns a weak spot item for the enemy.
        '''
        return self.weakness
