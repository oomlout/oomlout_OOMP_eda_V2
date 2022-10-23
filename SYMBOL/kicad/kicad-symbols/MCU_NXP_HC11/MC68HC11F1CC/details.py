
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_HC11"
    oIndex = "MC68HC11F1CC"
    hexID = "SZKMCUNXPHC11MC68HC11F1CC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC68HC11F1CC', 'kicadSymbolFootprint': 'Package_LCC:PLCC-68', 'kicadSymbolDatasheet': 'http://cache.freescale.com/files/microcontrollers/doc/data_sheet/MC68HC11F1.pdf', 'kicadSymbolki_keywords': 'HC11 MCU Microcontroller', 'kicadSymbolki_description': 'ROMless, 1K RAM, 512B EEPROM, PLCC-68', 'kicadSymbolki_fp_filters': 'PLCC*'}])
    newPart['name'].append('MC68HC11F1CC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

