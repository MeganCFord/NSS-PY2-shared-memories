import pickle
import sys


class Margaret:
    def __init__(self, message):
        self.memories_list = []
        self.margaret_memories_library = {"Mary": [], "Margaret": []}
        self.deserialize()
        self.add_to_margaret_memories(message)

    def deserialize(self):
        '''
        opens memories.txt file and puts results into self.memories_list. automatically runs dictionaryize function to convert list to dictionary.

        Arguments: none
        '''
        try:
            with open('memories.txt', 'rb') as m:
                self.memories_list = pickle.load(m)
                print('loaded list of memories')

        except FileNotFoundError:
                self.memories_list = []
                print('list was empty')

        self.dictionaryize()

    def dictionaryize(self):
        '''
        runs automatically after deserialization, because a .txt file returns a list. puts each message into its appropriate key ("mary" or "margaret") in the margaret_memories_library dictionary.

        Arguments: none
        '''
        for memory in self.memories_list:
            if memory[0] == "G":
                self.margaret_memories_library["Margaret"].append(memory[1:])
            else:
                self.margaret_memories_library["Mary"].append(memory[1:])

    def add_to_margaret_memories(self, message):
        '''
        runs in init. Adds a string message to the list of margaret's memories in margaret_memories_library dictionary, then rewrites memories.txt file to include new message via serialization.

        Arguments: one string message.
        '''
        self.margaret_memories_library["Margaret"].append(message)
        self.serialize()

    def serialize(self):
        '''
        Writes the contents of self.memories_list into a .txt file called 'memories.txt'. First it converts the memories_library back to a list via self.rebuild_memories_list.

        Arguments: none
        '''
        self.rebuild_memories_list()
        with open('memories.txt', 'wb+') as m:
            pickle.dump(self.memories_list, m)

    def rebuild_memories_list(self):
        '''
        runs before serialization, after addition of new memory to memories dictionary. Converts the entire dictionary back into a list, to be written to txt file.

        Arguments: none
        '''
        self.memories_list = []
        for mary_memory in self.margaret_memories_library["Mary"]:
            self.memories_list.append("M" + mary_memory)
        for margaret_memory in self.margaret_memories_library["Margaret"]:
            self.memories_list.append("G" + margaret_memory)

    def print_out_messages(self):
        '''
        prints out messages in margaret_memories_library in format.

        Arguments: none
        '''
        print("MARY: ")
        for mary_memory in self.margaret_memories_library["Mary"]:
            print("  " + mary_memory)
        print("MARGARET: ")
        for margaret_memory in self.margaret_memories_library["Margaret"]:
            print("  " + margaret_memory)


if __name__ == '__main__':
    app = Margaret(sys.argv[1])
    app.print_out_messages()
