import database

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
                    for p in possibleResponses:
                        if p[0] == k.Answer:
                            p = (p[0], p[1] + 1)
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