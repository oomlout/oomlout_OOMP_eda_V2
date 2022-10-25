
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_HC11"
    oIndex = "68HC11A8"
    hexID = "SZKMCUNXPHC1168HC11A8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '68HC11', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '68HC11A8', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'MCU Microcontroller HC11', 'kicadSymbolki_description': 'HC11 Microcontroller'}])
    newPart['name'].append('MCU_NXP_HC11 : 68HC11A8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

