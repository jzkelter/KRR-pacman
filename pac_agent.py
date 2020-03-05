from pythonian import *

class PacAgent(Pythonian):
    name = "PacAgent" # This is the name of the agent to register with

    def __init__(self, **kwargs):
        super(PacAgent, self).__init__(**kwargs)
        last_message = None

    


    def insert_to_Companion(self, data):
        print('inserting data into Companion working memory: ' + str(data))
        Pythonian.insert_data(self, 'session-reasoner', data) # , wm_only=True)

    def insert_a_microtheory(self, data, mt_name):
        Pythonian.insert_microtheory(self, 'session-reasoner', data, mt_name)

    def insert_to_a_microtheory(self, data, mt_name):
        Pythonian.insert_to_microtheory(self, 'session-reasoner', data, mt_name)



if __name__ == "__main__":
    # logger.setLevel(logging.DEBUG)
    a = PacAgent(host='localhost', port=9000, localPort=8950)


# cd Documents\companions-exe-02-07-2020\pythonian
# from pac_agent import PacAgent
# a.insert_to_Companion('(isa Maryam Student)')


# Pythonian.insert_microtheory(a, 'session-reasoner', '(isa Maryam Student)', 'Pac-tick1', wm_only=True)
# Pythonian.insert_to_microtheory(a, 'session-reasoner', '(isa Nick Student)', 'Pac-tick1')
