import database

lastResponse = ["","","","","","","","","",""]

def handleNewInput(userinput, response):
    userinput = userinput.upper()
    response = response.upper()
    newUserInput = ""
    newResponse = ""
    for c in userinput:
        if c == 'A' or c == 'B' or c == 'C' or c == 'D' or c == 'E' or c == 'F' or c == 'G' or c == 'H' or c == 'I' or c == 'J' or c == 'K' or c == 'L' or c == 'M' or c == 'N' or c == 'O' or c == 'P' or c == 'Q' or c == 'R' or c == 'S' or c == 'T' or c == 'U' or c == 'V' or c == 'W' or c == 'X' or c == 'Y' or c == 'Z' or c == '0' or c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9' or c == ' ':
            newUserInput += c
    for c in response:
        if c == 'A' or c == 'B' or c == 'C' or c == 'D' or c == 'E' or c == 'F' or c == 'G' or c == 'H' or c == 'I' or c == 'J' or c == 'K' or c == 'L' or c == 'M' or c == 'N' or c == 'O' or c == 'P' or c == 'Q' or c == 'R' or c == 'S' or c == 'T' or c == 'U' or c == 'V' or c == 'W' or c == 'X' or c == 'Y' or c == 'Z' or c == '0' or c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9' or c == ' ':
            newResponse += c
    userinput = newUserInput
    response = newResponse
    words = userinput.split(" ")
    for w in words:
        database.addKeyword(w, response)
    return "Thank you for this new response".upper()


def handleInput(userinput):
    response = ""
    userinput = userinput.upper()
    newUserInput = ""
    for c in userinput:
        if c == 'A' or c == 'B' or c == 'C' or c == 'D' or c == 'E' or c == 'F' or c == 'G' or c == 'H' or c == 'I' or c == 'J' or c == 'K' or c == 'L' or c == 'M' or c == 'N' or c == 'O' or c == 'P' or c == 'Q' or c == 'R' or c == 'S' or c == 'T' or c == 'U' or c == 'V' or c == 'W' or c == 'X' or c == 'Y' or c == 'Z' or c == '0' or c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9' or c == ' ':
            newUserInput += c
    userinput = newUserInput
    possibleResponses = []
    words = userinput.split(" ")
    keywords = database.getAllKeywords()
    for k in keywords:
        keyword = k.Keyword
        for w in words:
            if w == keyword:
                check = True
                for p in possibleResponses:
                    if p[0] == k.Answer:
                        check = False
                if check:
                    possibleResponses.append((k.Answer, 1))
                else:
                    for i in range(0,len(possibleResponses)):
                        if possibleResponses[i][0] == k.Answer:
                            possibleResponses[i] = (possibleResponses[i][0], possibleResponses[i][1] + 1)
    if len(possibleResponses) > 0:
        bestResponse = possibleResponses[0]
        nextBestResponses = [("",0),("",0),("",0),("",0),("",0),("",0),("",0),("",0),("",0),("",0)]
        for p in possibleResponses:
            if not p == bestResponse:
                if p[1] > bestResponse[1]:
                    nextBestResponses[9] = nextBestResponses[8]
                    nextBestResponses[8] = nextBestResponses[7]
                    nextBestResponses[7] = nextBestResponses[6]
                    nextBestResponses[6] = nextBestResponses[5]
                    nextBestResponses[5] = nextBestResponses[4]
                    nextBestResponses[4] = nextBestResponses[3]
                    nextBestResponses[3] = nextBestResponses[2]
                    nextBestResponses[2] = nextBestResponses[1]
                    nextBestResponses[1] = nextBestResponses[0]
                    nextBestResponses[0] = bestResponse
                    bestResponse = p 
                elif p[1] == bestResponse[1]:
                    if p[1] > nextBestResponses[0][1]:
                        nextBestResponses[0] = p
                    elif p[1] > nextBestResponses[1][1]:
                        nextBestResponses[1] = p
                    elif p[1] > nextBestResponses[2][1]:
                        nextBestResponses[2] = p
                    elif p[1] > nextBestResponses[3][1]:
                        nextBestResponses[3] = p
                    elif p[1] > nextBestResponses[4][1]:
                        nextBestResponses[4] = p
                    elif p[1] > nextBestResponses[5][1]:
                        nextBestResponses[5] = p
                    elif p[1] > nextBestResponses[6][1]:
                        nextBestResponses[6] = p
                    elif p[1] > nextBestResponses[7][1]:
                        nextBestResponses[7] = p
                    elif p[1] > nextBestResponses[8][1]:
                        nextBestResponses[8] = p
                    elif p[1] > nextBestResponses[9][1]:
                        nextBestResponses[9] = p
        global lastResponse
        for i in range(0,10):
            bestResponsetxt = bestResponse[0]
            if bestResponsetxt in lastResponse:
                bestResponse = nextBestResponses[i]
        response = bestResponse[0]

    else:
        response = "I couldn't find anything, can you help me with a response? Y/N"

    
    lastResponse[9] = lastResponse[8]
    lastResponse[8] = lastResponse[7]
    lastResponse[7] = lastResponse[6]
    lastResponse[6] = lastResponse[5]
    lastResponse[5] = lastResponse[4]
    lastResponse[4] = lastResponse[3]
    lastResponse[3] = lastResponse[2]
    lastResponse[2] = lastResponse[1]
    lastResponse[1] = lastResponse[0]
    lastResponse[0] = response
    return response