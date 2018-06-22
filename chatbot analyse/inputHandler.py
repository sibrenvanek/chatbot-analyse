import database

def handleNewInput(userinput, response):
    userinput = userinput.upper()
    response = response.upper()
    newUserInput = ""
    newResponse = ""
    for c in userinput:
        if c == 'A' or c == 'B' or c == 'C' or c == 'D' or c == 'E' or c == 'F' or c == 'G' or c == 'H' or c == 'I' or c == 'J' or c == 'K' or c == 'L' or c == 'M' or c == 'N' or c == 'O' or c == 'P' or c == 'Q' or c == 'R' or c == 'S' or c == 'T' or c == 'U' or c == 'V' or c == 'W' or c == 'X' or c == 'Y' or c == 'Z' or c == '0' or c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9':
            newUserInput += c
    for c in response:
        if c == 'A' or c == 'B' or c == 'C' or c == 'D' or c == 'E' or c == 'F' or c == 'G' or c == 'H' or c == 'I' or c == 'J' or c == 'K' or c == 'L' or c == 'M' or c == 'N' or c == 'O' or c == 'P' or c == 'Q' or c == 'R' or c == 'S' or c == 'T' or c == 'U' or c == 'V' or c == 'W' or c == 'X' or c == 'Y' or c == 'Z' or c == '0' or c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9':
            newResponse += c
    userinput = newUserInput
    response = newResponse
    words = userinput.split(" ")
    for w in words:
        database.addKeyword(w, response)
    return "Thank you for this new response".upper()


def handleInput(userinput):
    response = ""
    newUserInput = ""
    for c in userinput:
        if c == 'A' or c == 'B' or c == 'C' or c == 'D' or c == 'E' or c == 'F' or c == 'G' or c == 'H' or c == 'I' or c == 'J' or c == 'K' or c == 'L' or c == 'M' or c == 'N' or c == 'O' or c == 'P' or c == 'Q' or c == 'R' or c == 'S' or c == 'T' or c == 'U' or c == 'V' or c == 'W' or c == 'X' or c == 'Y' or c == 'Z' or c == '0' or c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9':
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
        for p in possibleResponses:
            if not p == bestResponse:
                if(p[1] > bestResponse[1]):
                    bestResponse = p    
        response = bestResponse[0]
    else:
        response = "I couldn't find anything, can you help me with a response? Y/N"
    return response