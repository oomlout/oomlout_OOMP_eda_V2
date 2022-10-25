
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Speaker_Crystal"
    hexID = "SZKDEVICESPEAKERX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'LS', 'kicadSymbolValue': 'Speaker_Crystal', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'crystal speaker ultrasonic transducer', 'kicadSymbolki_description': 'Crystal speaker/transducer'}])
    newPart['name'].append('Device : Speaker_Crystal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

