
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_HC12"
    oIndex = "MC68HC912"
    hexID = "SZKMCUNXPHC12MC68HC912"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC68HC912', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': '68HC12 Microcontroller', 'kicadSymbolki_description': 'HC12 Microcontroller'}])
    newPart['name'].append('MCU_NXP_HC12 : MC68HC912')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

