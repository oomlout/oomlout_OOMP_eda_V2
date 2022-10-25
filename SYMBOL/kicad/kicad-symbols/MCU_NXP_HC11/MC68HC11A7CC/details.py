
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_HC11"
    oIndex = "MC68HC11A7CC"
    hexID = "SZKMCUNXPHC11MC68HC11A7CC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC68HC11A8CC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC68HC11A7CC', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'HC11 MCU Microcotroller', 'kicadSymbolki_description': '8K ROM, 256B RAM, 512B EEPROM'}])
    newPart['name'].append('MCU_NXP_HC11 : MC68HC11A7CC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

