
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Jumper"
    oIndex = "Jumper_2_Bridged"
    hexID = "SZKJJ2BRIDGED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'JP', 'kicadSymbolValue': 'Jumper_2_Bridged', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'Jumper SPST', 'kicadSymbolki_description': 'Jumper, 2-pole, closed/bridged', 'kicadSymbolki_fp_filters': 'Jumper* TestPoint*2Pads* TestPoint*Bridge*'}])
    newPart['name'].append('Jumper : Jumper_2_Bridged')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

