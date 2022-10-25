
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Intel"
    oIndex = "8039"
    hexID = "SZKMCUINTEL839"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '8035', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '8039', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'MCS-48 uC Microcontroller', 'kicadSymbolki_description': 'MCS-48 8-bit Microcontroller, No (EP)ROM, 128B RAM, DIP-40', 'kicadSymbolki_fp_filters': 'DIP* PDIP*'}])
    newPart['name'].append('MCU_Intel : 8039')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

