
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BCV61"
    hexID = "SZKTRANSISTORBJTBCV61"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BCV61', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-143', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/BCV61.pdf', 'kicadSymbolki_keywords': 'Transistor Double NPN', 'kicadSymbolki_description': '100mA IC, 30V Vce, Double NPN Transistors, Current mirror configuration, SOT-143', 'kicadSymbolki_fp_filters': 'SOT?143*'}])
    newPart['name'].append('BCV61')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

