import pickle
import sys
import time


class Mary:
    '''
    Mary and Margaret share memories. This class, when run with a command line argument, adds a memory to Mary's memories and prints all the memories.
    Without an argument, it simply prints all the memories.

    Arguments: 1 optional string message. ex "this is a  message."

    methods: deserialize, add_to_mary_memories, serialize, print_out_messages
    '''
    def __init__(self):
        self.mary_memories_library = self.deserialize()

    def deserialize(self):
        '''
        opens memories.txt file and returns the results, which are a dictionary. Creates file if none exists.

        Arguments: none
        '''
        try:
            with open('memories.txt', 'rb') as m:
                library = pickle.load(m)

        except FileNotFoundError:
                library = {"Mary": [], "Margaret": []}
        return library

    def add_to_mary_memories(self, message):
        '''
        runs in init. Adds a string message to the list of mary's memories in mary_memories_library dictionary, then rewrites memories.txt file to include new message via serialization.

        Arguments: one string message.
        '''
        self.mary_memories_library["Mary"].append(message)
        self.serialize()

    def serialize(self):
        '''
        Writes the contents of self.mary_memories_library into a .txt file called 'memories.txt'.

        Arguments: none
        '''
        with open('memories.txt', 'wb+') as m:
            pickle.dump(self.mary_memories_library, m)

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
