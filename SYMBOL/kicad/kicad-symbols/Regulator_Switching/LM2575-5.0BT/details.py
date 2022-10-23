
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2575-5.0BT"
    hexID = "SZKREGULATORSWITCHINGLM25755BT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2576HVT-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2575-5.0BT', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-5_Vertical', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/lm2575.pdf', 'kicadSymbolki_keywords': 'Buck regulator Switcher', 'kicadSymbolki_description': 'Fixed 5.0V 52kHz Simple 1A Buck Regulator, TO-220-5', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('LM2575-5.0BT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

