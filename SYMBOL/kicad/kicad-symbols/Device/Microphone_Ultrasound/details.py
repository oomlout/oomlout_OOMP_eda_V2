
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Microphone_Ultrasound"
    hexID = "SZKDEVICEMPHONEULTRASOUND"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Microphone_Crystal', 'kicadSymbolReference': 'MK', 'kicadSymbolValue': 'Microphone_Ultrasound', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'microphone ultrasound crystal', 'kicadSymbolki_description': 'Ultrasound receiver'}])
    newPart['name'].append('Device : Microphone_Ultrasound')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

