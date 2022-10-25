
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "CircuitBreaker_2P_US"
    hexID = "SZKDEVICECIRCUITBREAKER2PUS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'CB', 'kicadSymbolValue': 'CircuitBreaker_2P_US', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'CB 2P', 'kicadSymbolki_description': 'Double pole circuit breaker, US symbol'}])
    newPart['name'].append('Device : CircuitBreaker_2P_US')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

