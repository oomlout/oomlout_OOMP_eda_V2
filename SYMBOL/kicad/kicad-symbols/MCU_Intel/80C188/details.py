
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Intel"
    oIndex = "80C188"
    hexID = "SZKMCUINTEL8C188"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '80C188', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://datasheets.chipdb.org/Intel/x86/8018x/datashts/80188/intel-80c188.pdf', 'kicadSymbolki_keywords': 'MPRO', 'kicadSymbolki_description': 'CHMOS High-Integration 16-Bit Microprocessor', 'kicadSymbolki_fp_filters': 'PLCC* PGA*Layout11x11*P2.54mm* LCC*'}])
    newPart['name'].append('MCU_Intel : 80C188')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

