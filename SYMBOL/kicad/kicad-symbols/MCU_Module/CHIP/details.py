
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "CHIP"
    hexID = "SZKMCUMOCHIP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CHIP', 'kicadSymbolFootprint': 'Module:MODULE_NEXTTHINGCO_CHIP', 'kicadSymbolDatasheet': 'https://github.com/NextThingCo/CHIP-Hardware/tree/master/CHIP%5Bv1_0%5D', 'kicadSymbolki_keywords': 'nextthingco chip module', 'kicadSymbolki_description': 'NextThingCo C.H.I.P. Module', 'kicadSymbolki_fp_filters': 'MODULE*NEXTTHINGCO*CHIP*'}])
    newPart['name'].append('CHIP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

