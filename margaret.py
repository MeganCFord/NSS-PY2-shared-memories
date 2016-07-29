import pickle
import sys
import time


class Margaret:
    '''
    Mary and Margaret share memories. This class, when run with a command line argument, adds a memory to Margaret's memories and prints all the memories.
    Without an argument, it simply prints all the memories.

    Arguments: 1 optional string message. ex "this is a  message."

    methods: deserialize, add_to_margaret_memories, serialize, print_out_messages

    '''
    def __init__(self):
        self.margaret_memories_library = self.deserialize()

    def deserialize(self):
        '''
        opens memories.txt file and puts results into self.memories_list. automatically runs dictionaryize function to convert list to dictionary.

        Arguments: none
        '''
        try:
            with open('memories.txt', 'rb') as m:
                library = pickle.load(m)

        except FileNotFoundError:
                library = {"Mary": [], "Margaret": []}

        return library

    def add_to_margaret_memories(self, message):
        '''
        runs in init. Adds a string message to the list of margaret's memories in margaret_memories_library dictionary, then rewrites memories.txt file to include new message via serialization.

        Arguments: one string message.
        '''
        self.margaret_memories_library["Margaret"].append(message)
        self.serialize()

    def serialize(self):
        '''
        Writes the contents of self.margaret_memories_library into a .txt file called 'memories.txt'.

        Arguments: none
        '''
        with open('memories.txt', 'wb+') as m:
            pickle.dump(self.margaret_memories_library, m)


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
    # run: if mary.py is run with a command line argument, we add the message then print all the messages. if there is no command line argument, we simply print all the messages.
    app = Margaret()
    message = sys.argv[1] if len(sys.argv) > 1 else None

    if message is not None:
        print("adding new message \n")
        app.add_to_margaret_memories(message)
    else:
        print("printing all messages \n")

    time.sleep(.6)
    app.print_out_messages()
