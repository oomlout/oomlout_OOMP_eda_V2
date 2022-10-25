
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_HC11"
    oIndex = "68HC11_PLCC"
    hexID = "SZKMCUNXPHC1168HC11PLCC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '68HC11_PLCC', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'MCU Microcontroller HC11', 'kicadSymbolki_description': 'HC11 Microcontroller, PLCC-52'}])
    newPart['name'].append('MCU_NXP_HC11 : 68HC11_PLCC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

