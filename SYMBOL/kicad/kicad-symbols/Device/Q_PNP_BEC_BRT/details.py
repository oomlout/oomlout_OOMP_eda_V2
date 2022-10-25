
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Q_PNP_BEC_BRT"
    hexID = "SZKDEVICEQPNPBECBRT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'Q_PNP_BEC_BRT', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'transistor PNP', 'kicadSymbolki_description': 'PNP bias resistor transistor, base/emitter/collector'}])
    newPart['name'].append('Device : Q_PNP_BEC_BRT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

