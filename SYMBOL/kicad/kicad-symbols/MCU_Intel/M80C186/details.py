
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Intel"
    oIndex = "M80C186"
    hexID = "SZKMCUINTELM8C186"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'M80C186', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://datasheets.chipdb.org/Intel/x86/8018x/datashts/80186/27050008.PDF', 'kicadSymbolki_keywords': 'MPRO', 'kicadSymbolki_description': 'CHMOS High-Integration 16-Bit Microprocessor', 'kicadSymbolki_fp_filters': 'PLCC* PGA*Layout11x11*P2.54mm* LCC*'}])
    newPart['name'].append('MCU_Intel : M80C186')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

