
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPU_NXP_68000"
    oIndex = "68000D"
    hexID = "SZKCPUNXP6868D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '68000D', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/reference-manual/MC68000UM.pdf', 'kicadSymbolki_keywords': '68000 Microprocessor CPU', 'kicadSymbolki_description': '16/32-bit Microprocessor'}])
    newPart['name'].append('68000D')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

