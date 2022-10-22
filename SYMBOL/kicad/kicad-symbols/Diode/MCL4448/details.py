
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "MCL4448"
    hexID = "SZKDIODEMCL4448"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCL4148', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'MCL4448', 'kicadSymbolFootprint': 'Diode_SMD:D_MicroMELF', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/85566/mlc4148.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '75V 0.2A Switching Diode, MicroMELF', 'kicadSymbolki_fp_filters': 'D*MicroMELF*'}])
    newPart['name'].append('MCL4448')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

