class Stack:
    def __init__(self):
        self.history = []

    def undo(self):
        if len(self.history) > 0:
            return self.history.pop()
        else:
            return None
