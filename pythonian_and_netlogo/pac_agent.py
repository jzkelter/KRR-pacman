from pythonian import *

class PacAgent(Pythonian):
    name = "PacAgent" # This is the name of the agent to register with

    def __init__(self, **kwargs):
        super(PacAgent, self).__init__(**kwargs)
        self.directions = None
        self.new_direction = False

    def insert_to_Companion(self, data, wm_only=False):
        print('inserting data into Companion working memory: ' + str(data))
        Pythonian.insert_data(self, 'session-reasoner', data, wm_only=wm_only)  # wm_only=True seems to break

    def insert_a_microtheory(self, data, mt_name):
        Pythonian.insert_microtheory(self, 'session-reasoner', data, mt_name)

    def insert_to_a_microtheory(self, data, mt_name, wm_only=False):

        Pythonian.insert_to_microtheory(self, 'session-reasoner', data, mt_name, wm_only=wm_only) # wm_only=True seems to break

    def ask_direction(self):
        self.new_direction = False
        self.ask_agent('session-reasoner', '(ist-Information PacPersonMt (directionToFace ?direction))')

    def receive_tell(self, msg, content):
        """Override to store content and reply
        with nothing

        Arguments:
            msg {KQMLPerformative} -- tell to be passed along in reply
            content {KQMLPerformative} -- tell from companions to be logged
        """
        # logger.debug('received tell: %s', content)  # lazy logging
        content = convert_to_list(content)
        print(content)
        self.directions = [str(c[2][1]) for c in content]
        self.new_direction = True
        print("Test print new direction: {}; direction: {}".format(self.new_direction, self.direction))
        reply_msg = KQMLPerformative('tell')
        reply_msg.set('sender', self.name)
        reply_msg.set('content', None)
        self.reply(msg, reply_msg)





if __name__ == "__main__":
    # logger.setLevel(logging.DEBUG)
    a = PacAgent(host='localhost', port=9000, localPort=8950, debug=False)


# cd Documents\companions-exe-02-07-2020\pythonian
# from pac_agent import PacAgent
# a = PacAgent(host='localhost', port=9000, localPort=8950, debug=False)
# a.ask_agent('session-reasoner', '(isa ?students Person)')

# a.insert_to_Companion('(isa Maryam Student)')

# a.ask_agent('session-reasoner', '(isa ?students Student)')

# Pythonian.insert_microtheory(a, 'session-reasoner', '(isa Maryam Student)', 'Pac-tick1', wm_only=True)
# Pythonian.insert_to_microtheory(a, 'session-reasoner', '(isa Nick Student)', 'Pac-tick1')

# (ist-Information Pac-tick2 (isa ?students Student))
