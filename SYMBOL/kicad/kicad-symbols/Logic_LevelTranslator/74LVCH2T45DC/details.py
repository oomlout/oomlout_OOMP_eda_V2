
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Logic_LevelTranslator"
    oIndex = "74LVCH2T45DC"
    hexID = "SZKLOGICLEVELTRANSLATOR74LVCH2T45DC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LVC2T45DC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LVCH2T45DC', 'kicadSymbolFootprint': 'Package_SO:VSSOP-8_2.3x2mm_P0.5mm', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/74LVC_LVCH2T45.pdf', 'kicadSymbolki_keywords': 'Level-Shifter CMOS-TTL-Translation', 'kicadSymbolki_description': 'Dual supply translating transceiver with bus-hold for unused/floating inputs, 3-state, 2-bit, VSSOP-8', 'kicadSymbolki_fp_filters': 'VSSOP*2.3x2mm*P0.5mm*'}])
    newPart['name'].append('74LVCH2T45DC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

