
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Jumper"
    oIndex = "Jumper_2_Open"
    hexID = "SZKJJ2OPEN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'JP', 'kicadSymbolValue': 'Jumper_2_Open', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'Jumper SPST', 'kicadSymbolki_description': 'Jumper, 2-pole, open', 'kicadSymbolki_fp_filters': 'Jumper* TestPoint*2Pads* TestPoint*Bridge*'}])
    newPart['name'].append('Jumper : Jumper_2_Open')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

