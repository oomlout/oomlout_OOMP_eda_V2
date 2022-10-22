
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "1N4148W"
    hexID = "SZKDIODE1N4148W"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '1N4001', 'kicadSymbolReference': 'D', 'kicadSymbolValue': '1N4148W', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-123', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/85748/1n4148w.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '75V 0.15A Fast Switching Diode, SOD-123', 'kicadSymbolki_fp_filters': 'D*SOD?123*'}])
    newPart['name'].append('1N4148W')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

