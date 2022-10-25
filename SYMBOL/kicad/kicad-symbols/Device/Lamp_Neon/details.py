
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Lamp_Neon"
    hexID = "SZKDEVICELAMPNEON"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'NE', 'kicadSymbolValue': 'Lamp_Neon', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'neon lamp', 'kicadSymbolki_description': 'Neon lamp'}])
    newPart['name'].append('Device : Lamp_Neon')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

