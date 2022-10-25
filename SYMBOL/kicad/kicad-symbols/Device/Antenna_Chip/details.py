
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Antenna_Chip"
    hexID = "SZKDEVICEANTENNACHIP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'AE', 'kicadSymbolValue': 'Antenna_Chip', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'antenna', 'kicadSymbolki_description': 'Ceramic chip antenna with pin for PCB trace'}])
    newPart['name'].append('Device : Antenna_Chip')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

