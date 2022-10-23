
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "CHIP-PRO"
    hexID = "SZKMCUMOCHIPPRO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CHIP-PRO', 'kicadSymbolFootprint': 'Module:MODULE_NEXTTHINGCO_CHIPPRO', 'kicadSymbolDatasheet': 'https://github.com/NextThingCo/CHIP_Pro-Hardware/blob/master/Datasheets/CHIP_PRO_Datasheet_v1.0.pdf', 'kicadSymbolki_keywords': 'nextthingco chip pro module', 'kicadSymbolki_description': 'NextThingCo C.H.I.P. Pro Module', 'kicadSymbolki_fp_filters': 'MODULE*NEXTTHINGCO*CHIPPRO*'}])
    newPart['name'].append('CHIP-PRO')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

