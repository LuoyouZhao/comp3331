from socket import *
from Message import *
from ContactLog import *
import threading
import sys

ServerIP = sys.argv[1]
serverPort = int(sys.argv[2])
udpPort = int(sys.argv[3])
preSocket = socket(AF_INET, SOCK_STREAM)
preSocket.connect((ServerIP, serverPort))
currentPort = unpackMessage(preSocket.recv(2048)).data[0]
preSocket.close()


# this function repetitively receive beacon from other users
def receiveBeacon(udpServer):
    while True:
        data, addr = udpServer.recvfrom(2048)
        newLog = unpackMessage(data).data
        print("received beacon: " + newLog.tempId + ", " + newLog.startTime + ", " + newLog.expireTime + ";")
        if newLog.isValid:
            print("The beacon is valid.")
            contactLogs[newLog] = time.time()
            print("receive time "+time2txt(contactLogs[newLog]))
            f = open("z5225024_contactlog.txt", mode='a')
            f.write(newLog.tempId + " " + newLog.startTime + " " + newLog.expireTime + "\n")
            f.close()
        else:
            print("The beacon is invalid.")


# this function update beacons in every 10 secs
def updateBeacon():
    while True:
        for log in list(contactLogs.keys()):
            if time.time() > contactLogs[log] + 180:
                del contactLogs[log]
        for log in contactLogs.keys():
            f = open("z5225024_contactlog.txt", mode='w')
            f.write(log.tempId + " " + log.startTime + " " + log.expireTime + "\n")
            f.close()
        time.sleep(10)


clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((ServerIP, currentPort))
# login part
while True:
    print("Please login\n")
    certification = [input("Username:"), input("Password:")]
    clientSocket.send(packMessage(None, certification))
    mes = unpackMessage(clientSocket.recv(2048))
    print(mes.data[1])
    if mes.data[0]:
        tempID = None
        break

# read z5225024_contactlog.txt
file = open("z5225024_contactlog.txt", mode='r')
contactLogs = {}
for line in file.readlines():
    line = line.rstrip("\n")
    string = line.split(" ")
    contactLogs[Log(string[0], string[1] + " " + string[2], string[3] + " " + string[4])] = time.time()
file.close()

serverADDR = ('', udpPort)
udpServer = socket(AF_INET, SOCK_DGRAM)
udpServer.bind(serverADDR)
receiveBeacon = threading.Thread(target=receiveBeacon, args=(udpServer,))
receiveBeacon.start()
updateBeacon = threading.Thread(target=updateBeacon, args=())
updateBeacon.start()
print("updating complete")

# receive commands from key board
while True:
    command = input()
    commands = string = command.split(" ")
    if command == "download":
        clientSocket.send(packMessage("download", certification))
        mes = unpackMessage(clientSocket.recv(2048))
        tempID = mes.data[1]
        print(mes.data[0])
    elif command == "upload":
        clientSocket.send(packMessage("upload", contactLogs))
        print(unpackMessage(clientSocket.recv(2048)).data[0])
    elif commands[0] == "Beacon":
        destADDR = (commands[1], int(commands[2]))
        udpClient = socket(AF_INET, SOCK_DGRAM)
        if tempID is None:
            print("need to download tempID first!")
        elif not tempID.isValid():
            print("invalid tempID, please download again.")
        else:
            try:
                udpClient.sendto(packMessage("Beacon", tempID), destADDR)
            except BaseException as e:
                print("send unsuccessfully, please check your network, destIp, or destPort.")
                continue
            print("send successfully")
    elif command == "logout":
        clientSocket.send(packMessage("logout", []))
        clientSocket.close()
        print("logout successfully")
        sys.exit()
    elif command == "help":
        print("download                      ---download tempID")
        print("upload                        ---upload contactLogs")
        print("Beacon <dest IP> <dest port>  ---send Beacon")
        print("logout                        ---logout")
    else:
        print("invalid command, type help for usage")
