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

def main():
    global notstop

    RegisterCommand("-q", lambda : exit()
                    )
    while notstop:
        userinput = input()
        if not RunCommand(userinput):
            print(inputHandler.handleInput(userinput))
            
main()