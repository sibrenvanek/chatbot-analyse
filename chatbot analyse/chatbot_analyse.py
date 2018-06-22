import inputHandler
import database


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
    print("Please provide a keyword")
    keyword = input()

def newInput(UserInput):
    userinput = input()
    if userinput == "Y":
        print("Please provide a response for this sentence")
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

    inputHandler.handleNewInput("Are you enjoying life?","Is this life?")

    while notstop:
        userinput = input()
        if not RunCommand(userinput):
            response = inputHandler.handleInput(userinput)
            print(response)
            if response == "I couldn't find anything, can you help me by adding a response? Y/N":
                newInput(userinput)

main()