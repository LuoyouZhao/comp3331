from socket import *
from Message import *
from ContactLog import *
import sys
import threading
import random


# this function change block situation to false after required time
def resume(user):
    time.sleep(int(blockDuration))
    user.block = False
    return


# this function repetitively receive commands from clients
def command(connectSocket):
    while True:
        mes = unpackMessage(connectSocket.recv(2048))
        try:
            user = accounts[mes.data[0]]
        except BaseException as e:
            sendData = [False, "Cannot find user, please check again"]
            connectSocket.send(packMessage(None, sendData))
            continue
        if user.block:
            sendData = [False, "Your account is blocked due to multiple login failures. Please try again later"]
            connectSocket.send(packMessage(None, sendData))
        elif user.check(mes.data[0], mes.data[1]):
            sendData = [True, "Welcome to BlueTrace"]
            connectSocket.send(packMessage(None, sendData))
            user.wrongTime = 0
            print("User " + user.username + " login")
            break
        elif user.wrongTime == 2:
            sendData = [False, "Your account is blocked due to multiple login failures. Please try again later"]
            connectSocket.send(packMessage(None, sendData))
            user.block = True
            block = threading.Thread(target=resume, args=(user,))
            block.start()
        else:
            sendData = [False, "Incorrect password, please check again"]
            connectSocket.send(packMessage(None, sendData))
            user.wrongTime += 1
    while True:
        mes = unpackMessage(connectSocket.recv(2048))
        command = mes.command
        if command == "download":
            # to download tempID need valid username and password
            if accounts[mes.data[0]].check(mes.data[0], mes.data[1]):
                ID = findTempId(mes.data[0])
                connectSocket.send(packMessage(None, ["your tempID is " + ID.tempId, ID]))
            else:
                connectSocket.send(packMessage(None, ["ERROR: invalid certification"]))
        elif command == "upload":
            print("received contact log from " + user.username)
            for log in mes.data:
                print(log.tempId + ", " + log.startTime + ", " + log.expireTime + ";")
            print("Contact log checking")
            for log in mes.data:
                print(tempIDs[log] + ", " + log.startTime + ", " + log.tempId + ";")
            connectSocket.send(packMessage(None, ["upload successfully"]))
        elif command == "logout":
            connectSocket.close()
            print("User " + user.username + " logout")
            break


# this function find tempID for user, if tempID is invalid, it create a new tempID
def findTempId(username):
    if username in i_tempIDs.keys() and i_tempIDs[username].isValid():
        return i_tempIDs[username]
    else:
        ID = generateLog(str(random.randint(10000000000000000000, 99999999999999999999)))
        i_tempIDs[username] = ID
        tempIDs[ID] = username
        f = open("tempIDs.txt", mode='a')
        f.write(username + " " + ID.tempId + " " + ID.startTime + " " + ID.expireTime + "\n")
        f.close()
        return ID


file = open("credentials.txt", mode='r')
accounts = {}
for line in file.readlines():
    line = line.rstrip("\n")
    string = line.split(" ")
    accounts[string[0]] = User(string[0], string[1])
file.close()

# read tempIDs.txt, put it in dictionary tempIDs and i_tempIDs
file = open("tempIDs.txt", mode='r')
tempIDs = {}
for line in file.readlines():
    line = line.rstrip("\n")
    string = line.split(" ")
    tempIDs[Log(string[1], string[2] + " " + string[3], string[4] + " " + string[5])] = string[0]
i_tempIDs = {v: k for k, v in tempIDs.items()}
file.close()

serverPort = int(sys.argv[1])
blockDuration = sys.argv[2]
serverName = '127.0.0.1'
currentPort = serverPort + 1
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(5)

# server create a new threading with a unique port number whenever a new client login,
while True:
    clientSocket, addr = serverSocket.accept()
    data = [currentPort]
    clientSocket.send(packMessage(None, data))
    Socket = socket(AF_INET, SOCK_STREAM)
    Socket.bind((serverName, currentPort))
    Socket.listen(5)
    connectSocket, add = Socket.accept()
    thread = threading.Thread(target=command, args=(connectSocket,))
    thread.start()
    currentPort += 1
