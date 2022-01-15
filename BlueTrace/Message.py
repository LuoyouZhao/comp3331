import pickle


class Message:
    def __init__(self, command, data):
        self.command = command
        self.data = data

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.wrongTime = 0
        self.block = False

    def check(self, username, password):
        return self.username == username and self.password == password


def packMessage(command, data):
    mes = Message(command, data)
    return pickle.dumps(mes)


def unpackMessage(mes):
    return pickle.loads(mes)
