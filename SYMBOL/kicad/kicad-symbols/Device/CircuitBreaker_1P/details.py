
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "CircuitBreaker_1P"
    hexID = "SZKDEVICECIRCUITBREAKER1P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'CB', 'kicadSymbolValue': 'CircuitBreaker_1P', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'CB', 'kicadSymbolki_description': 'Single pole circuit breaker'}])
    newPart['name'].append('Device : CircuitBreaker_1P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

