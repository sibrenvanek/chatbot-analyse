import database

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
                            p[1] += 1
    bestResponse = possibleResponses[0]
    for p in possibleResponses:
        if not p == bestResponse:
            if(p[1] > bestResponse[1]):
                bestResponse = p
    response = bestResponse[0]
    return response