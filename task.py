class Task:

    def __init__(self, name):
        self.name = name
        self.state = "incomplete"

    def getName(self):
        return self.name
    
    def getState(self):
        return self.state

    def setName(self, name):
        self.name = name

    def setState(self, state):
        self.state = state

    def showTask(self):
        return f'name: {self.name}, state: {self.state}'