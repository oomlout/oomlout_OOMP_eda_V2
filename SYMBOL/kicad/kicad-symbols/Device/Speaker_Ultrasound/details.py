
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Speaker_Ultrasound"
    hexID = "SZKDEVICESPEAKERULTRASOUND"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Speaker_Crystal', 'kicadSymbolReference': 'LS', 'kicadSymbolValue': 'Speaker_Ultrasound', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'crystal speaker ultrasonic transducer', 'kicadSymbolki_description': 'Ultrasonic transducer'}])
    newPart['name'].append('Device : Speaker_Ultrasound')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

