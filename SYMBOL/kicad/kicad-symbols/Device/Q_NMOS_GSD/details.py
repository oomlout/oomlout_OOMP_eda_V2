
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Q_NMOS_GSD"
    hexID = "SZKDEVICEQNMOSGSD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'Q_NMOS_GSD', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'transistor NMOS N-MOS N-MOSFET', 'kicadSymbolki_description': 'N-MOSFET transistor, gate/source/drain'}])
    newPart['name'].append('Device : Q_NMOS_GSD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

