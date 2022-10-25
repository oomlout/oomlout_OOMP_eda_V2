
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Intel"
    oIndex = "8088_Min_Mode"
    hexID = "SZKMCUINTEL888MINMODE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '8088', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '8088_Min_Mode', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'http://datasheets.chipdb.org/Intel/x86/808x/datashts/8088/231456-006.pdf', 'kicadSymbolki_keywords': 'MPRO', 'kicadSymbolki_description': '8088 (minimum mode), 8-Bit HMOS Microprocessor, PDIP-40', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('MCU_Intel : 8088_Min_Mode')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

