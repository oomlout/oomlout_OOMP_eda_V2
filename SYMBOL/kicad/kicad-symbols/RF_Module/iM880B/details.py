
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "iM880B"
    hexID = "SZKRFMOIM88B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'iM880A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'iM880B', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.wireless-solutions.de/images/stories/downloads/Radio%20Modules/iM880B/General_Information/iM880B_Datasheet_V1_0.pdf', 'kicadSymbolki_keywords': 'IOT LoRa', 'kicadSymbolki_description': 'IMST Long Range Radio Module - LoRa Alliance Certified'}])
    newPart['name'].append('iM880B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

