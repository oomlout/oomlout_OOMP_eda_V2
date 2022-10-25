
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Q_TRIAC_GA2A1"
    hexID = "SZKDEVICEQTRIACGA2A1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'Q_TRIAC_GA2A1', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'TRIAC', 'kicadSymbolki_description': 'Triode for alternating current, gate/anode2/anode1'}])
    newPart['name'].append('Device : Q_TRIAC_GA2A1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

