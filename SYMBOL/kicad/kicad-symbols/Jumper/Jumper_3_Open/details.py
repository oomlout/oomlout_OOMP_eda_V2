
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Jumper"
    oIndex = "Jumper_3_Open"
    hexID = "SZKJJ3OPEN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'JP', 'kicadSymbolValue': 'Jumper_3_Open', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'Jumper SPDT', 'kicadSymbolki_description': 'Jumper, 3-pole, both open', 'kicadSymbolki_fp_filters': 'Jumper* TestPoint*3Pads* TestPoint*Bridge*'}])
    newPart['name'].append('Jumper : Jumper_3_Open')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

