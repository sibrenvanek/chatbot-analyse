import inputHandler
import database
from chatterbot import ChatBot
import sqlite3

class Command:
    def __init__(self, command, callback):
        self.command = command
        self.callback = callback

    def GetCommand(self):
        return self.command

    def GetCallback(self):
        return self.callback

# Command array
commands = []

# Adds a command to the command handler
def RegisterCommand(command, callback):
    cmd = Command(command, callback)
    commands.append(cmd)

# Run a defined command, or return false if it does not exist
def RunCommand(command):
    for cmd in commands:
        if cmd.GetCommand() == command:
            cmd.GetCallback()()
            return True

    return False

notstop = True

def stop():
    global notstop
    notstop = False

def addKeywordAndResponse(response):
    print("Please provide a keyword".upper())
    keyword = input()

def newInput(UserInput):
    userinput = input()
    if userinput == "Y":
        print("Please provide a response for this sentence".upper())
        newresponse = input()
        print(inputHandler.handleNewInput(UserInput, newresponse))
    else:
        return

def main():
    global notstop

    #hier ergens kan je het aanroepen

    RegisterCommand("-q", lambda : stop())
    RegisterCommand("-k", lambda : database.printKeywords())

    #hier ergens kan je het aanroepen

    #inputHandler.handleNewInput("Are you enjoying life?","Is this life?")

    while notstop:
        userinput = input()
        if not RunCommand(userinput):
            response = inputHandler.handleInput(userinput)
            print(response.upper())
            if response == "I couldn't find anything, can you help me with a response? Y/N":
                newInput(userinput)

#conn = sqlite3.connect('db.sqlite3')
#c = conn.cursor()
#data = c.execute('SELECT * FROM response')
#for d in data:
#    print(d[0])
#    inputHandler.handleNewInput(d[1],d[4])
main()