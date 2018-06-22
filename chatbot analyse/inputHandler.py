import database

lastResponse = ""

def handleNewInput(userinput, response):
    words = userinput.split(" ")
    for w in words:
        database.addKeyword(w, response)
    return "Thank you for this new response"


def handleInput(userinput):
    response = ""
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
        nextBestResponse = ("",0)
        for p in possibleResponses:
            if not p == bestResponse:
                if(p[1] > bestResponse[1]):
                    nextBestResponse = bestResponse
                    bestResponse = p 
        global lastResponse
        if bestResponse[0] == lastResponse:
            response = nextBestResponse[0]
        else:
            response = bestResponse[0]

    else:
        response = "I couldn't find anything, can you help me with a response? Y/N"

    lastResponse = response
    return response