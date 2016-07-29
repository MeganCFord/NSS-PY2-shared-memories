import pickle
import sys
import time


class Mary:
    '''
    Mary and Margaret share memories. This class, when run with a command line argument, adds a memory to Mary's memories and prints all the memories.
    Without an argument, it simply prints all the memories.

    Arguments: 1 optional string message. ex "this is a  message."
    '''
    def __init__(self):
        self.memories_list = []
        self.mary_memories_library = {"Mary": [], "Margaret": []}
        self.deserialize()

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
        runs automatically after deserialization, because a .txt file returns a list. puts each message into its appropriate key ("mary" or "margaret") in the mary_memories_library dictionary.

        Arguments: none
        '''
        for memory in self.memories_list:
            if memory[0] == "G":
                self.mary_memories_library["Margaret"].append(memory[1:])
            else:
                self.mary_memories_library["Mary"].append(memory[1:])

    def add_to_mary_memories(self, message):
        '''
        runs in init. Adds a string message to the list of mary's memories in mary_memories_library dictionary, then rewrites memories.txt file to include new message via serialization.

        Arguments: one string message.
        '''
        self.mary_memories_library["Mary"].append(message)
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
        for mary_memory in self.mary_memories_library["Mary"]:
            self.memories_list.append("M" + mary_memory)
        for margaret_memory in self.mary_memories_library["Margaret"]:
            self.memories_list.append("G" + margaret_memory)

    def print_out_messages(self):
        '''
        prints out messages in mary_memories_library in format.

        Arguments: none
        '''
        print("MARY: ")
        for mary_memory in self.mary_memories_library["Mary"]:
            print("  " + mary_memory)
        print("MARGARET: ")
        for margaret_memory in self.mary_memories_library["Margaret"]:
            print("  " + margaret_memory)


if __name__ == '__main__':
    # run: if mary.py is run with a command line argument, we add the message then print all the messages. if there is no command line argument, we simply print all the messages.
    app = Mary()
    message = sys.argv[1] if len(sys.argv) > 1 else None

    if message is not None:
        print("adding new message \n")
        app.add_to_mary_memories(message)
    else:
        print("printing all messages \n")

    time.sleep(.6)
    app.print_out_messages()
