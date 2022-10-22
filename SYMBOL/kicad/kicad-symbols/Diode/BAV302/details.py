
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BAV302"
    hexID = "SZKDIODEBAV32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCL4148', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BAV302', 'kicadSymbolFootprint': 'Diode_SMD:D_MicroMELF', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/85545/bav300.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '150V 0.25A Switching Diode, High Voltage, MicroMELF', 'kicadSymbolki_fp_filters': 'D*MicroMELF*'}])
    newPart['name'].append('BAV302')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

