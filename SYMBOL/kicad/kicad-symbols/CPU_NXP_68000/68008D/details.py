
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPU_NXP_68000"
    oIndex = "68008D"
    hexID = "SZKCPUNXP68688D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '68008D', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/reference-manual/MC68000UM.pdf', 'kicadSymbolki_keywords': '68000 Microprocessor CPU', 'kicadSymbolki_description': '16/32-bit Microprocessor, 8-bit databus'}])
    newPart['name'].append('68008D')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

