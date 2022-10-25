
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Intel"
    oIndex = "8050"
    hexID = "SZKMCUINTEL85"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '8035', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '8050', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'MCS-48 uC Microcontroller', 'kicadSymbolki_description': 'MCS-48 8-bit Microcontroller, 4KB Mask ROM, 256B RAM, DIP-40', 'kicadSymbolki_fp_filters': 'DIP* PDIP*'}])
    newPart['name'].append('MCU_Intel : 8050')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

